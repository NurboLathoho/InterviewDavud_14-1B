import re
def count_word(word1):
    words = re.findall(r'\b\w+\b', word1.lower())
    
    word_counts = {}
    
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
        
    return word_counts

word1 = "Money, money, money, it’s always sunny, in the richmen’s world"
result = count_word(word1)
print(result)
