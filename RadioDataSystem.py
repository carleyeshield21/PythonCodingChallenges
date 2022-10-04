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
del arr[0]
print(arr)
print(' '.join(arr))

# Here set an array or list and has a single space as the initial value. The purpose of this is to have a basis
# when we are trying to make a comparison in the if statement "if arr[n] != input_string:". We increment the counter
# by one on every iteration if it detects a False, then we compare the counter to the length of the list "arr",
# if it equals the length of arr, then that is the time we append the 'input_string' meaning in the given arr/list,
# it currently has no same value of string as the 'input_string. All of these are inside a while statement,
# setting first the value of str_input to True, and making it to False if the user inputs endstr to stop and output
# the final string
