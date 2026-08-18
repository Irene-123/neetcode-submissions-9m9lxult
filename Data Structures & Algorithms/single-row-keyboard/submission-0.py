class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        keymap = {}
        head = 0
        ans = 0

        for index, key in enumerate(keyboard):
            keymap[key] = index

        for w in word:
            ans += abs(keymap[w] - head)
            head = keymap[w]
        return ans