#!/usr/bin/env bash
# oppor9m
# adb -s SCJFEY4LTGPBZLCI shell input text ym12345
# adb -s SCJFEY4LTGPBZLCI shell input tap 760 730

# oppoR15X
# adb -s 47f1c6e1 shell input text ym123456
# adb -s 47f1c6e1 shell input tap 700 950

for ((i=1;i<=100;i++))
do
adb shell input tap 825 1350
sleep 0.7
done
