class Log:
    def __init__(self, id):
        self.order_id = id
        self.next = None
class Logger:
    def __init__(self):
        self.head = None
        self.num_elements = 0
    def size(self):
        return self.num_elements
    def is_empty(self):
        return self.num_elements == 0
    def record(self, order_id):
        new_log = Log(order_id)
        self.num_elements += 1
        if self.head is None:
            self.head = new_log
            return
        old_head = self.head
        new_log.next = old_head
        self.head = new_log
    def get_last(self):
        if self.is_empty():
            return None
        return self.head.order_id


logger = Logger()
logger.record(3)
logger.record(5)
logger.record(9)
last = logger.get_last()
print(last)

    

