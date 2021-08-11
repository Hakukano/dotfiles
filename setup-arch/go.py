from module import Module

CONFIGS = [
]

PROGRAMS = {
    'go': 'sudo pacman -S --needed go',
}

DEPENDENCIES = [
]


class Go(Module):
    def __init__(self):
        super().__init__(
            'go',
            'Golang',
            CONFIGS,
            PROGRAMS,
            DEPENDENCIES,
        )
