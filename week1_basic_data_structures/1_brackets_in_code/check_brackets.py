# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"]) # I don't know what's this line for


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next)
            opening_pos = i + 1

        if next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack: # if stack is empty
                return i + 1
            top = opening_brackets_stack.pop()
            
            if not are_matching(top, next):
                return i + 1
            
            opening_pos -= 1
    
    if not opening_brackets_stack: # if stack is empty
        return 'Success'
    elif opening_pos >= 1:
        return opening_pos - len(opening_brackets_stack) + 1 # find the first index of the unmatched opening bracket
    else:
        return i + 1 # The last position
            


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)

if __name__ == "__main__":
    main()
