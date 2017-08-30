import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class Main {

	public static void main(String[] args) throws IOException {
		
		ArrayList<String> idList = new ArrayList<String>();	//List of sequence IDs
		ArrayList<String> sequenceLineList = new ArrayList<String>();	//All lines of text fine which are sequence parts
		ArrayList<Integer> countList = new ArrayList<Integer>();	//Number of lines of each sequence
		
		//Read in file with nucleotide sequence which is in fasta format
		BufferedReader br = new BufferedReader(new FileReader("rosalind_gc.txt"));
		String line;
		
		int count = 0;
		
		while((line = br.readLine()) != null) {
			
			if (line.startsWith(">")) {
				countList.add(count);
				count = 0;
				String[] parts = line.split(">");
				idList.add(parts[1]);
			}
			
			else {
				sequenceLineList.add(line);
				count++;
			}
		}
		countList.add(count);
		
		//Call CalculatingGCContent Class
		CalculatingGCContent calc = new CalculatingGCContent(idList, sequenceLineList, countList);

	}
}