class MyQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__list_queue = list()

    def is_empty(self):
        return len(self.__list_queue) == 0
    
    def is_full(self):
        return len(self.__list_queue) == self.__capacity
    
    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self.__list_queue.pop(0)
    
    def enqueue(self, value):
        if self.is_full():
            raise Exception('Queue is full')
        return self.__list_queue.append(value)
    
    def front(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self.__list_queue[0]
    
if __name__ == "__main__":
    queue1 = MyQueue(capacity=5)

    queue1.enqueue(1)

    queue1.enqueue(2)

    print(queue1.is_full())
