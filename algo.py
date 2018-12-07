class needleman:

    mismatch = -1
    match = 1
    gap = -1

    def __init__(self, str1, str2):
        str1 = " " + str1
        str2 = " " + str2
        self.arr = []
        self.initArr(str1, str2)

    def initArr(self, str1, str2):
        self.arr.append([0])
        for i, ch1 in enumerate(str1):

            if i > 0:
                self.arr.append([])

            for j, ch2 in enumerate(str2):

                #where the array is defined
                if i == 0 and j == 0 :
                    continue

                if i == 0 and j > 0:
                    self.arr[i].append(self.arr[i][j-1] + self.gap)

                if j == 0 and i > 0:
                    self.arr[i].append(self.arr[i-1][j] + self.gap)

                if j > 0 and i > 0:
                    match_ = self.arr[i-1][j-1] + self.match if ch1 == ch2 else self.arr[i-1][j-1] + self.mismatch
                    g1 = self.arr[i-1][j] + self.gap
                    g2 = self.arr[i][j-1] + self.gap
                    max = 0
                    
                    if match_ > g1:
                        if match_ > g2:
                            max = match_
                        else:
                            max = g2

                    elif g1 > g2:
                        max = g1

                    else:
                        max = g2

                    self.arr[i].append(max)
                #=========================

        print(self.arr[len(self.arr) - 1][len(self.arr[len(self.arr) - 1]) - 1])


if __name__ == "__main__":
    str1 = raw_input()
    str2 = raw_input()
    nmw = needleman(str1, str2)