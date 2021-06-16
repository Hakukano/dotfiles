Table of Contents
=================

   * [Arch](#arch)
      * [Example](#example)
      * [Post-installation](#post-installation)
      * [Awesome](#awesome)
   * [Installation](#installation)
   * [Must-have list](#must-have-list)
      * [git](#git)
      * [zsh](#zsh)
      * [npm](#npm)
      * [nvim](#nvim)
   * [Optional list](#optional-list)
      * [amethyst](#amethyst)
      * [firefox](#firefox)
      * [htop](#htop)
      * [ibus](#ibus)
      * [tldr](#tldr)
      * [tmux](#tmux)
      * [tree](#tree)
      * [xclip](#xclip)
   * [Outline VPN Config](#outline-vpn-config)

# Arch

Follow the Installation guide on https://wiki.archlinux.org/index.php/Installation_guide

## Example

### Check EFI or not

```
ls /sys/firmware/efi/efivars
```

### Update cystem clock

```
timedatectl set-ntp true
```

### Partition disk

```
fdisk /dev/sda
```

* EFI + GPT
```
g
n
1
<enter>
+512M
t
uefi
n
2
<enter>
+1G
t
2
swap
n
3
<enter>
<enter>
t
3
linux
w
mkfs.fat -F32 /dev/sda1
mkfs.ext4 /dev/sda3
mkswap /dev/sda2
mount /dev/sda3 /mnt
mkdir /mnt/boot
mount /dev/sda1 /mnt/boot
swapon /dev/sda2
```

* BIOS + MBR
```
o
n
p
1
<enter>
+1G
t
swap
n
p
2
<enter>
<enter>
t
2
linux
w
mkfs.ext4 /dev/sda2
mkswap /dev/sda1
mount /dev/sda2 /mnt
swapon /dev/sda1
```

### Pacstrap

```sh
pacstrap /mnt base linux linux-firmware vim net-tools netctl sudo grub
```

### Config system

```
genfstab -U /mnt >> /mnt/etc/fstab
arch-chroot /mnt
ln -sf /usr/share/zoneinfo/Americas/Toronto /etc/localtime
hwclock --systohc
# Edit /etc/locale.gen and uncomment en_US.UTF-8 UTF-8 and other needed locales
locale-gen
echo 'LANG=en_US.UTF-8' > /etc/locale.conf
echo ${myhostname} > /etc/hostname
echo -e "127.0.0.1	localhost\n::1		localhost\n127.0.1.1	${myhostname}.localdomain	${myhostname}"
passwd
```

### Bootloader

* EFI + GPT

```
pacman -S efibootmgr
grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB
```

* BIOS + MBR

```
grub-install --target=i386-pc /dev/sda
```

### Microcode

```
pacman -S intel-ucode
grub-mkconfig -o /boot/grub/grub.cfg
```

Check if the microcode is generated

```
grep 'intel-ucode' /boot/grub/grub.cfg
```

### Finishing

```
exit
umount -R /mnt
reboot
```

## Post-installation

### After guide su

```sh
echo -e "Interface=XXX\nConnection=ethernet\nIP=static\nAddress=('XXX.XXX.XXX.XXX/XX')\nGateway='XXX.XXX.XXX.XXX'\nDNS=('XXX.XXX.XXX.XXX')" > /etc/netctl/ethernet_static
chmod +r /etc/netctl/ethernet_static
netctl start ethernet_static
netctl enable ethernet_static
groupadd sudo
useradd -m XXX
passwd XXX
usermod -aG sudo XXX
visudo
uncomment %sudo & append XXX ALL=(ALL) NOPASSWD:ALL
exit
```

### In user space

``` sh
sudo pacman -Syu
sudo pacman -S --needed base-devel git
mkdir ~/Git
cd ~/Git
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
sudo pacman -S openssh
ssh-keygen
sudo ssh-keygen -A
```

## Awesome

```
sudo pacman -S thunar kitty ncmpcpp gtk3 picom
yay -S awesome-git rofi lm_sensors acpid jq fortune-mod redshift mpd mpc maim feh light-git pulseaudio inotify-tools xdotool
systemctl --user enable mpd.service
systemctl --user start mpd.service
sudo systemctl enable acpid.service
sudo systemctl start acpid.service
fc-cache -v
```

# Installation

At least to have a ~/Git directory and all git repos go into it.

Run install.py in a clean environment, then install not-installed programs in the Must-have list below.

# Must-have list

## zsh

```sh
sudo pacman -S zsh
chsh -s /bin/zsh
```

## npm

```sh
sudo pacman -S nodejs npm
```

## nvim

```sh
yay -S neovim-git bear rust-analyzer-git
sudo pacman -S python python-pip python2 python2-pip the_silver_searcher clang cscope cmake jdk11-openjdk stack rustup texlive-core texlab zathura zathura-pdf-mupdf
pip3 install neovim cmake-language-server 'python-language-server[all]'
npm install -g typescript bash-language-server dockerfile-language-server-nodejs vscode-css-languageserver-bin vscode-html-languageserver-bin vscode-json-languageserver typescript-language-server vim-language-server yaml-language-server purescript-language-server purty
~/.fzf/install
source ~/.zshrc
```

# Optional list

## amethyst

```sh
sudo pacman -S grep gcc pkgconf openssl alsa-lib cmake make python3 freetype2 awk libxcb
```

## firefox

```sh
sudo pacman -S firefox
```

## htop

```sh
sudo pacman -S htop
```

## ibus

```sh
sudo pacman -S ibus ibus-rime
yay -S ibus-mozc
```

## tldr

```sh
sudo pacman -S tldr
```

## tmux

```sh
sudo pacman -S tmux xsel
cd ~/Git
git clone https://github.com/tmux-plugins/tpm
```

Ctrl-b I to install plugins

Ctrl-b U to update plugins

Ctrl-b alt-u to remove plugins

## tree

```sh
sudo pacman -S tree
```

## xclip

```sh
sudo pacman -S xclip
```

# Outline VPN Config

```sh
sudo wget -qO- https://raw.githubusercontent.com/Jigsaw-Code/outline-server/master/src/server_manager/install_scripts/install_server.sh | bash
```
