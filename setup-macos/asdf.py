from module import Module

CONFIGS = [
]

PROGRAMS = {
    'asdf': 'brew install asdf',
}

DEPENDENCIES = [
]


class Asdf(Module):
    def __init__(self):
        super().__init__(
            'asdf',
            'Extendable version manager with support for Ruby, Node.js, Erlang & more',
            CONFIGS,
            PROGRAMS,
            DEPENDENCIES,
        )
