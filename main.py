# Maksims Jakusevs 221RDB376

class Bracket:
    def __init__(self, type, position):
        self.type = '\0'
        self.position = 0

        self.type = type
        self.position = position

    def Matchc(self, c):
        if self.type == '[' and c == ']':
            return True
        if self.type == '{' and c == '}':
            return True
        if self.type == '(' and c == ')':
            return True
        return False


def main():
    text = ""
    text = input()

    opening_brackets_stack = []

    position = 0
    while position < len(text):
        next = text[position]

        if next == '(' or next == '[' or next == '{':
            opening_brackets_stack.push(Bracket(next, position + 1))

        if next == ')' or next == ']' or next == '}':
            if opening_brackets_stack.empty() or not opening_brackets_stack.top().Matchc(next):
                print(position + 1, end = '')
                print("\n", end = '')
            opening_brackets_stack.pop()
        position += 1

    if opening_brackets_stack.empty():
        print("Success", end = '')
        print("\n", end = '')
    else:
        print(opening_brackets_stack.top().position, end = '')
        print("\n", end = '')

if __name__ == "__main__":
    main()
