Special Variables | Explaination 
--------------------|---------
$$ 				| Process ID of shell
$PPID			| Process ID of shell’s parent process.
$?			| Exit status of last command.
$_			| Name of last command.
$! 			| Process ID of last process run in the background using ampersand (&) operator. This is commonly used in conjunction with the wait builtin.
$PATH 		| A colon-delimited list of locations where trusted executables are installed. Any executable in one of these locations can be executed without specifying a complete path.
$IFS		| Input Field Separators (uses are explained in Variable Expansion and Field Separators)
$HOME		| The user’s home directory.
$UID		| The user’s ID.
$USER		| The user’s (short) login name.
$#		| Number of arguments passed to the shell. This variable is described further in Handling Flags and Arguments.
$@		| Complete list of arguments passed to the shell, separated by spaces.. This variable is described further in Handling Flags and Arguments.
$*		| Complete list of arguments passed to the shell, separated by the first character of the IFS (input field separators) variable. This variable is 

$-		| A list of all shell flags currently enabled.
$PWD	| The current working directory. Equivalent to executing the pwd command.


Quirk Warning:For subshells, the value of PPID is inherited from the parent shell. Thus, PPID is only the parent of the outermost shell process.


Security Warning:This value can be modified by the calling script, so it should not be used for authentication purposes.


Security Warning:This value can be modified by the calling script, so it should not be used for authentication purposes.

Miscellaneous Variables
