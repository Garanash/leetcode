class Solution:
    def kthCharacter(self, k: int) -> str:
        def add_new_chars(wrd):
            new_chars = ''
            for elem in wrd:
                ov = ord(elem) if ord(elem) < 122 else 96
                new_chars += chr(ov + 1)
            return new_chars
        word = 'a'
        while len(word) < k:
            word += add_new_chars(word)
        return word[k-1]