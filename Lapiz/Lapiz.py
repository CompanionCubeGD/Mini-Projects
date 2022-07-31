#Modules
from prompt_toolkit.cursor_shapes import CursorShape, ModalCursorShapeConfig
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit import PromptSession
import config
import os 

# You can find documentation @
# 1: The Github Repo (https://github.com/companioncubegd/Mini-ProjectsLapiz)
# 2: Prompt Toolkit Documentation: https://python-prompt-toolkit.readthedocs.io/en/master/


#in WordCompleter insert your tab-list words, session is history suggest (it will suggest things from you command history)
html_completer = WordCompleter(config.tablist)
session = PromptSession()

#Toolbar (optional, delete if you dont want it. Make sure to also delete the bottom_toolbar=bottom_toolbar() in the text)
def bottom_toolbar():
    return HTML(config.deftoolbar)

#Actaul Terminal Emulator
while True:
    text = session.prompt(config.promt, auto_suggest=AutoSuggestFromHistory(), completer=html_completer, bottom_toolbar=bottom_toolbar())
    
    #Quit
    if text == 'quit':
        quit()
        
    os.system(text)
