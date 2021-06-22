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
        'sudo pacman -S i3 bind noto-fonts && '
        'yay -S ttf-linux-libertine ttf-dejavu '
        'ttf-inconsolata ttf-ubuntu-font-family ',
    'Xorg': 'sudo pacman -S xorg-server xorg-xinit',
    'acpi': 'sudo pacman -S acpi',
    'alsamixer': 'sudo pacman -S alsa-utils',
    'dunst': 'sudo pacman -S dunst',
    'feh': 'sudo pacman -S feh',
    'i3lock-fancy': 'yay -S i3lock-color-git i3lock-fancy-git',
    'mpd': 'sudo pacman -S mpd',
    'picom': 'yay -S picom-ibhagwan-git',
    'polybar': 'yay -S polybar ttf-freefont ttf-ms-fonts',
    'pulseaudio': 'sudo pacman -S pulseaudio-alsa',
    'rofi': 'sudo pacman -S rofi noto-fonts-cjk noto-fonts-emoji',
    'scrot': 'sudo pacman -S scrot',
    'urxvt': 'sudo pacman -S rxvt-unicode ttf-hack',
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
