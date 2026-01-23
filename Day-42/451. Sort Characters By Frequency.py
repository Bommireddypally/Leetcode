class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        return ''.join(char * freq for char, freq in Counter(s).most_common())
