from module import Module

CONFIGS = [
]

PROGRAMS = {
    'cargo': 'asdf plugin add rust && asdf install rust stable && asdf global rust stable',
}

DEPENDENCIES = [
]


class Rust(Module):
    def __init__(self):
        super().__init__(
            'rust',
            'Rust + cargo',
            CONFIGS,
            PROGRAMS,
            DEPENDENCIES,
        )
