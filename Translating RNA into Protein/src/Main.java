import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class Main {

	public static void main(String[] args) throws IOException {
		
		ArrayList <String> rnaTrinucleotideList = new ArrayList <String>();	//List of possible trinucleotide combinations
		ArrayList <String> aminoAcidList = new ArrayList <String>();	//List of possible amino acids (corresponding to rnaTrinucleotideList)
		
		//Read in RNA codon table
		BufferedReader br = new BufferedReader(new FileReader("RNACodonTable.txt"));
		String line;
		
		while ((line = br.readLine()) != null) {
			String[] parts = line.split(" ");
			rnaTrinucleotideList.add(parts[0]);
			aminoAcidList.add(parts[1]);
		}
		br.close();
		
		//Read in sequence and compare every 3 nucleotides with the rnaTrinucleotideList to find the amino acid form the aminoAcidList
		BufferedReader br2 = new BufferedReader(new FileReader("rosalind_prot.txt"));
		String line2;
		
		while ((line2 = br2.readLine()) != null) {
			for (int i = 0; i < line2.length(); i+=3) {
				for (int j = 0; j < rnaTrinucleotideList.size(); j++) {
					if (rnaTrinucleotideList.get(j).equals(line2.substring(i, i+3))) {
						if (!(aminoAcidList.get(j).equals("Stop"))) {	//Do not include stop codons
							System.out.print(aminoAcidList.get(j));
						}
					}
				}
			}
		}
		br2.close();
		
		
	}

}
