from module import Module

CONFIGS = [
]

PROGRAMS = {
    'asdf': 'brew install asdf && mkdir ${HOME}/.settings && echo -e "\n. $(brew --prefix asdf)/libexec/asdf.sh" >> ${HOME}/.settings/path',
}

DEPENDENCIES = [
]


class Asdf(Module):
    def __init__(self):
        super().__init__(
            'asdf',
            'Asdf Version Manager',
            CONFIGS,
            PROGRAMS,
            DEPENDENCIES,
        )
