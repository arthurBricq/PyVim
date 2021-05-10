# Pyvim 

> Arthur Bricq

This repo contains a script to easily work with Vim in Python. The set up requires to have
- Vundle installed
- Jupyter-Vim installed with Vundle
- Jupyter-qtconsole installed.

The behavior is very simple, and it is just made to have a nicer setup than what is provided by the default installation (so, this is JUST setup steps !)

The **pyvim** command will simply 
- open python script in Vim
- open qtconsole if it is not already open, with default configs. 

## Installation

Once you have `git clone` the repo, run the following sequences: 

1. Let's add pyvim as executable
```
cp pyvim ~/.local/bin/pyvim
cd ~/.local/bin/pyvim
sudo chmod +y pyvim
```

2. Let's add a startup script for I-Python loaded by Jupyter-QtConsole (*Any code in this script will be run at every lunch of the console*)

```
cp 00-first.py ~/.python/profile_default/startup/00-first.py
```

To try if this worked, open a console and enter 'np'. If it worked, you will see something like '<numpy ...>'

3. And let's change the keybinds of jupyter-vim, so add the following lines at the end of the '~/.vimrc' script: 

```
" setups for jupyter kernel
nnoremap <C-r> :JupyterRunFile<CR>
nnoremap <C-x> :JupyterSendCell<CR>
nnoremap <C-e> :JupyterSendRange<CR>
```

Those are: 
- Ctrl + R: run the entire file 
- Ctrl + x: run the cell
- Ctrl + e: run the visual selection
