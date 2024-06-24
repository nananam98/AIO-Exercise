class MyStack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__list_stack = list()

    def is_empty(self):
        return len(self.__list_stack) == 0
    
    def is_full(self):
        return len(self.__list_stack) == self.__capacity
    
    def pop(self):
        if self.is_empty():
            raise Exception("Underflow")
        return self.__list_stack.pop()
    
    def push(self, value):
        if self.is_full():
            raise Exception("Overflow")
        return self.__list_stack.append(value)
    
    def top(self):
        if self.is_empty():
            print("Stack is empty")
            return
        return self.__list_stack[-1]
    
if __name__ == "__main__":
    stack1 = MyStack(capacity=5)

    stack1.push(1)

    stack1.push(2)

    print(stack1.is_full())

    print(stack1.top())

    print(stack1.pop())

    print(stack1.top())

    print(stack1.pop())