#Find the largest word in a given string
#Examples
#Input: "fun&!! time"
#Output: time


def solve(string):
    max_count = 0
    max_word = ""

    current_word = ""
    current_count = 0    
    for idx in range(len(string)):
        char = string[idx]

        if char.isalpha():
            current_word += char
            current_count += 1
        
        if not char.isalpha() or idx == len(string) - 1:
            if current_count > max_count:
                max_word = current_word
                max_count = current_count
                
            current_count = 0
            current_word = ""
        
    
    return max_count, max_word



data = "fun&!! time"

print(solve(data))