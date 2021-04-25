#!/bin/bash
for i in $(ls -a)
do
    rm -rfv $i
done
cp -rT /etc/skel/ ~/
