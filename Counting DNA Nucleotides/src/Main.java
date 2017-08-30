import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Main {

	public static void main(String[] args) throws IOException {
		
		String dataSet = null;	//Nucleotide sequence
		char nucleotide;	//Nucleotide in string
		int nucleotideA = 0;	//A nucleotide count
		int nucleotideC = 0;	//C nucleotide count
		int nucleotideG = 0;	//G nucleotide count
		int nucleotideT = 0;	//T nucleotide count
		
		//Read in file with nucleotide sequence
		BufferedReader br = new BufferedReader(new FileReader("rosalind_dna.txt"));
		String line;
		
		while((line = br.readLine()) != null) {
			dataSet = line;
		}
		
		//Print out data set
		System.out.println(dataSet);
		
		//Go through sequence and count nucleotides 
		for(int i = 0; i < dataSet.length(); i++) {
			nucleotide = dataSet.charAt(i);
			
			if (nucleotide == 'A') {
				nucleotideA++;
			}
			
			else if (nucleotide == 'C') {
				nucleotideC++;
			}
			
			else if (nucleotide == 'G') {
				nucleotideG++;
			}
			
			else if (nucleotide == 'T') {
				nucleotideT++;
			}
		}
		
		//Print out number of each nucleotide in proper format (format determined by Rosalind)
		System.out.println(nucleotideA + " " + nucleotideC + " " + nucleotideG + " " + nucleotideT);
		
	}

}
