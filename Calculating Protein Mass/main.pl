
#Read in mass table and store in array
my $MonoisotopicMassTable = 'MonoisotopicMassTable.txt';

open(my $fh, '<:encoding(UTF-8)', $MonoisotopicMassTable)
  or die "Could not open file '$MonoisotopicMassTable' $!";
 
chomp(my @massArray = <$fh>);
close $fh;

#split mass table into amino acids and masses
my $count = 0;
my @aminoAcids;
my @masses;

foreach (@massArray) {
	my @seperated = split("   ", $_);
	push @aminoAcids, $seperated[0];
	push @masses, $seperated[1];
}

#Read in sequence
my $inputFile = 'rosalind_prtm.txt';
my $sequence;

open(my $fh2, '<:encoding(UTF-8)', $inputFile)
  or die "Could not open file '$inputFile' $!";

 while (my $row = <$fh2>) {
  chomp $row;
  $sequence = $row;
}
close $fh2;

#Split sequence into the amino acid components
my @sequenceAminoAcids = split("", $sequence);

#Find the mass for each amino acid and add them together to find the total mass
my $saaSize = scalar @sequenceAminoAcids;
my $aaSize = scalar @aminoAcids;
my $mSize = scalar @masses;
my $totalMass = 0;

for (my $i=0; $i <= $saaSize; $i++) {
   for (my $j=0; $j <= $aaSize; $j++) {
		if (@sequenceAminoAcids[$i] eq @aminoAcids[$j]) {
			$totalMass = $totalMass + $masses[$j];
		}
	}
}
print $totalMass;