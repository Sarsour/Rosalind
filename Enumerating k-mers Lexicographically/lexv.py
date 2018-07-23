import itertools


def main():
	
	content = ''
	with open('rosalind_lexv.txt') as f:
		content = f.readlines()
	
	f.close()
	
	length = content[1]
	print(length)
	
	letters_list = content[0].split()	
	print(letters_list)
	main_word = ''.join(str(e) for e in letters_list)
	
	words_4long = [''.join(i) for i in itertools.product(letters_list, repeat = 4)]
	words_3long = [''.join(i) for i in itertools.product(letters_list, repeat = 3)]
	words_2long = [''.join(i) for i in itertools.product(letters_list, repeat = 2)]
	words_1long = [''.join(i) for i in itertools.product(letters_list, repeat = 1)]
	main_list = words_3long + words_2long + words_1long + words_4long
	
	main_list = sorted(main_list, key=lambda word: [main_word.index(c) for c in word])
		
	for x in main_list:
		print(x)
	
	
	output_file = open('output.txt', 'w')
	for word in main_list:
		output_file.write("%s\n" % word)
	
	
	
if __name__ == "__main__":
		main()