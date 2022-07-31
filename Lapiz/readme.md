# Lapiz
Python 3 terminal emulator made using Prompt Toolkit. Designed to make working in the terminal faster

# Requirments
```
pip install prompt_toolkit
```

# How to install (Requires: Git, Python 3)
```
git clone https://github.com/CompanionCubeGD/Mini-Projects
cd Mini-Projects/Lapiz
python(3) Lapiz.py
```

# Features
Currently it has a tab-list and auto suggest but I will be add more

# Todo
- [ ] Add Windows Binary
- [ ] Add GUI
- [ ] Add Features For Faster Use (Like Macro Support & Keybinds)
- [ ] Add A Config File To Easily Configure Lapiz To Your Liking

# How To Cuztomize
you can add more stuff to it by using Prompt Toolkit (Docs: https://python-prompt-toolkit.readthedocs.io/en/master/)

You can add tab-list words by editing the words inside Word Completer:
```
html_completer = WordCompleter([''])
```

You can add custom commands by making a if statment in in the while True loop. Example:
```
    if text == 'quit':
        quit()
```

You can also edit the toolbar (Also sense the toolbar is just html code you can format it using html.)
```
def bottom_toolbar():
    return HTML('type quit to quit')
```
