from debian.neovim import NeoVim
from debian.nodejs import NodeJs
from debian.rust import Rust
from debian.scripts import Scripts
from debian.tmux import Tmux
from debian.zsh import Zsh

MODULES = {
    'neovim': NeoVim(),
    'nodejs': NodeJs(),
    'rust': Rust(),
    'scripts': Scripts(),
    'tmux': Tmux(),
    'zsh': Zsh(),
}
