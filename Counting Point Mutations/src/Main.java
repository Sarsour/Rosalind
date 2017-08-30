import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class Main {

	public static void main(String[] args) throws IOException {
		
		ArrayList <String> sequencesList = new ArrayList <String> (); //List of the two sequences
		
		//Read in file with the two DNA strings
		BufferedReader br = new BufferedReader(new FileReader("rosalind_hamm.txt"));
		String line;
		
		while ((line = br.readLine()) != null) {
			sequencesList.add(line);
		}
		
		//Compare every nucleotide in both sequences to find any point mutations
		int pointMutCount = 0;
		for (int i = 0; i < sequencesList.get(0).length(); i++) {
			if (!(sequencesList.get(0).charAt(i) == (sequencesList.get(1).charAt(i)))) {
				pointMutCount++;
			}
		}
		
		System.out.println(pointMutCount);
	}

}
