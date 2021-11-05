from module import Module

CONFIGS = [
]

PROGRAMS = {
    'rustup': 'brew install rustup-init && rustup-init',
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
