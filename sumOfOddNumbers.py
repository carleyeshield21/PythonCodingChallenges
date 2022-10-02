class SumOfOddNumbers:

    def __init__(self, n):
        self.n = n

    def printvalue(self):
        print(f'n = {self.n}')
        self.num = ((self.n)*(self.n))+(self.n-1)
        print(f'the last odd number in this sequence is {self.num}')

    def oddCount(self):
        arr = []
        for i in range(1, self.num+2, 2):
            # print(i)
            arr.append(i)
        # print(arr)
        # print(len(arr))
        arr_reverse = arr[::-1]
        # print(arr_reverse)
        new_arr = arr_reverse[0:self.n]
        # print(new_arr)

        sum = 0
        for i in range(0, len(new_arr)):
            # print(i)
            sum += new_arr[i]
        print(f'{new_arr} = {sum}')

# created number relationships to make calculations easier
# 1 / 1 / (1*1)+0 = 1
# 2 / 3+5 /(2*2)+1 = 5
# 3 / 7+9+11 / (3*3)+2 = 11
# 4 / 13+15+17+19 / (4*4)+3 = 19
# 5 / 21+23+25+27+29 / (5*5)+4 = 29
# 6 / 31+33+35+37+39+41 / (6*6)+5 = 41
# 7 / 43+45+47+49+51+53+55 / (7*7)+6 = 55
# 8 / 57+59+61+63+65+67+69+71 / (8*8)+7 = 71