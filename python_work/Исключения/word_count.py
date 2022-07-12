def count_words(filename):
    '''Подсчет приблизительного количества строк в файле.'''
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        # Подсчет приблизительного количества слов в файле
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filename = 'txt_files/alice.txt'
count_words(filename)

filenames = ['txt_files/alice.txt', 'txt_files/mobi_dick.txt', 'txt_files/sidhart.txt', 'txt_files/little_woman.txt']

for filename in filenames:
    count_words(filename)

