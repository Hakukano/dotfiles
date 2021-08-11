from module import Module

CONFIGS = [
]

PROGRAMS = {
    'rustup': 'sudo pacman -S --needed rustup && rustup install nightly',
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
