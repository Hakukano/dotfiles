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
    'nvim': 'brew install neovim',
    'ag': 'brew install the_silver_searcher',
    'rg': 'cargo install ripgrep --features="pcre2"',
    'rust-analyzer': 'brew install rust-analyzer',
    'clang': 'brew install llvm',
    'texlab': 'brew install texlab',
    'gopls': 'brew install gopls',
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
