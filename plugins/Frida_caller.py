import re
import idaapi
import idc
from idc import *
from idaapi import *
import PyQt4
from PyQt4 import QtCore, QtGui
import idautils

class caramber(idaapi.plugin_t):
    flags = idaapi.PLUGIN_FIX
    comment = "This is a comment"

    help = "Plugin That uses Frida API"
    wanted_name = "Frida"
    wanted_hotkey = ""



    def init(self):
        idaapi.msg(" Frida Plugin Is Found.\nLoad Via Plugins")
        return idaapi.PLUGIN_OK

    def run(self, arg):
        idaapi.msg("run() called with %d!\n" % arg)

    def term(self):
        idaapi.msg("")
    
    def AddMenuElements(self):
        '''Menus are better than no GUI at all *sigh*'''

        idaapi.add_menu_item("Debugger/", "frida", "", 0, self.Poppers, ())




    def run(self, arg = 0):
        idaapi.msg("Frida Widget is Found\nAfter its Loaded\nFind It Under Debugger Menu")

        self.AddMenuElements()

    def Poppers(self):
        g = globals()
        idahome = idaapi.idadir("QTApps\\Frida")
        IDAPython_ExecScript(idahome +  "\\Frida_For_Ida_Pro.py", g)



def PLUGIN_ENTRY():
    return caramber()
