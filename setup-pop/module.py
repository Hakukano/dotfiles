from pathlib import Path
from tabulate import tabulate
import shutil
import subprocess

ANSI_CLEAR = '\033[0m'
ANSI_BOLD = '\033[1m'
ANSI_ERROR = '\033[91m'
ANSI_SUCCESS = '\033[92m'
ANSI_WARNING = '\033[93m'

SRC_HOME = Path(__file__).parent.parent.absolute().joinpath('home')
DST_HOME = Path.home()

GIT_HOME = DST_HOME.joinpath('Git')

DESCRIBE_HEADER_PROGRAM = [
    'Name',
    'Command',
    'Installed',
]
DESCRIBE_HEADER_CONFIG = [
    'Source',
    'Destination',
    'Linked',
]
DESCRIBE_HEADER_DEPENDENCY = [
    'Name',
    'Description',
    'Status',
    'Installed',
]


class Module:
    def __init__(self, name, description, configs, programs, dependencies):
        self.name = name
        self.description = description
        self.configs = configs
        self.programs = programs
        self.dependencies = dependencies

    def to_brief_row(self):
        installed = '{}N{}'.format(
            ANSI_ERROR,
            ANSI_CLEAR,
        )
        if self.installed():
            installed = '{}Y{}'.format(
                ANSI_SUCCESS,
                ANSI_CLEAR
            )
        return [
            self.name,
            self.description,
            self.status(),
            installed,
        ]

    def status(self):
        for dependency in self.dependencies:
            if not dependency.installed():
                return '{}Dependency: {} is not installed{}'.format(
                    ANSI_ERROR,
                    dependency.name,
                    ANSI_CLEAR,
                )
        for program in self.programs.keys():
            if shutil.which(program) is None:
                return '{}{} does not exist{}'.format(
                    ANSI_ERROR,
                    program,
                    ANSI_CLEAR,
                )
        for config in self.configs:
            src = SRC_HOME.joinpath(config)
            dst = DST_HOME.joinpath(config)
            if not dst.exists():
                return '{}{} does not exist{}'.format(
                    ANSI_ERROR,
                    dst,
                    ANSI_CLEAR,
                )
            if not dst.is_symlink():
                return '{}{} is not a symlink{}'.format(
                    ANSI_WARNING,
                    dst,
                    ANSI_CLEAR,
                )
            if dst.readlink() != src:
                return '{}{} links to wrong target{}'.format(
                    ANSI_WARNING,
                    dst,
                    ANSI_CLEAR,
                )
        return '{}Installed{}'.format(
            ANSI_SUCCESS,
            ANSI_CLEAR
        )

    def installed(self):
        return self.status() == '{}Installed{}'.format(
            ANSI_SUCCESS,
            ANSI_CLEAR
        )

    def describe(self):
        program_rows = []
        for name, command in self.programs.items():
            installed = '{}Y{}'.format(
                ANSI_SUCCESS,
                ANSI_CLEAR
            )
            if shutil.which(name) is None:
                installed = '{}N{}'.format(
                    ANSI_ERROR,
                    ANSI_CLEAR
                )
            program_rows.append([
                name,
                command,
                installed,
            ])
        config_rows = []
        for config in self.configs:
            linked = '{}Y{}'.format(
                ANSI_SUCCESS,
                ANSI_CLEAR
            )
            src = SRC_HOME.joinpath(config)
            dst = DST_HOME.joinpath(config)
            if not dst.exists():
                linked = '{}{} does not exist{}'.format(
                    ANSI_ERROR,
                    dst,
                    ANSI_CLEAR,
                )
            if not dst.is_symlink():
                linked = '{}{} is not a symlink{}'.format(
                    ANSI_WARNING,
                    dst,
                    ANSI_CLEAR,
                )
            if dst.is_symlink() and dst.readlink() != src:
                linked = '{}{} links to wrong target{}'.format(
                    ANSI_WARNING,
                    dst,
                    ANSI_CLEAR,
                )
            config_rows.append([
                str(src),
                str(dst),
                linked,
            ])
        dependency_rows = []
        for dependency in self.dependencies:
            dependency_rows.append(dependency.to_brief_row())
        return '{}Programs{}:\n{}\n\n\
{}Configs{}:\n{}\n\n\
{}Dependencies{}:\n{}'.format(
            ANSI_BOLD,
            ANSI_CLEAR,
            tabulate(program_rows, headers=DESCRIBE_HEADER_PROGRAM),
            ANSI_BOLD,
            ANSI_CLEAR,
            tabulate(config_rows, headers=DESCRIBE_HEADER_CONFIG),
            ANSI_BOLD,
            ANSI_CLEAR,
            tabulate(dependency_rows, headers=DESCRIBE_HEADER_DEPENDENCY),
        )

    def install(self):
        print('[INFO] Installing module: {}'.format(self.name))
        for dependency in self.dependencies:
            if not dependency.installed():
                print('[{}WARN{}] Dependency: {} is not installed\
, installing it'.format(ANSI_WARNING, dependency.name, ANSI_CLEAR))
                dependency.install()
                if not dependency.installed():
                    print('[{}ERRO{}] Cannot install dependency: {}'.format(
                        ANSI_ERROR, dependency.name, ANSI_CLEAR
                    ))
                    return
        print('[INFO] Linking configs...')
        for config in self.configs:
            src = SRC_HOME.joinpath(config)
            dst = DST_HOME.joinpath(config)
            if dst.exists() and (not dst.is_symlink()):
                print(
                    '[{}ERRO{}] {} is not a symlink, '
                    'please remove it manually'.format(
                        ANSI_ERROR,
                        ANSI_CLEAR,
                        dst,
                    )
                )
                print(
                    '[{}ERRO{}] Cannot install module: {}'.format(
                        ANSI_ERROR,
                        ANSI_CLEAR,
                        self.name,
                    )
                )
                return
            if dst.is_symlink():
                print('[INFO] Unlinking old {}'.format(dst))
                dst.unlink()
            dst.parent.mkdir(parents=True, exist_ok=True)
            print('[INFO] Linking {} -> {}'.format(dst, src))
            dst.symlink_to(src)
        print('[INFO] Installing programs...')
        for name, command in self.programs.items():
            print('[INFO] Installing {}'.format(name))
            try:
                subprocess.run(command, shell=True, check=True)
            except subprocess.CalledProcessError:
                print(
                    '[{}ERRO{}] Cannot install program: {}'.format(
                        ANSI_ERROR,
                        ANSI_CLEAR,
                        name,
                    )
                )
        print('[INFO] Module: {} installed!'.format(self.name))
