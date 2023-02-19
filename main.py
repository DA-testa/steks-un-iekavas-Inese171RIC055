# python3

from collections import namedtuple, deque

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = deque()
    errors = deque()
    for i, next in enumerate(text, 1):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i))
        elif next in ")]}":
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                return i
            opening_brackets_stack.pop()

    if opening_brackets_stack:
        return i
    else:
        return "Success"

def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == '__main__': 
    choice = input("Enter F to choose test file or I to enter input: ") 
    if choice == 'F': 
        filename = input('Enter test filename: ') 
        with open(filename) as file: 
            for line in file: 
                print(find_mismatch(line.strip())) 
    elif choice == 'I': 
        main()
