# FC_Libre
FreeCAD macro to exchnage data with Libre Office Calc module

Currently this macro only runs on Linux and has the following dependencies;

> Libre Office must be installed

> FreeCAD version .18 or higher

## Solved:
    - Launch LibreOffice and listen on port 2002
    - Detect if LibreOffice is currently running
    - Shutdown existing instance of LibreOffice
    - Select file to open before launching LibreOffice
    - Open the selected Calc file
    - Create link from FreeCAD to Calc file
    - Read data from Calc file (by row,col and also by named range)
    - Write data to Calc file (by row,col and also by named range)
    
## TODO:
    1 TODO: use different port if 2002 is being used
    2 TODO: Create a data structure in Calc
    3 TODO: duplicate Calc data structre in FreeCAD
    4 TODO: sync data if it chnages in either location (Calc or FreeCAD)
    5 TODO: Write properties of selected object to Calc file
    6 TODO: Make data visible to FreeCAD external variables function 
    7 TODO: verify path where soffice and freecad are installed (used to import libraries)
    8 TODO: Allow selection of tab in active sheet
