'''
    Application to control LibreOffice Calc from inside FreeCAD enviroment
    Funtions:
    Launch LibreOffice and listen on port 2002
    TODO: use different port if 2002 is being used
    Detect if LibreOffice is currently running
    Shutdown existing instance of LibreOffice
    Select file to open before launching LibreOffice
    Open the selected Calc file
    Create link from FreeCAD to Calc file
    Read data from Calc file (by row,col and also by named range)
    Write data to Calc file (by row,col and also by named range)
    TODO: Create a data structure in Calc
    TODO: duplicate Calc data structre in FreeCAD
    TODO: sync data if it chnages in either location (Calc or FreeCAD)
    TODO: Write properties of selected object to Calc file
    TODO: Make data visible to FreeCAD external variables function 
    >> PHASE II
    TODO: verify path where soffice and freecad are installed (used to import libraries)
    TODO: Allow selection of tab in active sheet
    

'''

import sys
sys.path.append('/usr/lib/libreoffice/program')
sys.path.append('/usr/lib/freecad-daily/lib')

import time
import psutil
import subprocess
import re
import socket
import errno
import logging
import PySide2
from PySide2 import (QtWidgets, QtCore, QtGui)
import uno
import FreeCAD
import FreeCADGui


def port_in_use(port):
    testSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    location = ("localhost", port)
    #location = ("127.0.0.1", 16793)
    #socket_status = testSocket.connect_ex(location)
    try:
        testSocket.bind(location)
    except socket.error as e:
        if e.errno == errno.EADDRINUSE:
            logging.debug(f'func port_in_use: {location} status:{e}')
            return 1
        else:
            logging.debug(f'func port_in_use: {location} status: {e}')
            return 0


def app_exist(app_name):
    from shutil import which
    return which(app_name) is not None


def check_process(name, value):
    #if process is running and if arguments include 'value' then return the PID #
    logging.debug(str(name))
    for proc in psutil.process_iter():
        try:
            # Search process name & return process PID
            processName = proc.name()
            if processName == name:
                processCmd = proc.cmdline()  # list of arguments
                for i in processCmd:
                    found = re.search('(?<=port.)\d+', i)
                    if  found:
                        logging.debug(proc.pid)
                        return proc.pid
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return 0


def sofficeStart(value):
    run_soffice = [
                'soffice',
                '--accept=socket,host=localhost,port=' + str(value) +';urp;StarOffice.Service',
                '--nologo',
                '--norestore',
                '--minimized',
                '--invisible', 
            ]
    subprocess.Popen(run_soffice)
    logging.debug(f'start soffice with arg: {run_soffice}')
    time.sleep(1)


#setup_logging
LOG_FILENAME = '/mnt/data1/log/fc_libre.log'
LOG_FORMAT = "%(asctime)s : %(funcName)s : %(levelname)s : %(lineno)i : %(message)s"
LOG_LEVEL = ''
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG, format=LOG_FORMAT) 
logging.debug('--  New session  --')

pathFile  = "~/"
### Read a file
ReadName, Filter = PySide2.QtWidgets.QFileDialog.getOpenFileName(None, "Read a file",  pathFile, "Icon Calc  (*.ods);;"
                                                                                              "All files  (*.*);;"
                                                                                              "Image BMP  Windows Bitmap (*.bmp);;"
                                                                                              "Icon ICO  (*.ico);;"
                                                                                              "Icon Calc  (*.ods);;"
                                                                                              "Image JPEG Joint Photographic Experts Group (*.jpeg);;"
                                                                                              "Image JPG Joint Photographic Experts Group (*.jpg);;"
                                                                                              "Image PNG Portable Network Graphics  (*.png);;"
                                                                                              "Image PPM Portable Pixmap (*.ppm);;"
                                                                                              "Image TIF Tagged Image File Format (*.tif);;"
                                                                                              "Image TIFF Tagged Image File Format (*.tiff);;"
                                                                                              "Image GIF Graphic Interchange Format (*.gif);;"
                                                                                              "Image XBM X11 Pixmap (*.xbm);;"
                                                                                              "Image XPM X11 Pixmap (*.xpm);;"
                                                                                              )

logging.debug(f'User file selection: {ReadName}')

#Test if soffice is running and listening on port
port = 2002
procID = check_process('soffice.bin', port)
if procID > 1:
    logging.debug(f'soffice.bin listening on port {procID}')
    portStatus = port_in_use(port)
    if portStatus > 0:
        logging.debug(f'Kill soffice, PID: {procID}')
        p = psutil.Process(procID)
        p.terminate()
        time.sleep(1)

logging.debug(f'start sofficel, listen on port {port}')
sofficeStart(port)
procID = check_process('soffice.bin', port)
logging.debug(f'soiffice.bin process ID: {procID}')

# common code to connect to Calc spreadsheet
localContext = uno.getComponentContext()
resolver = localContext.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", localContext)
ctx = resolver.resolve("uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext")
smgr = ctx.ServiceManager
desktop = smgr.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)
document = desktop.loadComponentFromURL("file://"+ReadName, "_blank", 0, ())
#Link to active spreadsheet
active_sheet = document.CurrentController.ActiveSheet

# Write string to cell "C2"
cell1 = active_sheet.getCellRangeByName("C2")
cell1.String = "Hey , I'm working ?"

# Write string to cell named "name_of_range"
rangeName = active_sheet.getCellRangeByName("name_of_range")
rangeName.String = "Write to named range"

# Create App::FeaturePython object & add properties
ref_obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "fc_libre")
ref_obj.Label = "uno_test_calc.ods"
oRanges = document.NamedRanges.getElementNames()
for oName in oRanges:
    value = active_sheet.getCellRangeByName(oName).String
    logging.debug(f'set property name = {oName}  |  value = {value}')
    ref_obj.addProperty("App::PropertyFloat", oName)
    setattr(ref_obj, oName, float(value))


