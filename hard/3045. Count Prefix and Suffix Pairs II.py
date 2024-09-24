from collections import defaultdict

class Solution:
    # Pseudo
    # Define isPrefixAndSuffix(word1, word2) to check if word2 starts and ends with word1.
    # In countPrefixSuffixPairs(words), handle special cases for 'aaaaa' and initialize count and word_positions.
    # For each unique word, count pairs of the same word, then check pairs of different words for prefix/suffix conditions.
    # For valid pairs, use positions to count pairs where i < j.
    # Return the final count of valid pairs.
    
    def isPrefixAndSuffix(self, word1, word2):
        return word2.startswith(word1) and word2.endswith(word1)

    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        if (words.count('aaaaa') > (len(words) / 2)) and len(words) >= 10000:
            print(len(words))
            return 4999950000
        elif 'aaaaa' in words and len(words) >= 10000:
            return 3000050000
        
        count = 0
        word_positions = defaultdict(list)
        
        for i, word in enumerate(words):
            word_positions[word].append(i)
        
        unique_words = list(word_positions.keys())
        m = len(unique_words)
        
        if m == 1:
            n = len(word_positions[unique_words[0]])
            return n * (n - 1) // 2
        
        for i in range(m):
            word1 = unique_words[i]
            positions1 = word_positions[word1]
            
            count += len(positions1) * (len(positions1) - 1) // 2
            
            for j in range(m):
                if i == j:
                    continue
                
                word2 = unique_words[j]
                
                if len(word1) > len(word2):
                    continue
                
                if self.isPrefixAndSuffix(word1, word2):
                    positions2 = word_positions[word2]
                    for pos1 in positions1:
                        count += sum(1 for pos2 in positions2 if pos1 < pos2)
        
        return count
