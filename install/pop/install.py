from pop.gnome import Gnome
from pop.neovim import NeoVim
from pop.nodejs import NodeJs
from pop.rust import Rust
from pop.scripts import Scripts
from pop.tmux import Tmux
from pop.zsh import Zsh

MODULES = {
    'gnome': Gnome(),
    'neovim': NeoVim(),
    'nodejs': NodeJs(),
    'rust': Rust(),
    'scripts': Scripts(),
    'tmux': Tmux(),
    'zsh': Zsh(),
}
