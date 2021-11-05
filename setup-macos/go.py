from module import Module

CONFIGS = [
]

PROGRAMS = {
    'go': 'brew install go',
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
