from module import Module

CONFIGS = [
    '.scripts',
]

PROGRAMS = {
}


class Scripts(Module):
    def __init__(self):
        super().__init__(
            'scripts',
            'Some useful scripts',
            CONFIGS,
            PROGRAMS
        )
