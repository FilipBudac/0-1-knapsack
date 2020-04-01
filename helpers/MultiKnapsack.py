class MultiKnapsack:
    WEIGHT = 2
    VALUE = 1

    def __init__(self):
        self.items = []
        self.K = []
        self.N = 0
        self.W = 0
        self.F = 0

    def load_from_file(self, filename: str) -> None:
        """
        loads knapsack with file contents
        :param filename:
        """
        file_contents = [line.replace('\n', '') for line in open(filename)]

        self.N = int(file_contents.pop(0))
        self.W = int(file_contents.pop(0))
        self.F = int(file_contents.pop(0))

        self.items = [list(map(int, item.split())) for item in file_contents]

    def knapsack(self):
        """
        0-1 knapsack
        """
        self.K = [[0 for x in range(self.W + 1)] for x in range(self.N + 1)]

        for item in range(1, self.N + 1):
            for weight in range(1, self.W + 1):
                item_weight = self.items[item - 1][self.WEIGHT]
                item_value = self.items[item - 1][self.VALUE]

                if item_weight <= weight:
                    self.K[item][weight] = max(item_value + self.K[item - 1][weight - item_weight], self.K[item - 1][weight])
                else:
                    self.K[item][weight] = self.K[item - 1][weight]

        self.print_knapsack()
        print(self.K[self.N][self.W])

    def print_knapsack(self):
        for row in self.K:
            print(row)