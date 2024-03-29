from module import Module

CONFIGS = [
    '.npmrc'
]

PROGRAMS = {
    'node': 'asdf plugin add nodejs && asdf install nodejs latest && asdf global nodejs latest',
    'yarn': 'npm install -g yarn; yarn config set prefix ~/.yarn',
}

DEPENDENCIES = [
]


class NodeJs(Module):
    def __init__(self):
        super().__init__(
            'nodejs',
            'NodeJS + npm + yarn',
            CONFIGS,
            PROGRAMS,
            DEPENDENCIES,
        )
