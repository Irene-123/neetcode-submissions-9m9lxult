class Solution:

    def findNum(self, s, i):
        j = i + 2
        numFound = False

        while j < j + 4:
            if s[j].isnumeric():
                j += 1
            else:
                break

        if j > i + 2:
            numFound = True
        return j, numFound

    def encode(self, strs: List[str]) -> str:
        
        n = len(strs)
        encoded = str(n)
        for s in strs:
            encoded += ("/#" + str(len(s)) + "/" + s)
        return encoded

    def decode(self, s: str) -> List[str]:
        n = len(s)
        decoded = []
        i, j = 0, 0
        # /#5/Hello/#5/World
        while i < n:
            if s[i: i+2] == '/#': # Probably our split breaker
                j, numFound = self.findNum(s, i)
                print("j: ", j)
                if not numFound:
                    continue
                else:
                    num = int(s[i+2 : j])
                    print(num)
                    if s[j] == '/':
                        decoded.append(s[j+1: j + 1 + num])
                        i = j + 1 + num
            else:
                i += 1
        
        return decoded

                    

        

