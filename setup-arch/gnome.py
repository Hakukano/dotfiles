from module import Module
from pathlib import Path

CONFIGS = [
    '.Xresources',
    '.local/share/fonts',
    '.profile',
    '.wallpaper',
]

PROGRAMS = {
    'gnome-shell': 'sudo pacman -S --needed gnome noto-fonts-cjk',
    'gnome-tweaks': 'sudo pacman -S --needed gnome-tweaks',
    'dconf-editor': 'sudo pacman -S --needed dconf-editor',
    'urxvt': 'sudo pacman -S --needed rxvt-unicode',
}

DEPENDENCIES = [
]

DCONF = Path(__file__).parent.parent.absolute().joinpath('gnome.dconf')


class Gnome(Module):
    def __init__(self):
        super().__init__(
            'gnome',
            'Gnome Desktop Manager',
            CONFIGS,
            PROGRAMS,
            DEPENDENCIES,
        )

    def install(self):
        super().install()
        print('[INFO] Loading dconf')
        try:
            subprocess.run(
                'dconf load / < {}'.format(DCONF),
                shell=True,
                check=True,
            )
            print('[INFO] Done!')
        except subprocess.CalledProcessError:
            print(
                '[{}ERRO{}] Cannot load dconf'.format(
                    ANSI_ERROR,
                    ANSI_CLEAR,
                )
            )
