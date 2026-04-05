class Solution:
    def confusingNumber(self, n: int) -> bool:
        invert = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        k = str(n)
        bruh = []

        for ch in k:
            if ch not in invert:
                return False
        
        k = reversed(k)
        for ch in k:
            bruh.append(invert[ch])
        return "".join(bruh) != str(n)
