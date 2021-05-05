class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


class List(Node):
    def __init__(self, *args):
        super().__init__('head')
        node = self
        for arg in args:
            new_node = Node(arg)
            node.next = new_node
            node = node.next

    def __str__(self):
        node = self

        if node.next:
            list_as_string = '['
            while node.next:
                node = node.next
                list_as_string += f'{str(node.value)}, '

            list_as_string = list_as_string[:-2] + ']'
        else:
            list_as_string = '[]'

        return list_as_string

    def __len__(self):
        counter = 0
        node = self

        if node.next:

            while node.next:
                node = node.next
                counter += 1

        return counter

    def __getitem__(self, item):
        assert len(self) > item, "IndexError"
        counter = 0

        node = self

        if node.next:

            while node.next:
                node = node.next
                if counter == item :
                    return node.value
                counter += 1

    def pop(self, item):
        assert len(self) > item, "IndexError"
        counter = 0

        node = self

        if node.next:

            while node.next:
                prev = node
                node = node.next

                if counter == item:
                    prev.next = node.next
                    return node.value
                counter += 1

    def append(self, val):
        node = self
        while node.next:
            node = node.next
        node.next = Node(val)

    def __setitem__(self, item, val):
        assert len(self) > item, "IndexError"
        counter = 0

        node = self

        if node.next:

            while node.next:
                prev = node
                node = node.next
                if counter == item:
                    ins = Node(val)
                    prev.next = ins
                    ins.next = node.next

                counter += 1

    def insert(self, item, val):
        assert len(self) > item, "IndexError"
        counter = 0

        node = self

        if node.next:

            while node.next:
                prev = node
                node = node.next
                if counter == item:
                    ins = Node(val)
                    prev.next = ins
                    ins.next = node

                counter += 1

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if self.counter < len(self):
            self.counter += 1
            return self[self.counter - 1]
        else:
            raise StopIteration

    def __add__(self, other):
        assert isinstance(other, List)
        node = self
        while node.next:
            node = node.next
        node.next = other.next
        return self


my_list = List(2, List('dfg', 10, 20), 4, None)
print(my_list)
# print(len(my_list))
# print(my_list[20])
# print(my_list.pop(3))
# print(my_list.pop(1))
# print(my_list)
# my_list.append(34)
# print(my_list)

# my_list[2] = 34
# print(my_list)
# my_list.insert(2, 21)
# print(my_list)

# for i in my_list:
#     print(i)
my_list = my_list + List(1, 2, 3)
print(my_list)

