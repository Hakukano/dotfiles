#!/bin/python3

from pathlib import Path
import os

VERSION_FILE = Path('VERSION')
SRC_HOME = Path(__file__).parent.absolute().joinpath('home')
DST_HOME = Path.home()

CURRENT_VERSION_FILE = DST_HOME.joinpath(VERSION_FILE)
CURRENT_VERSION = -1
if os.path.isfile(CURRENT_VERSION_FILE):
    CURRENT_VERSION = int(open(CURRENT_VERSION_FILE, mode='r').read())


def install_0():
    print('[INFO] Installing version 0')
    open(CURRENT_VERSION_FILE, 'w').write('0')
    print('[INFO] Version 0 installed')


def install_1():
    if CURRENT_VERSION < 0:
        print('[INFO] Version 0 not found, Install it first')
        install_0()

    print('[INFO] Installing version 1')

    files = [
        '.config/dunst',
        '.config/i3',
        '.config/nvim',
        '.config/polybar',
        '.config/rofi',
        '.config/vis',
        '.config/zathura',
        '.config/picom.conf',
        '.dbus',
        '.local/share/fonts',
        '.scripts',
        '.vim',
        '.wallpaper',
        '.zsh_completion',
        '.latexmkrc',
        '.p10k.zsh',
        '.tmux.conf',
        '.xinitrc',
        '.Xresources',
        '.zgen-setup',
        '.zsh_aliases',
        '.zsh_functions',
        '.zshrc',
    ]

    for file in files:
        dst = DST_HOME.joinpath(file)
        if dst.exists() and (not dst.is_symlink()):
            print('[ERRO] {} is not a symlink'.format(dst))
            exit(1)

    for file in files:
        src = SRC_HOME.joinpath(file)
        dst = DST_HOME.joinpath(file)
        if dst.is_symlink():
            print('[INFO] Removing existing link: {}'.format(dst))
            dst.unlink()
        dst.parent.mkdir(parents=True, exist_ok=True)
        print('[INFO] Creating link: {} -> {}'.format(dst, src))
        os.symlink(src, dst)

    open(CURRENT_VERSION_FILE, 'w').write('1')
    print('[INFO] Version 1 installed')


print('[INFO] Start installing')
install_1()
print('[INFO] All done!')
