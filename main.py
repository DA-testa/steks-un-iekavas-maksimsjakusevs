# python3
# Maksims Jaksuevs 221RDB376

from collections import namedtuple
Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    opening_brackets_stack = []


    for i, next in enumerate(text):
        if next in " ([{ ":
            opening_brackets_stack.append(Bracket(next, i + 1))

        if next in " )]} ":

            if are_matching(opening_brackets_stack.pop().char, next) == False:
                return i + 1

    if (len(opening_brackets_stack) == 0):
        return ' Success '

    else:
        while len(opening_brackets_stack) > 0:
            first_opening_bracket = opening_brackets_stack.pop()
        return first_opening_bracket.position 


def main():
    text=input()
    if 'I' in text:
        text=input()
    mismatch=find_mismatch(text)
    print(mismatch)

if __name__ == "__main__":
    main()