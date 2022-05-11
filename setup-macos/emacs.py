import subprocess
from module import Module

CONFIGS = [
    '.emacs.d',
]

PROGRAMS = {
    'emacs': 'brew install emacs',
}

DEPENDENCIES = [
]


class Emacs(Module):
    def __init__(self):
        super().__init__(
            'emacs',
            'Emacs!?',
            CONFIGS,
            PROGRAMS,
            DEPENDENCIES,
        )
