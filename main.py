from helpers.Knapsack import MultiKnapsack

TEST_1 = 'tests/t1.txt'
TEST_2 = 'tests/t2.txt'
TEST_3 = 'tests/t3.txt'
TEST_4 = 'tests/t4.txt'
TEST_5 = 'tests/t5.txt'

mk = MultiKnapsack()
mk.load_from_file(TEST_1)
mk.knapsack()

mk.load_from_file(TEST_3)
mk.knapsack_3d()

mk.load_from_file(TEST_4)
mk.knapsack_3d()

mk.load_from_file(TEST_5)
mk.knapsack_3d()
mk.write_to_file('output.txt')
