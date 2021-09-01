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
    'i3': 'sudo pacman -S --needed i3 bind',
    'Xorg': 'sudo pacman -S --needed xorg-server xorg-xinit',
    'acpi': 'sudo pacman -S --needed acpi',
    'alsamixer': 'sudo pacman -S --needed alsa-utils',
    'dunst': 'sudo pacman -S --needed dunst',
    'feh': 'sudo pacman -S --needed feh',
    'i3lock-fancy': 'yay -S i3lock-color-git i3lock-fancy-git',
    'mpd': 'sudo pacman -S --needed mpd',
    'picom': 'yay -S picom-ibhagwan-git',
    'polybar': 'yay -S polybar',
    'pulseaudio': 'sudo pacman -S --needed pulseaudio-alsa',
    'rofi': 'sudo pacman -S --needed rofi',
    'scrot': 'sudo pacman -S --needed scrot',
    'urxvt': 'sudo pacman -S --needed rxvt-unicode',
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
