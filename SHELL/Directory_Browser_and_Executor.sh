#!/usr/bin/env bash

# AUTHOR    : AVI MEHENWAL
# DATE      : 07th-JULY-2014
# PURPOSE   : Browsing Directories to run a command in all


cd ~
for dir in `ls -l | grep ^d | awk '{print $9}'`
do
        ( cd $dir
          echo $"***************************************        Now in directory [$dir] "
          f=$(ls -l | grep ^d | wc -l)
          echo "Total sub-directories in [$dir] = $f"
           )
done
