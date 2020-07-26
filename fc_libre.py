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


__title__    = "FC_Libre"
__author__   = "Sal Polifemo <salp>"
__url__      = "https://github.com/???"
__date__     = "2020.07.26"
__version__  = 0.10

import os
import math
import re 


from FreeCAD import Gui 
from PySide import QtCore, QtGui 

import FreeCAD
import FreeCADGui
import Part


__dir__ = os.path.dirname(__file__)
iconPath = os.path.join( __dir__, 'Resources', 'icons' )

keepToolbar = True
windowFlags = QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint


def initialize():
    Gui.addCommand("FC_LibreLinkSpreadsheet",FC_LibreLinkSpreadsheetCommandClass())
    Gui.addCommand("FC_LibreImport",FC_LibreImportCommandClass())
    Gui.addCommand("FC_LibreExport",FC_LibreExportCommandClass())
    Gui.addCommand("FC_LibreSync",FC_LibreSyncCommandClass())
    
propertyTypes =[
    "Acceleration",
    "Angle",
    "Area",
    "Bool",
    "Color",
    "Direction",
    "Distance",
    "File",
    "FileIncluded",
    "Float",
    "FloatConstraint",
    "FloatList",
    "Font",
    "Force",
    "Integer",
    "IntegerConstraint",
    "IntegerList",
    "Length",
    "Link",
    "LinkChild",
    "LinkGlobal",
    "LinkList",
    "LinkListChild",
    "LinkListGlobal",
#    "Material",
    "MaterialList",
    "Matrix",
    "Path",
    "Percent",
    "Placement",
    "PlacementLink",
    "Position",
    "Precision",
    "Pressure",
    "Quantity",
    "QuantityConstraint",
    "Speed",
    "String",
    "StringList",
    "Vector",
    "VectorList",
    "VectorDistance",
    "Volume"]

nonLinkableTypes=[ #cannot be linked with setExpresion()
    "Bool",
    "Color",
    "File",
    "FileIncluded",
    "FloatList",
    "Font",
    "IntegerList",
    "Link",
    "LinkChild",
    "LinkGlobal",
    "LinkList",
    "LinkListChild",
    "LinkListGlobal",
    #"Material",
    "MaterialList",
    "Matrix",
    "Path",
    "PlacementLink",
    "String",
    "StringList",
    "VectorList"]

xyzTypes = [#x,y,z elements must be linked separately
    "Direction",
    "Position",
    "Vector",
    "VectorDistance"]    
    
    
    
    
    
    
    