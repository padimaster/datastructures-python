# A string is given. We have to print the reversed string.
# For example, the string is "Hi how are you?"
# The output should be "?ouy era woh iH"

def swap(string, a, b): #Function which swaps two characters of a string
    string = list(string)
    temp = string[a]
    string[a] = string[b]
    string[b] = temp
    return ''.join(string)

def smarter_reverse(string):
    for i in range(len(string)//2):
        string = swap(string, i, len(string)-i-1)
    return string

string = "Hi how are you?"

print(smarter_reverse(string))

### Libs
# string1 = 'abcde'
# string2 = reversed(string1)
# print(''.join(string2))

