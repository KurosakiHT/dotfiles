#!/bin/bash
fcitx5 &
picom &
xcalib ~/.themes/Asus_X456UAK.icm &
lxpolkit &
nm-applet &
light-locker &
parcellite &
aria2c --enable-rpc --rpc-listen-all=true --rpc-allow-origin-all &
