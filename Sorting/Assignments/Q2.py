# https://leetcode.com/problems/sorting-the-sentence/
# SORT THE SENTENCE


class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        lis = s.split(" ")
        # lis.sort(key=lambda x: int(x[-1]))
        #Cyclic sort
        i = 0
        while i < len(lis):
            correct_idx = int(lis[i][-1]) - 1
            if lis[i] != lis[correct_idx]:
                lis[i], lis[correct_idx] = lis[correct_idx], lis[i]
            else:
                i += 1
        
        # Removing numbers from the words manually
        lis_without_num = [''.join([char for char in word if not char.isdigit()]) for word in lis]
        
        
        sorted_sentence = ' '.join(lis_without_num)
        
        return sorted_sentence
