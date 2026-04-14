import timeit

# 基于List的队列（队尾入队O(1)，队头出队O(n))
class ListQueue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item) 
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")
    def is_empty(self):
        return len(self.items) == 0
# 队列单向链表实现: 同时记录首尾, 尾部入队O(1)，头部出队O(1)
class ListNode:
    def __init__(self, value = None):
        self.val = value
        self.next = None
class LinkedListQueue():
    def __init__(self):
        self.head = ListNode()
        self.tail = self.head
        self.size = 0
    def _add_to_tail(self, node: ListNode):
        self.tail.next = node
        self.tail = node
        self.size += 1
    def _remove_from_head(self):
        if self.head.next is None:
            raise IndexError("Queue is empty")
        target = self.head.next
        self.head.next = target.next
        if self.size == 1:
            self.tail = self.head
        self.size -= 1
    def enqueue(self, val: int):
        new_node = ListNode(value = val)
        self._add_to_tail(new_node)
    def peek(self):
        if self.size == 0:
            raise IndexError("Queue is empty")
        return self.head.next.val
    def dequeue(self) -> int:
        if self.size == 0:
            raise IndexError("Queue is empty")
        val = self.head.next.val
        self._remove_from_head()
        return val

# 测试给定队列的出入队性能：
def test_performance():
    # 枚举数据大小
    test_sizes = [1000, 10000, 100000]
    for size in test_sizes:
        # 测量 N 次入列的用时：
        # A. 基于list的链表
        setup_list = "from __main__ import ListQueue; q = ListQueue()"
        run_list = "q.enqueue(1)"
        t_enq_list = timeit.timeit(run_list, setup_list, number = size)
        # B. 基于linkedlist的链表
        setup_ll = "from __main__ import LinkedListQueue; q = LinkedListQueue()"
        run_ll = "q.enqueue(1)"
        t_enq_ll = timeit.timeit(run_ll, setup_ll, number = size)

        # 测量 N 次出列的用时：
        # A. 基于list的链表
        setup_list = f"from __main__ import ListQueue; q = ListQueue(); [q.enqueue(i) for i in range({size})]"
        run_list = "q.dequeue()"
        t_deq_list = timeit.timeit(run_list, setup_list, number = size)
        # B. 基于linkedlist的链表
        setup_ll = f"from __main__ import LinkedListQueue; q = LinkedListQueue(); [q.enqueue(i) for i in range({size})]"
        run_ll = "q.dequeue()"
        t_deq_ll = timeit.timeit(run_ll, setup_ll, number = size)
        print(f"# SIZE: {size} ")
        print(f"       LIST  |{1000*t_enq_list:^15.5f}ms|{1000*t_deq_list:^15.5f}ms")
        print(f" LINKEDLIST  |{1000*t_enq_ll:^15.5f}ms|{1000*t_deq_ll:^15.5f}ms")
test_performance()

