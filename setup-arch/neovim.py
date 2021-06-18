from module import Module

CONFIGS = [
    '.config/nvim',
    '.config/zathura',
    '.latexmkrc',
    '.vim',
]

PROGRAMS = {
    'nvim': 'yay -S neovim-git && pip install neovim',
    'ag': 'sudo pacman -S the_silver_searcher',
    'clang': 'sudo pacman -S clang',
    'cscope': 'sudo pacman -S cscope',
    'cmake': 'sudo pacman -S cmake',
    'rustup': 'sudo pacman -S rustup',
    'texlab': 'sudo pacman -S texlive-core texlab',
    'zathura': 'sudo pacman -S zathura zathura-pdf-mupdf',
    'cmake-language-server': 'pip install cmake-language-server',
    'pyls': 'pip install "python-language-server[all]"',
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


class NeoVim(Module):
    def __init__(self):
        super().__init__(
            'neovim',
            'NeoVim full setup, run ~/.fzf/install later!',
            CONFIGS,
            PROGRAMS
        )
