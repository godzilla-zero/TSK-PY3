
def check_brackets(brackets_row, str="〈〉()[]{}"):
    opening, closing = str[::2], str[1::2]
    stack = []
    for character in brackets_row:
        if character in opening:
            stack.append(opening.index(character))
        elif character in closing:
            if stack and stack[-1] == closing.index(character):
                stack.pop()  # remove the matched pair
            else:
                return False
    return (not stack)

if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False
