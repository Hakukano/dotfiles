import subprocess
from module import Module

CONFIGS = [
    '.zsh_completion',
    '.p10k.zsh',
    '.zgen-setup',
    '.zsh_aliases',
    '.zsh_functions',
    '.zshrc',
]

PROGRAMS = {
    'zsh': 'sudo apt-get install zsh',
    'curl': 'sudo apt-get install curl',
}

DEPENDENCIES = [
]


class Zsh(Module):
    def __init__(self):
        super().__init__(
            'zsh',
            'zsh + zgen',
            CONFIGS,
            PROGRAMS,
            DEPENDENCIES,
        )

    def install(self):
        super().install()
        print('[INFO] Running chsh')
        try:
            subprocess.run(
                'chsh -s /bin/zsh',
                shell=True,
                check=True,
            )
            print('[INFO] Done!')
        except subprocess.CalledProcessError:
            print(
                '[{}ERRO{}] Cannot call chsh'.format(
                    ANSI_ERROR,
                    ANSI_CLEAR,
                )
            )
