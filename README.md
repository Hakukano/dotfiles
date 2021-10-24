Table of Contents
=================

   * [Arch](#arch)
      * [Example](#example)
      * [Post-installation](#post-installation)
   * [Installation](#installation)

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
echo -e "127.0.0.1	localhost\n::1		localhost\n127.0.1.1	${myhostname}.localdomain	${myhostname}" > /etc/hosts
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
sudo systemctl start sshd
sudo systemctl enable sshd
```

# Installation

1. Create ~/Git, clone this repo into it.

2. Install python3 and pip3

3. Run install.sh, follow the prompt to setup
