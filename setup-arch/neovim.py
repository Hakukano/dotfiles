from module import Module

from go import Go
from nodejs import NodeJs
from rust import Rust

CONFIGS = [
    '.config/nvim',
    '.config/zathura',
    '.latexmkrc',
    '.vim',
]

PROGRAMS = {
    'nvim': 'sudo pacman -S --needed neovim && pip install neovim',
    'ag': 'sudo pacman -S --needed the_silver_searcher',
    'rg': 'cargo install ripgrep --features="pcre2"',
    'rust-analyzer': 'yay -S --needed rust-analyzer-git',
    'clang': 'sudo pacman -S --needed clang',
    'cscope': 'sudo pacman -S --needed cscope',
    'cmake': 'sudo pacman -S --needed cmake',
    'texlab': 'sudo pacman -S --needed texlive-core texlab',
    'zathura': 'sudo pacman -S --needed zathura zathura-pdf-mupdf',
    'gopls': 'sudo pacman -S --needed gopls',
    'cmake-language-server': 'pip install cmake-language-server',
    'pylsp': 'pip install python-lsp-server',
    'bash-language-server': 'yarn global add bash-language-server',
    'docker-langserver': 'yarn global add dockerfile-language-server-nodejs',
    'css-languageserver': 'yarn global add vscode-css-languageserver-bin',
    'html-languageserver': 'yarn global add vscode-html-languageserver-bin',
    'vscode-json-languageserver': 'yarn global add vscode-json-languageserver',
    'typescript-language-server':
        'yarn global add typescript typescript-language-server',
    'vim-language-server': 'yarn global add vim-language-server',
    'yaml-language-server': 'yarn global add yaml-language-server',
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
