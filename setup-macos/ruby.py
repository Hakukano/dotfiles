from module import Module

from asdf import Asdf

CONFIGS = [
]

PROGRAMS = {
    'ruby': 'asdf plugin add ruby && asdf install ruby latest',
}

DEPENDENCIES = [
    Asdf(),
]


class Ruby(Module):
    def __init__(self):
        super().__init__(
            'ruby',
            'Ruby',
            CONFIGS,
            PROGRAMS,
            DEPENDENCIES,
        )
