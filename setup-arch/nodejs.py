from module import Module

CONFIGS = [
    '.npmrc'
]

PROGRAMS = {
    'node': 'sudo pacman -S --needed nodejs',
    'npm': 'sudo pacman -S --needed npm',
}

DEPENDENCIES = [
]


class NodeJs(Module):
    def __init__(self):
        super().__init__(
            'nodejs',
            'NodeJS + npm',
            CONFIGS,
            PROGRAMS,
            DEPENDENCIES,
        )
