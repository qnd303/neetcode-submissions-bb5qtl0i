class Solution:
    def confusingNumber(self, n: int) -> bool:
        bruh = str(n)
        grah = str("")
        for s in reversed(bruh):
            if s == "6":
                grah += ("9")
            elif s == "9":
                grah += "6"
            else:
                grah += s
            if s == "3":
                return False
            if s == "2":
                return False
            if s == "4":
                return False
            if s == "5":
                return False
            if s == "7":
                return False
        return grah != bruh