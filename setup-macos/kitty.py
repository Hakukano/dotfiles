from module import Module

CONFIGS = [
    '.config/kitty'
]

PROGRAMS = {
    'kitty': 'brew install --cask kitty',
}

DEPENDENCIES = [
]


class Kitty(Module):
    def __init__(self):
        super().__init__(
            'kitty',
            'Kitty terminal',
            CONFIGS,
            PROGRAMS,
            DEPENDENCIES,
        )
