#!/usr/bin/env bash

# AUTHOR	AVI MEHENWAL
# DATE		21-MARCH-14
# PURPOSE	Demostrate Special Shell Arguments

echo "Command	Description				Output"
echo "\$\$	Process ID of shell			$$"
echo "\$0	FileName of Currentshell		$0"
echo "\$1	CommandLine Positional(n) Arguments	$1"
echo "\$#	Number of Arguments supplied to shell	$#"
echo "\$*	All CommandLine Arguments String	$*"
echo "\$@	All CommandLine Arguments Array		$@"
echo "\$?	Exit STatus of last executed command	$?"
echo "\$!	Proccess no of Last Executed command 	$!"
echo "\$_	Current Value in Pipe		 	$_"
