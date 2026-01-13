$pdflatex = 'xelatex -synctex=1 -file-line-error -interaction=nonstopmode -halt-on-error -shell-escape %O %S';

$ENV{'TEXINPUTS'} = './packages//:' . ($ENV{'TEXINPUTS'} // '');

# Set local time zone on Overleaf if needed
# List of supported timezones: https://www.php.net/manual/en/timezones.php
# $ENV{'TZ'}='Canada/Central';

$root = 'book.tex';