class WordsFinder:
    def __init__(self, *file_names: list):
        self.file_names = file_names
        
    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding ='utf-8') as file:
                words = []
                words = file.read().lower().replace(',', '').replace('.', '').replace('=', '').replace('!', '').replace('?',
                                                                                                            '').replace(
                        ';', '').replace(':', '').replace(' - ', ' ').split()
                all_words[file_name] = words
            return all_words

    def find(self, word):
        word_positions = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            if word.lower() in words:
                word_positions[file_name] = words.index(word)
        return word_positions

    def count(self, word):
        word_counts = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            if word.lower() in words:
                word_counts[file_name] = words.count(word)
        return word_counts

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
