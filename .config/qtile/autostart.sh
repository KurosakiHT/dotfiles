#!/bin/bash
ibus-daemon -drx &
picom &
xfce4-power-manager &
xcalib ~/.themes/Nitro5_03.icm &
lxpolkit &
nm-applet &
light-locker &
parcellite &
aria2c --enable-rpc --rpc-listen-all=true --rpc-allow-origin-all &
