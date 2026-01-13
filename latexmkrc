use Config;

$pdflatex = 'xelatex -synctex=1 -file-line-error -interaction=nonstopmode -halt-on-error -shell-escape %O %S';

my $path_sep = $Config{path_sep} // ':';
$ENV{'TEXINPUTS'} = './packages//' . $path_sep . ($ENV{'TEXINPUTS'} // '');

# Set local time zone on Overleaf if needed
# List of supported timezones: https://www.php.net/manual/en/timezones.php
# $ENV{'TZ'}='Canada/Central';

$root = 'book.tex';

# Ensure glossaries/acronyms are built automatically
add_cus_dep('glo','gls',0,'makeglossaries');
add_cus_dep('acn','acr',0,'makeglossaries');

sub makeglossaries {
	my ($base) = @_;
	return system('makeglossaries', $base);
}
