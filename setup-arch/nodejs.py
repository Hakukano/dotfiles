from module import Module

CONFIGS = [
]

PROGRAMS = {
    'node': 'sudo pacman -S nodejs',
    'npm': 'sudo pacman -S npm',
}


class NodeJs(Module):
    def __init__(self):
        super().__init__('nodejs', 'NodeJS + npm', CONFIGS, PROGRAMS)
