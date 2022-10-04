# https://www.codewars.com/kata/5ba58763924c945f950000a5/train/python
str_input = True
arr = ['']
while str_input:
    # input_string = arr.append(input('Type any string or endstr to end\n'))
    input_string = input('Type any string or "endstr" to end\n')
    if input_string != 'endstr':
        counter = 0
        for n in range(len(arr)):
            # print(arr[n], input_string)
            # print(arr[n] == input_string)
            if arr[n] != input_string:
                counter += 1
                if counter == len(arr):
                    arr.append(input_string)
        # print(f'counter = {counter}')
        print(arr)
    else:
        str_input = False
print(arr)
