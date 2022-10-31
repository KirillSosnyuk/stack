class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        removed_item = self.stack.pop()
        return removed_item

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def isEmpty(self):
        if self.size() == 0:
            return True
        else:
            return False


def isBalanced(quotes: str):
    instance = Stack()

    open_dict = ('{', '[', '(')
    close_dict = {'}': '{', ')': '(', ']': '['}

    for elem in quotes:
        if elem in open_dict:
            instance.push(elem)
        elif elem in close_dict:
            if instance.size() != 0 and close_dict[elem] == instance.peek():
                instance.pop()
            else:
                return 'Несбалансировано'

    if instance.isEmpty():
        return 'Сбалансировано'
    else:
        return 'Несбалансировано'


if __name__ == '__main__':
    print(isBalanced(input('Введите строку для проверки: ')))