# Lapiz
Python 3 terminal emulator make using Prompt Toolkit

# Requirments
```
pip install prompt_toolkit
```

# Features
Currently it has a tab-list and auto suggest but I will be add more

# Todo
- [ ] Add Windows Binary
- [ ] Add GUI
- [ ] Add For Features For Faster Use

# How To Cuztomize
you can add more stuff to it by using Prompt Toolkit (Docs: https://python-prompt-toolkit.readthedocs.io/en/master/)

You can add tab-list words by editing the words inside Word Completer:
```
html_completer = WordCompleter([''])
```

You can add custom commands by making a if statment in in the while True loop
```
    if text == 'quit':
        quit()
```

You can also edit the toolbar
```
def bottom_toolbar():
    return HTML('type quit to quit')
```
