import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class Main {

	public static void main(String[] args) throws IOException {
		
		String dataSet = null;
		char nucleotide;
		
		//Read in file with nucleotide sequence
		BufferedReader br = new BufferedReader(new FileReader("rosalind_rna.txt"));
		String line;
		
		while((line = br.readLine()) != null) {
			dataSet = line;
		}
		
		//Print out data set
		System.out.println(dataSet);
		
		//Replace T nucleotides with U nucleotides and print new sequence to screen
		for(int i = 0; i < dataSet.length(); i++) {
			nucleotide = dataSet.charAt(i);
			
			if (nucleotide == 'T') {
				System.out.print('U');
			}
			
			else {
				System.out.print(nucleotide);
			}
		}

	}

}
