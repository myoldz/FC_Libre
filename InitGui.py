# -*- coding: utf-8 -*-
###################################################################################
#
#  InitGui.py
#  
#  Copyright 2020 Sal Polifemo <salp>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
###################################################################################

import FC_Librewb_locator
FC_LibreWBPath = os.path.dirname(FC_Librewb_locator.__file__)
FC_LibreWB_icons_path = os.path.join(FC_LibreWBPath, 'Resources', 'icons')

global main_FC_LibreWB_Icon
main_FC_LibreWB_Icon = os.path.join(FC_LibreWB_icons_path, 'FC_Libre3.png')


###################################################################################
# Initialize workbench

class FC_Libre ( Workbench ):
    "FC LibreOffice workbench object"
    
    global main_FC_LibreWB_Icon
    
    MenuText = "FC_Libre"
    ToolTip = "Spreadsheet interface workbench"
    Icon = main_FC_LibreWB_Icon
    
    def __init__(self):
        pass


    def Initialize(self):
        "This function is executed when FreeCAD starts"
        import fc_libre
        self.list = ["LinkSpreadsheet", "Export", "Import", "Sync"] # A list of command names created in the line above
        self.appendToolbar("FC_Libre Commands", self.list[:-1])      # leave settings off toolbar
        self.appendMenu("&FC_libre", self.list)                      # create new menu
        
            
    def Activated(self):
        " Function excuted on workbench activation"
        return


    def Deactivated(self):
        "Function excuted on workbench de-activated"
        #FreeCAD will hide our menu and toolbar upon exiting the wb, so we setup a singleshot
        #to unhide them once FreeCAD is finished, 2 seconds later
        from PySide import QtCore
        QtCore.QTimer.singleShot(2000, self.showMenu)
        return


    def showMenu(self):
        from PySide import QtGui
        window = QtGui.QApplication.activeWindow()
        #freecad hides wb toolbars on leaving wb, we unhide ours here to keep it around
        #if the user has it set in parameters to do so
        pg = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/FC_Libre")
        keep = pg.GetBool('KeepToolbar',True)
        if not keep:
            return
        tb = window.findChildren(QtGui.QToolBar) 
        for bar in tb:
            if "FC_Libre Commands" in bar.objectName():
                bar.setVisible(True)        
    
    
    
    def ContextMenu(self, recipient):
        "Function executed whenever the user right-clicks on screen"
        # "recipient" will be either "view" or "tree"
        self.appendContextMenu("FC_Libre",self.list) # add commands to the context menu
        
    
    def GetClassName(self):
        "Mandatory function if this is a full python workbench"
        return "Gui::PythonWorkbench"
    

wb = FC_Libre()
Gui.addWorkbench(wb)
