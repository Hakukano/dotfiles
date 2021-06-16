#!/bin/python3

from __future__ import annotations

from pathlib import Path
from typing import Optional
import os

VERSION_FILE = Path('.dotfiles_version')
SRC_HOME = Path(__file__).parent.absolute().joinpath('home')
DST_HOME = Path.home()

CURRENT_VERSION_FILE = DST_HOME.joinpath(VERSION_FILE)


def get_current_version():
    if CURRENT_VERSION_FILE.is_file():
        return int(open(CURRENT_VERSION_FILE, mode='r').read())
    else:
        return -1


class Installation:
    def __init__(self, version: int, previous: Optional[Installation]):
        self.version = version
        self.previous_version = version - 1
        self.previous = previous

    def upgrade(self):
        pass

    def install_self(self):
        pass

    def install(self):
        current_version = get_current_version()
        if self.previous is not None and \
           current_version < self.previous_version:
            print('[INFO] Current version is less than {}, install {} first'.
                  format(self.previous_version, self.previous_version))
            self.previous.install()

        current_version = get_current_version()
        if current_version == self.previous_version:
            print('[INFO] Upgrading version from {} to {}'.
                  format(self.previous_version, self.version))
            self.upgrade()
            print('[INFO] Upgrading done')

        print('[INFO] Installing version {}'.format(self.version))
        self.install_self()
        open(CURRENT_VERSION_FILE, mode='w').write(str(self.version))
        print('[INFO] Version {} installed'.format(self.version))


class Installation0(Installation):
    def __init__(self):
        super().__init__(0, None)


class Installation1(Installation):
    def __init__(self):
        super().__init__(1, Installation0())

    def install_self(self):
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


print('[INFO] Start installing')
Installation1().install()
print('[INFO] All done!')
