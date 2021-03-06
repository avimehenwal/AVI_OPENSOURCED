chmod Command Examples for Beginners


Following are the symbolic representation of three different roles:

 u is for user,
 g is for group,
 o is for others.

Following are the symbolic representation of three different permissions:

 r is for read permission,
 w is for write permission,
 x is for execute permission.


Following are few examples on how to use the symbolic representation on chmod.


 1. Add single permission to a file/directory

 Changing permission to a single set. + symbol means adding permission. For example, do the following to give execute permission for the user irrespective of anything else:

 $ chmod u+x filename


2. Add multiple permission to a file/directory

 Use comma to separate the multiple permission sets as shown below.

 $ chmod u+r,g+x filename


3. Remove permission from a file/directory

 Following example removes read and write permission for the user.

 $ chmod u-rx filename


4. Change permission for all roles on a file/directory

 Following example assigns execute privilege to user, group and others (basically anybody can execute this file).


  
  $ chmod a+x filename


5. Make permission for a file same as another file (using reference)

  If you want to change a file permission same as another file, use the reference option as shown below. In this example, file2′s permission will be set exactly same as file1′s permission.

  $ chmod --reference=file1 file2


6. Apply the permission to all the files under a directory recursively

  Use option -R to change the permission recursively as shown below.

  $ chmod -R 755 directory-name/


7. Change execute permission only on the directories (files are not affected)

  On a particular directory if you have multiple sub-directories and files, the following command will assign execute permission only to all the sub-directories in the current directory (not the files in the current directory).

  $ chmod u+X *
  Note: If the files has execute permission already for either the group or others, the above command will assign the execute permission to the user
