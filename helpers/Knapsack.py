class MultiKnapsack:
    VALUE = 1
    WEIGHT = 2
    FRAGILE = 3

    def __init__(self):
        self.__items = []
        self.__K = []
        self.__N = 0
        self.__W = 0
        self.__F = 0
        self.__used_items = []
        self.optimal_value = 0

    def load_from_file(self, filename: str) -> None:
        """
        loads knapsack with file contents from file specified
        :param filename:
        """
        file_contents = [line.replace('\n', '') for line in open(filename)]

        self.__N = int(file_contents.pop(0))
        self.__W = int(file_contents.pop(0))
        self.__F = int(file_contents.pop(0))

        self.__items = [list(map(int, item.split())) for item in file_contents]

    def knapsack(self) -> None:
        """
        0-1 knapsack [value][weight]
        """
        self.__K = [[0 for w in range(self.__W + 1)] for i in range(self.__N + 1)]

        for item in range(1, self.__N + 1):
            for weight in range(1, self.__W + 1):
                item_weight = self.__items[item - 1][self.WEIGHT]
                item_value = self.__items[item - 1][self.VALUE]

                if item_weight <= weight:
                    self.__K[item][weight] = max(item_value + self.__K[item - 1][weight - item_weight],
                                                 self.__K[item - 1][weight]
                                                 )
                else:
                    self.__K[item][weight] = self.__K[item - 1][weight]

        self.print_knapsack()
        print(self.__K[self.__N][self.__W])

    def knapsack_3d(self) -> None:
        """
        0-1 knapsack [value][weight][fragility]
        """
        self.__K = [[[0 for f in range(self.__F + 1)] for w in range(self.__W + 1)] for i in range(self.__N + 1)]

        for item in range(1, self.__N + 1):
            for weight in range(0, self.__W + 1):
                for fragile in range(0, self.__F + 1):
                    item_value = self.__items[item - 1][self.VALUE]
                    item_weight = self.__items[item - 1][self.WEIGHT]
                    item_fragile = self.__items[item - 1][self.FRAGILE]

                    if item_weight <= weight and item_fragile <= fragile:
                        self.__K[item][weight][fragile] = max(
                                                            item_value +
                                                            self.__K[item - 1][weight - item_weight][fragile - item_fragile],
                                                            self.__K[item - 1][weight][fragile]
                                                            )
                    else:
                        self.__K[item][weight][fragile] = self.__K[item - 1][weight][fragile]

        self.print_knapsack()
        self.optimal_value = self.__K[self.__N][self.__W][self.__F]
        print(self.__K[self.__N][self.__W][self.__F])

    def write_to_file(self, filename: str) -> None:
        """
        writes knapsack results to file specified

        optimal value
        count of items in knapsack
        id_1 if item inserted
        ...
        id_n if item inserted

        :param filename:
        """
        self.__collect_items()

        file = open(filename, "w+")
        file.write(f"{self.optimal_value}\n")
        file.write(f"{len(self.__used_items)}\n")

        for item in self.__used_items:
            file.write(f"{item[0]}\n")

    def __collect_items(self) -> None:
        """
        collects items from knapsack
        """
        tmp_fragile = self.__F
        tmp_weight = self.__W

        for count in range(self.__N, 0, -1):
            if self.__K[count][self.__W][self.__F] != self.__K[count - 1][self.__W][self.__F] and 0 <= tmp_weight - self.__items[count - 1][self.WEIGHT]:
                tmp_fragile -= self.__items[count - 1][self.FRAGILE]
                tmp_weight -= self.__items[count - 1][self.WEIGHT]
                self.__used_items.insert(0, self.__items[count - 1])

    def print_knapsack(self) -> None:
        """
        print knapsack
        """
        for row in self.__K:
            print(row)
