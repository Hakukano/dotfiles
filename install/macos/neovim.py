from module import Module

from macos.go import Go
from macos.nodejs import NodeJs
from macos.rust import Rust

CONFIGS = [
    '.config/nvim',
    '.config/zathura',
    '.latexmkrc',
    '.vim',
]

PROGRAMS = {
    'nvim': 'brew install neovim',
    'ag': 'brew install the_silver_searcher',
    'rg': 'cargo install ripgrep --features="pcre2"',
}

DEPENDENCIES = [
    Go(),
    NodeJs(),
    Rust(),
]


class NeoVim(Module):
    def __init__(self):
        super().__init__(
            'neovim',
            'NeoVim full setup, run ~/.fzf/install later!',
            CONFIGS,
            PROGRAMS,
            DEPENDENCIES,
        )
