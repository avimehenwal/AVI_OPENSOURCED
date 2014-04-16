#!/usr/bin/env bash


# DATE		:	16-April-2014
# AUTHOR	:	AVI MEHENWAL
# PURPOSE	:	counts the items in cwd and returns individual count of files, directories and symlinks
p=`pwd`
echo "For directory Path [$p]"

f=$(ls -l | grep ^- | wc -l)
d=$(ls -l | grep ^d | wc -l)
s=$(ls -l | grep ^l | wc -l)

echo "Total Directories = $d"
echo "Total Symlinks = $l"
echo "Total Files = $f"

