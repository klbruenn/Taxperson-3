import unittest
import item
import total

class FunTest(unittest.TestCase):

    testParams = [
        (100, True, 101.0),
        (100, False, 109.0),
        (100000000000000, True, 101000000000000.0),
        (100000000000000, False, 109000000000000.0),
        (0.001, True, 0.00101),
        (0.001, False, 0.00109),
    ]
    def setUp(self):
        self.anItem = item.Item()

    def test_A(self):
        """
        test different sets of test params
        """
        for (p, n, r) in self.testParams:
            self.anItem.setPrice(p)
            self.anItem.setNecessary(n)
            result = total.total(self.anItem)
            self.assertEqual(result, r, "%s does not match expected value %s" % (result, r))

    def test_Anegative(self):
        """
        fail test negative price
        """
        self.anItem.setPrice(-1)
        try:
            result = total.total(self.anItem)
        except ValueError:
            pass
        else:
            self.fail("Did not see ValueError")

if __name__ == "__main__":
    unittest.main()