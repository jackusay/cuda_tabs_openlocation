import os
import subprocess

from cudatext import *

from cudax_lib import get_translation
_ = get_translation(__file__)  # I18N
PRE = '[Tabs open location]'

class Command:
    def tab_open_location(self): #method in install.inf
        return run() 
    def on_tab_menu(self, ed_self):   return run(ed_self)

def open_tab_on_explorer(ed_self):
    filepath = ed_self.get_filename()
    if os.path.isfile(filepath):
        #only works on Windows OS
        subprocess.Popen(fr'explorer /select, "{filepath}"') # insecurity
          # https://stackoverflow.com/questions/281888/open-explorer-on-a-file?answertab=modifieddesc#comment123838403_49159988
    else:
        msg_status(PRE + _("File doesn't exist"))
    print("eee")
    return
    
def run(ed_self):
    menu_proc(  menu_proc("tab", MENU_GET_PROP)['id'] , MENU_ADD, 
                command=lambda: open_tab_on_explorer(ed_self), # Use lambda to delay the execution
                caption='Open explorer')
    msg_status(PRE + _('JOB DONE'))