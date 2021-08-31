from module import Module

CONFIGS = [
    '.zsh_completion',
    '.p10k.zsh',
    '.zgen-setup',
    '.zsh_aliases',
    '.zsh_functions',
    '.zshrc',
]

PROGRAMS = {
    'zsh': 'sudo apt-get install zsh',
}

DEPENDENCIES = [
]


class Zsh(Module):
    def __init__(self):
        super().__init__(
            'zsh',
            'zsh + zgen, run chsh -s /bin/zsh later!',
            CONFIGS,
            PROGRAMS,
            DEPENDENCIES,
        )
