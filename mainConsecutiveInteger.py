class MainConseeutive:

    def __init__(self, n = int(input('Type any integer\n'))):
        self.n = n

    def int_output(self):
        print(self.n)
        # n = 10
        j = 1
        while j <= self.n:
            arr = []
            for k in range(j):
                # print(k+1)
                arr.append(k + 1)
            j += 1
            print(arr)

# Exercise Output
        # 1 / 1
        # 2 / 1 / 1,2
        # 3 / 1 / 1, 2 / 1,2,3