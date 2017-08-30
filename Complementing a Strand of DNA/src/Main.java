import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Main {

	public static void main(String[] args) throws IOException {
		
		String dataSet = null;
		char nucleotide;
		
		//Read in file with nucleotide sequence
		BufferedReader br = new BufferedReader(new FileReader("rosalind_revc.txt"));
		String line;
		
		while((line = br.readLine()) != null) {
			dataSet = line;
		}
		
		//Print out data set
		System.out.println(dataSet);
		
		//Find reverse complementary sequence and print to screen
		for(int i = dataSet.length(); i > 0; i--) {
			nucleotide = dataSet.charAt(i-1);
			
			if (nucleotide == 'A') {
				System.out.print('T');
			}
			
			else if (nucleotide == 'T') {
				System.out.print('A');
			}
			
			else if (nucleotide == 'C') {
				System.out.print('G');
			}
			
			else if (nucleotide == 'G') {
				System.out.print('C');
			}
		}

	}

}
