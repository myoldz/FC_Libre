##  FC Libre
A FreeCAD macro that exchanges data with the LibreOffice Calc module

### Prerequisites 
Currently this macro only runs on Linux and has the following dependencies;
* [LibreOffice](https://www.libreoffice.org/) must be installed
* [FreeCAD](https://www.freecadweb.org) v0.18 or higher
* The log file path is hardcoded, edit the  
  `LOG_FILENAME = '/mnt/data1/log/fc_libre.log'`  
to point to an existing directory on you PC

### Limitations 
This macro will terminate any open instances of LibreOffice, and then starts a new session.

### TODO
- [ ] Launch LibreOffice and listen on port 2002
- [ ] Detect if LibreOffice is currently running
- [ ] Shutdown existing instance of LibreOffice
- [ ] Select file to open before launching LibreOffice
- [ ] Open the selected Calc file
- [ ] Create link from FreeCAD to Calc file
- [ ] Read data from Calc file (by row,col and also by named range)
- [ ] Write data to Calc file (by row,col and also by named range)
- [ ] TODO: use different port if 2002 is being used
- [ ] TODO: Create a data structure in Calc
- [ ] TODO: duplicate Calc data structre in FreeCAD
- [ ] TODO: sync data if it chnages in either location (Calc or FreeCAD)
- [ ] TODO: Write properties of selected object to Calc file
- [ ] TODO: Make data visible to FreeCAD external variables function 
- [ ] TODO: verify path where `soffice` and `FreeCAD` are installed (used to import libraries)
- [ ] TODO: Allow selection of tab in active sheet
