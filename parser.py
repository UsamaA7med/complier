terminals = {
    '=', '+', '-', '*', '/', '%', '|', '\\', '&', '^', '!', '#', '(', ')', '{', '}', '[', ']', '\'', ';', ':', ',', '.',
    '\"', '~', '`', '_'
}

grammar = [('', '') for _ in range(4)]
stack = []
idx = 0
input_string = ''


def is_terminal(n):
    return n.islower() or n.isdigit() or n in terminals


def is_simple_grammar():
    for rule in grammar:
        if is_terminal(rule[0]) or not is_terminal(rule[1][0]):
            return False
    if grammar[0][1][0] == grammar[1][1][0] or grammar[2][1][0] == grammar[3][1][0]:
        return False
    return True


def solve():
    global idx
    while stack:
        if idx == len(input_string):
            break
        top = stack[-1]

        if is_terminal(top):
            if top == input_string[idx]:
                stack.pop()
                idx += 1
            else:
                return False
        else:
            if top == 'S':
                non_terminal = 0
            elif top == 'B':
                non_terminal = 2
            else:
                return False

            if input_string[idx] == grammar[non_terminal][1][0]:
                rule = 0
            elif input_string[idx] == grammar[non_terminal + 1][1][0]:
                rule = 1
            else:
                return False

            stack.pop()
            for char in reversed(grammar[non_terminal + rule][1]):
                stack.append(char)

    return not stack and idx == len(input_string)


def main():
    global idx, input_string, stack
    while True:
        grammar[0] = ('S', '')
        grammar[1] = ('S', '')
        grammar[2] = ('B', '')
        grammar[3] = ('B', '')

        for i in range(4):
            non_terminal = 'S' if i < 2 else 'B'
            grammar[i] = (non_terminal, input(f"Enter rule number {i + 1} for non-terminal '{non_terminal}': ").strip())

        if not is_simple_grammar():
            print("Not a simple grammar")
            continue

        while True:
            input_string = input("Enter the string to be checked: ").strip()
            print(f"The input string: [{', '.join([f'\'{char}\'' for char in input_string])}]")

            stack = []
            idx = 0
            stack.append('S')

            accepted = solve()

            print("Stack after checking: [", end="")
            print(", ".join([f"'{char}'" for char in reversed(stack)]), end="")
            print("]")

            print("The rest of the unchecked string: [", end="")
            print(", ".join([f"'{char}'" for char in input_string[idx:]]), end="")
            print("]")

            if accepted:
                print("The input string is Accepted.")
            else:
                print("The input string is Rejected.")

            print("1- Another grammar.")
            print("2- Another string.")
            print("3- Exit.")
            choice = int(input("Enter your choice: ").strip())

            if choice == 1:
                break
            elif choice == 3:
                return


if _name_ == "_main_":
    main()
