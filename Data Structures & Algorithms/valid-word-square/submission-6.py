class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        setbro = []
        sethoe = []
        dongdong = ""
        count = 0
        for index, row in enumerate(words):
            setbro.append(row)
            for x in range(len(row)):
                try:
                    dongdong += words[x][index]
                    print(dongdong)
                except IndexError:
                    break
            sethoe.append(dongdong)
            dongdong = ""
        return setbro == sethoe

