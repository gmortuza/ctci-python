class MultiStack:
    def __init__(self, stack_capacity):
        self.num_stack = 3
        self.stack_capacity = stack_capacity
        self.array = [None] * (stack_capacity * self.num_stack)
        # This will contain the minimum value in each stage
        self.min = [None] * (stack_capacity * self.num_stack)
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
        self.stack_sizes[stack_number] += 1
        self.array[self.__get_stack_offset(stack_number)] = value
        self.min[self.__get_stack_offset(stack_number)] = self.__get_min(stack_number, value)

    def __get_min(self, stack_number, value):
        if self.stack_sizes[stack_number] <= 1:
            return value
        return min(self.min[self.__get_stack_offset(stack_number) - 1], value)

    def __get_stack_offset(self, stack_number):
        return (stack_number * self.stack_capacity) + self.stack_sizes[stack_number] - 1

    def pop(self, stack_number):
        """

        :return:
        """
        value = self.array[(stack_number * self.stack_capacity) + self.stack_sizes[stack_number] - 1]
        self.array[self.__get_stack_offset(stack_number)] = None
        self.min[self.__get_stack_offset(stack_number)] = None
        self.stack_sizes[stack_number] -= 1
        return value

    def get_stack_min(self, stack_number):
        return self.min[self.__get_stack_offset(stack_number)]


if __name__ == '__main__':
   stack = MultiStack(10)
   stack.push(0, 1)
   stack.push(1, 5)
   stack.push(2, 4)
   stack.push(0, -1)
   stack.push(0, 10)
   stack.push(0, 100)
   stack.push(0, -100)
   stack.pop(0)
   print(stack.get_stack_min(0))
   print(stack.array)