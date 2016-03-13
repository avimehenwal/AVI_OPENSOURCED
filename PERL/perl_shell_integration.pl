#!/usr/bin/perl
# 
# AUTHOR      avimehenwal
# DATE        Wed Sep  2 12:24:52 IST 2015
# PURPOSE     Perl shell integration
#
#

# 1. Backticks
my $out, $str;
$out = `ls -la`;
print $out;

# 2. qx operator
$str = qx{ls -al};
print $str;

# 3. fetching error
$out = qx(ls -l 2>&1);
print $out;

# 4. Writing to file
open(my $fh, ">", "output.txt")
  or die "cannot open > output.txt : $!";
  print $fh $out;
close($fh) || warn "closed file: $!"; 
