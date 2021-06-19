from module import Module

CONFIGS = [
    '.Xresources',
    '.config/dunst',
    '.config/i3',
    '.config/picom.conf',
    '.config/polybar',
    '.config/rofi',
    '.config/vis',
    '.dbus',
    '.local/share/fonts',
    '.wallpaper',
    '.xinitrc',
]

PROGRAMS = {
    'i3':
        'sudo pacman -S i3 xorg-server xorg-xinit '
        'bind noto-fonts-cjk noto-fonts-emoji noto-fonts '
        'feh alsa-utils scrot imagemagick util-linux '
        'ttf-hack pulseaudio mpd acpi && '
        'yay -S ttf-freefont ttf-ms-fonts ttf-linux-libertine '
        'ttf-dejavu ttf-inconsolata ttf-ubuntu-font-family '
        'i3lock-fancy-git i3lock-color-git',
    'urxvt': 'sudo pacman -S rxvt-unicode',
    'rofi': 'sudo pacman -S rofi',
    'dunst': 'sudo pacman -S dunst',
    'picom': 'yay -S picom-ibhagwan-git',
    'polybar': 'yay -S polybar',
}

DEPENDENCIES = [
]


class I3(Module):
    def __init__(self):
        super().__init__(
            'i3',
            'I3 setup, run fc-cache later!',
            CONFIGS,
            PROGRAMS,
            DEPENDENCIES,
        )
