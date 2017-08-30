import java.util.ArrayList;
import java.util.Collections;

public class CalculatingGCContent {
	
	public ArrayList<String> idList = new ArrayList<String>();	//List of sequence IDs from text file
	public ArrayList<String> sequenceLineList = new ArrayList<String>();	//All lines of text fine which are sequence parts
	public ArrayList<Integer> countList = new ArrayList<Integer>();	//Number of lines of each sequence
	public ArrayList<String> combinedSequenceLineList = new ArrayList<String>();	//Combined sequence parts to create a full sequence.  Thus, each index is a full sequence
	public ArrayList<Integer> gcCountList = new ArrayList<Integer>();	//GC count of each sequence
	public ArrayList<Double> gcPercentagesList = new ArrayList<Double>();	//GC percentage of each sequence

	public CalculatingGCContent(ArrayList<String> idList, ArrayList<String> sequenceLineList, ArrayList<Integer> countList) {
		this.idList = idList;
		this.sequenceLineList = sequenceLineList;
		this.countList = countList;
		
		combineSequenceParts();
	}
	
	//Combine each sequence parts to create full sequences
	public void combineSequenceParts() {
		String combinedSequence = "";
		int count2 = 0;
		
		for(int i = 0; i < countList.size(); i++) {
			for (int j = 0; j < countList.get(i); j++) {
				combinedSequence = combinedSequence + sequenceLineList.get(count2);
				count2++;
			}
			combinedSequenceLineList.add(combinedSequence);
			combinedSequence = "";
		}
		
		countGCs();
	}
	
	//Count number of G's and C's per sequence
	public void countGCs() {
		
		for(int i = 0; i < combinedSequenceLineList.size(); i++) {
			int gcCount = 0;
			
			for(int j = 0; j < combinedSequenceLineList.get(i).length(); j++) {
				if (combinedSequenceLineList.get(i).charAt(j) == 'G' || combinedSequenceLineList.get(i).charAt(j) == 'C') {
					gcCount++;
				}
			}
			gcCountList.add(gcCount);
		}
		
		findGCPercentages();
	}
	
	//Fine GC percent of each sequence
	public void findGCPercentages() {
		
		for(int i = 0; i < combinedSequenceLineList.size(); i++) {
			gcPercentagesList.add(((double)gcCountList.get(i) / (double)combinedSequenceLineList.get(i).length()) * 100);
		}
		
		findHighestGCContent();
	}
	
	//Find sequence with highest GC content and print to screen in appropriate format
	public void findHighestGCContent() {
		double maxPercentage = Integer.MIN_VALUE;
		int maxPos = -1;
		
		for (int i = 0; i < gcPercentagesList.size(); i++) {
		    double value = gcPercentagesList.get(i);
		    if (value > maxPercentage) {
		    	maxPercentage = value;
		        maxPos = i;
		    }   
		}

		System.out.println(idList.get(maxPos));
		System.out.println(gcPercentagesList.get(maxPos));	
	}
	
	
}
