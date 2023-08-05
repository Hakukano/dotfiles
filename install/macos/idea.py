from module import Module

CONFIGS = [
    '.ideavimrc',
]

PROGRAMS = {
}

DEPENDENCIES = [
]


class Idea(Module):
    def __init__(self):
        super().__init__(
            'idea',
            'Jetbrains idea configs',
            CONFIGS,
            PROGRAMS,
            DEPENDENCIES,
        )
