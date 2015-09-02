#!/usr/bin/perl
# 
# AUTHOR        = avimehenwal
# DATE          = Wed Sep  2 12:24:52 IST 2015
# PURPOSE       = Perl shell integration
 

# backticks
my $out, $str;
$out = `ls -la`;
print $out;

# qx operator
$str = qx{ls -al};
print $str;

# fetching error
$out = qx(ls -l 2>&1);
print $out;

# writing to file
open(my $fh, ">", "output.txt")
  or die "cannot open > output.txt : $!";
  print $fh $out;
close($fh) || warn "closed file: $!"; 
