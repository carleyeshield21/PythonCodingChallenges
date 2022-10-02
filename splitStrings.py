# This is the link to this Python Code Challenge
# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/python
def solution(s):
    length = len(s)
    arr = []
    for index in range(0,length,2):
        arr.append(s[index:index+2])
    
    if len(arr[len(arr)-1]) < 2:
        arr[len(arr) - 1] = arr[len(arr)-1]+'_'
        print(arr)
    else:
        print(arr)
solution('abcdefgh')
print('========')
solution('abcdefg')