import unittest
from price_info import total_cost_shopping, cost_of_fruits, price_list, quantity_list

class TestPriceInfo(unittest.TestCase):

    def test_total_cost_shopping(self):
        # Calculate expected total cost by iterating over the dictionaries
        expected_total = sum(price_list[fruit] * quantity for fruit, quantity in quantity_list.items())
        self.assertAlmostEqual(total_cost_shopping(), expected_total)

    def test_cost_of_fruits(self):
        # Test for individual fruit cost
        self.assertAlmostEqual(cost_of_fruits('apple', 10), 12.0)  # 10 * 1.20 = 12.0
        self.assertAlmostEqual(cost_of_fruits('orange', 3), 4.2)   # 3 * 1.40 = 4.2

if __name__ == "__main__":
    unittest.main()
