from module import Module, GIT_HOME
from module import ANSI_BOLD, ANSI_ERROR, ANSI_CLEAR, ANSI_SUCCESS
from tabulate import tabulate
import subprocess

CONFIGS = [
    '.tmux.conf',
]

PROGRAMS = {
    'tmux': 'sudo apt-get install tmux',
    'xsel': 'sudo apt-get install xsel',
    'xclip': 'sudo apt-get install xclip',
}

DEPENDENCIES = [
]

GIT_TPM = 'https://github.com/tmux-plugins/tpm'

DESCRIBE_HEADER_GIT = [
    'Repo',
    'Path',
    'Cloned',
]


class Tmux(Module):
    def __init__(self):
        super().__init__(
            'tmux',
            'tmux setup, Ctrl-b + i to install plugins',
            CONFIGS,
            PROGRAMS,
            DEPENDENCIES,
        )

    def status(self):
        s = super().status()
        if s == '{}Installed{}'.format(
            ANSI_SUCCESS,
            ANSI_CLEAR
        ):
            if not GIT_HOME.joinpath('tpm').is_dir():
                return '{}tpm does not exist{}'.format(
                    ANSI_ERROR,
                    ANSI_CLEAR,
                )
        return s

    def describe(self):
        d = super().describe()
        path = GIT_HOME.joinpath('tpm')
        cloned = '{}Y{}'.format(
            ANSI_SUCCESS,
            ANSI_CLEAR
        )
        if not path.is_dir():
            cloned = '{}N{}'.format(
                ANSI_ERROR,
                ANSI_CLEAR
            )
        git_rows = [[
            GIT_TPM,
            path,
            cloned
        ]]
        return '{}\n\n{}Git{}:\n{}'.format(
            d,
            ANSI_BOLD,
            ANSI_CLEAR,
            tabulate(git_rows, headers=DESCRIBE_HEADER_GIT)
        )

    def install(self):
        super().install()
        print('[INFO] Cloning tmux plugins manager')
        try:
            subprocess.run(
                'git clone {} {}'.format(
                    GIT_TPM,
                    str(GIT_HOME.joinpath('tpm'))
                ),
                shell=True,
                check=True,
            )
            print('[INFO] Done!')
        except subprocess.CalledProcessError:
            print(
                '[{}ERRO{}] Cannot clone tpm'.format(
                    ANSI_ERROR,
                    ANSI_CLEAR,
                )
            )
