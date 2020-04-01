from helpers.MultiKnapsack import MultiKnapsack

TEST_1 = 'tests/t1.txt'

mk = MultiKnapsack()
mk.load_from_file(TEST_1)
mk.knapsack()
