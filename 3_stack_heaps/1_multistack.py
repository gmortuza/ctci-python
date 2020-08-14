class MultiStack:
    def __init__(self, stack_capacity):
        self.num_stack = 3
        self.stack_capacity = stack_capacity
        self.array = [None] * (stack_capacity * self.num_stack)
        self.stack_sizes = [0] * self.num_stack

    def push(self, stack_number):
        """
        Push value in the stack
        :param stack_number: put value in this stack number
        :return:
        """
        if self.stack_sizes[stack_number] > self.stack_capacity:
            raise Exception("Stack full")
        self.stack_sizes[stack_number] += 1
        self.array[stack_number*self.stack_capacity]