from arch.go import Go
from arch.i3 import I3
from arch.neovim import NeoVim
from arch.nodejs import NodeJs
from arch.rust import Rust
from arch.scripts import Scripts
from arch.task import Task
from arch.tmux import Tmux
from arch.zsh import Zsh

MODULES = {
    'go': Go(),
    'i3': I3(),
    'neovim': NeoVim(),
    'nodejs': NodeJs(),
    'rust': Rust(),
    'scripts': Scripts(),
    'task': Task(),
    'tmux': Tmux(),
    'zsh': Zsh(),
}
