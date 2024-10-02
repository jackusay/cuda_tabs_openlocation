import os
import subprocess

from cudatext import *

from cudax_lib import get_translation
_ = get_translation(__file__)  # I18N
PRE = '[Tabs open location]'

class Command:
    def tab_open_location(self): #method in install.inf
        return run() 
    def on_start2(self, ed_self):   return run() #Called once on program start.

def open_tab_on_explorer():
    filepath = ed.get_filename()
    print(f'{filepath}')
    if os.path.isfile(filepath):
        #only works on Windows OS
        subprocess.Popen(fr'explorer /select, "{filepath}"') # insecurity
          # https://stackoverflow.com/questions/281888/open-explorer-on-a-file?answertab=modifieddesc#comment123838403_49159988
    else:
        msg_status(PRE + _("File doesn't exist"))
    print("eee")
    return
    
def run():
    menu_proc( menu_proc("tab", MENU_GET_PROP)['id'] , MENU_ADD, command=open_tab_on_explorer, caption='Open explorer')
    msg_status(PRE + _('JOB DONE'))