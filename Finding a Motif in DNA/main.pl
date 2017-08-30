use strict;
use warnings;

#Read in sequence
my $inputFile = 'rosalind_subs.txt';
my @sequences;

open(my $fh, '<:encoding(UTF-8)', $inputFile)
  or die "Could not open file '$inputFile' $!";

chomp(@sequences = <$fh>);
close $fh;

#Set variables of sequence, subsequence, and index
my $sequence = $sequences[0];
my $subSequence = $sequences[1];
my $offset = 0;

#Find all indexes of subsequence in sequence in order to find the motifs
my $result = index($sequence, $subSequence, $offset);

while ($result != -1) {
		
    print ($result+1);
	print " ";

    $offset = $result + 1;
    $result = index($sequence, $subSequence, $offset);
}