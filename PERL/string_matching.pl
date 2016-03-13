#!/usr/bin/perl -w
#
# AUTHOR   = avimehenwal
# DATE     = Mon Aug 31 16:09:41 IST 2015
# PURPOSE  = Demo perl string concationation
#


use strict;

my $sentence;
$sentence = "The quick brown fox.";

# RegEx is case-sensitive
if ($sentence =~ /the/) {
    print "\/the\/ true in $sentence\n";
}
else {
    print "\/the\/ false in $sentence\n";
}

# non-match RegEx
print $sentence !~ /the/


