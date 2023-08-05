from macos.asdf import Asdf
from macos.go import Go
from macos.idea import Idea
from macos.neovim import NeoVim
from macos.nodejs import NodeJs
from macos.rust import Rust
from macos.scripts import Scripts
from macos.tmux import Tmux
from macos.zsh import Zsh

MODULES = {
    'asdf': Asdf(),
    'go': Go(),
    'idea': Idea(),
    'neovim': NeoVim(),
    'nodejs': NodeJs(),
    'rust': Rust(),
    'scripts': Scripts(),
    'tmux': Tmux(),
    'zsh': Zsh(),
}
