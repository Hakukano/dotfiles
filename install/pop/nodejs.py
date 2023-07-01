from module import Module

CONFIGS = [
    '.npmrc'
]

PROGRAMS = {
    'node': 'sudo apt-get install nodejs',
    'npm': 'sudo apt-get install npm',
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
