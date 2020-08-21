class MultiStack:
    def __init__(self, stack_capacity):
        self.num_stack = 3
        self.stack_capacity = stack_capacity
        self.array = [None] * (stack_capacity * self.num_stack)
        self.stack_sizes = [0] * self.num_stack

    def push(self, stack_number, value):
        """
        Push value in the stack
        :param stack_number: put value in this stack number
        :param value: Value to be pushed
        :return:
        """
        if self.stack_sizes[stack_number] > self.stack_capacity:
            raise Exception("Stack full")
        self.array[(stack_number*self.stack_capacity) + self.stack_sizes[stack_number]] = value
        self.stack_sizes[stack_number] += 1

    def pop(self, stack_number):
        """

        :return:
        """
        value = self.array[(stack_number * self.stack_capacity) + self.stack_sizes[stack_number] - 1]
        self.array[(stack_number * self.stack_capacity) + self.stack_sizes[stack_number] - 1] = None
        self.stack_sizes[stack_number] -= 1
        return value


if __name__ == '__main__':
   stack = MultiStack(10)
   stack.push(0, 1)
   stack.push(1, 5)
   stack.push(2, 4)
   print(stack.pop(2))
   print(stack.array)

