#!/usr/bin/perl -w

use strict;

my $file_path;
my $home_dir = $ENV{"HOME"};
print "home_dir = $home_dir\n";
my $file_name = "/avimehenwal";
print "file_name = $file_name\n";

# String concationation
$file_path = $home_dir . $file_name;
print "concationation with .     \t $file_path\n";

$file_path = "${home_dir}${file_name}";
print "concationation with \$\{\}  \t $file_path\n";

$file_path = "$home_dir$file_name";
print "concationation with \$    \t $file_path\n";

$file_path = join($home_dir, $file_name);
print "concationation with join\t $file_path\n";

$home_dir .= $file_name;
print "concationation with \.\=     \t $home_dir";


