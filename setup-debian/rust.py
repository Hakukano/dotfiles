from module import Module

CONFIGS = [
]

PROGRAMS = {
    'rustup': 'curl --proto "=https" --tlsv1.2 -sSf https://sh.rustup.rs | sh && rustup install nightly',
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
