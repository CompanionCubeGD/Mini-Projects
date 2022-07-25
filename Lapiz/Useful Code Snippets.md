# Syntax Highlighting Example
```
from pygments.lexers.html import HtmlLexer
from prompt_toolkit.shortcuts import prompt
from prompt_toolkit.lexers import PygmentsLexer

text = prompt('Enter HTML: ', lexer=PygmentsLexer(HtmlLexer))
print('You said: %s' % text)
```

# Autocomplition Example
```
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

html_completer = WordCompleter(['<html>', '<body>', '<head>', '<title>'])
text = prompt('Enter HTML: ', completer=html_completer)
print('You said: %s' % text)
```

# Auto Suggestion Example
```
from prompt_toolkit import PromptSession
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory

session = PromptSession()

while True:
    text = session.prompt('> ', auto_suggest=AutoSuggestFromHistory())
    print('You said: %s' % text)
```

# Toolbar Example
```
from prompt_toolkit import prompt
from prompt_toolkit.formatted_text import HTML

def bottom_toolbar():
    return HTML('This is a <b><style bg="ansired">Toolbar</style></b>!')

text = prompt('> ', bottom_toolbar=bottom_toolbar)
print('You said: %s' % text)
```

# Custom Keybinding Example
```
from prompt_toolkit import prompt
from prompt_toolkit.application import run_in_terminal
from prompt_toolkit.key_binding import KeyBindings

bindings = KeyBindings()

@bindings.add('c-t')
def _(event):
    " Say 'hello' when `c-t` is pressed. "
    def print_hello():
        print('hello world')
    run_in_terminal(print_hello)

@bindings.add('c-x')
def _(event):
    " Exit when `c-x` is pressed. "
    event.app.exit()

text = prompt('> ', key_bindings=bindings)
print('You said: %s' % text)
```

# Multi-Line Example
```
from prompt_toolkit import prompt

def prompt_continuation(width, line_number, is_soft_wrap):
    return '.' * width
    # Or: return [('', '.' * width)]

prompt('multiline input> ', multiline=True,
       prompt_continuation=prompt_continuation)
```

# Mouse Support Example
```
from prompt_toolkit import prompt

prompt('What is your name: ', mouse_support=True)

```

# Password Input Example
```
from prompt_toolkit import prompt

prompt('Enter password: ', is_password=True)
```

# DIfferent Cursor Examples
```
from prompt_toolkit import prompt
from prompt_toolkit.cursor_shapes import CursorShape, ModalCursorShapeConfig

# Several possible values for the `cursor_shape_config` parameter:
prompt('>', cursor=CursorShape.BLOCK)
prompt('>', cursor=CursorShape.UNDERLINE)
prompt('>', cursor=CursorShape.BEAM)
prompt('>', cursor=CursorShape.BLINKING_BLOCK)
prompt('>', cursor=CursorShape.BLINKING_UNDERLINE)
prompt('>', cursor=CursorShape.BLINKING_BEAM)
prompt('>', cursor=ModalCursorShapeConfig())
```

# Progress Bar Example
```
from prompt_toolkit.shortcuts import ProgressBar
import time


with ProgressBar() as pb:
    for i in pb(range(800)):
        time.sleep(.01)
```

# Full Application Example (Using Keybinds And Progress Bar)
```
from prompt_toolkit import HTML
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.patch_stdout import patch_stdout
from prompt_toolkit.shortcuts import ProgressBar

import os
import time
import signal

bottom_toolbar = HTML(' <b>[f]</b> Print "f" <b>[x]</b> Abort.')

# Create custom key bindings first.
kb = KeyBindings()
cancel = [False]

@kb.add('f')
def _(event):
    print('You pressed `f`.')

@kb.add('x')
def _(event):
    " Send Abort (control-c) signal. "
    cancel[0] = True
    os.kill(os.getpid(), signal.SIGINT)

# Use `patch_stdout`, to make sure that prints go above the
# application.
with patch_stdout():
    with ProgressBar(key_bindings=kb, bottom_toolbar=bottom_toolbar) as pb:
        for i in pb(range(800)):
            time.sleep(.01)

            # Stop when the cancel flag has been set.
            if cancel[0]:
                break
```

# App Example
```
from prompt_toolkit import Application

app = Application(full_screen=True)
app.run()
```

# Window Focusing Example
```
from prompt_toolkit.application import get_app

# This window was created earlier.
w = Window()

# ...

# Now focus it.
get_app().layout.focus(w)
```

# Second Keybinding Example
```
from prompt_toolkit import Application
from prompt_toolkit.key_binding import KeyBindings

kb = KeyBindings()

@kb.add('c-q')
def exit_(event):
    """
    Pressing Ctrl-Q will exit the user interface.

    Setting a return value means: quit the event loop that drives the user
    interface and return this value from the `Application.run()` call.
    """
    event.app.exit()

app = Application(key_bindings=kb, full_screen=True)
app.run()
```

