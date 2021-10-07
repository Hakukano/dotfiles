from module import Module

from nodejs import NodeJs
from rust import Rust

CONFIGS = [
    '.config/nvim',
    '.config/zathura',
    '.latexmkrc',
    '.vim',
]

PROGRAMS = {
    'nvim': 'sudo apt-get update && sudo apt-get install neovim python3-neovim',
    'ag': 'sudo apt-get install silversearcher-ag',
    'rg': 'cargo install ripgrep --features="pcre2"',
    'rust-analyzer': 'curl -L https://github.com/rust-analyzer/rust-analyzer/releases/latest/download/rust-analyzer-x86_64-unknown-linux-gnu.gz | gunzip -c - > ~/.local/bin/rust-analyzer && chmod +x ~/.local/bin/rust-analyzer',
    'clang': 'sudo apt-get install clang',
    'cscope': 'sudo apt-get install cscope',
    'cmake': 'sudo apt-get install cmake',
    'texlab': 'sudo apt-get install texlive && cargo install --git https://github.com/latex-lsp/texlab.git --locked',
    'zathura': 'sudo apt-get install zathura zathura-pdf-poppler',
    'cmake-language-server': 'pip install cmake-language-server',
    'pylsp': 'pip install python-lsp-server',
    'bash-language-server': 'npm install -g bash-language-server',
    'docker-langserver': 'npm install -g dockerfile-language-server-nodejs',
    'css-languageserver': 'npm install -g vscode-css-languageserver-bin',
    'html-languageserver': 'npm install -g vscode-html-languageserver-bin',
    'vscode-json-languageserver': 'npm install -g vscode-json-languageserver',
    'typescript-language-server':
        'npm install -g typescript typescript-language-server',
    'vim-language-server': 'npm install -g vim-language-server',
    'yaml-language-server': 'npm install -g yaml-language-server',
    'purescript-language-server': 'npm install -g purescript-language-server',
    'purty': 'npm install -g purty'
}

DEPENDENCIES = [
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
