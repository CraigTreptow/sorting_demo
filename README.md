# sorting_demo
An attempt to visualize various sorting algorithms using Python.

## To Do

- [ ] Add visualizations of the data (bar graph, etc.)
- [ ] Find a way to "step through" as the sorts run


## Running

`python -m sorting size_of_list (default is 20_000)`

## Setup Commands 

_create virtual environment_
`python3 -m venv venv`

_activate virtual environment_
`source venv/bin/activate`

_Note:_ To deactivate the virtual environment, simply type `deactivate` in the terminal.
_Note:_ To delete the virtual environment, simply delete the `venv` folder.
_Note:_ The above requires the  `bash`shell. If you are using `zsh` or `fish` or any other shell, please refer to the [official documentation](https://docs.python.org/3/library/venv.html) for the appropriate commands.


### zsh with oh_my_zsh setup

1. Add `virtualenv` to plugins list: `plugins=(virtualenv)`
2. Add plugin to theme prompt elements (I use powerlevel10k theme):
  1. Example:
  ```
  # The list of segments shown on the left. Fill it with the most important segments.
  typeset -g POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(
    # os_icon               # os identifier
    dir                     # current directory
    vcs                     # git status
    virtualenv              # python venv
    # prompt_char           # prompt symbol
  )
  ```

## pip Commands

`pip install -r requirements.txt`
