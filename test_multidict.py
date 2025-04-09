import unittest
from multidict import MultiDict

class TestMultiDict(unittest.TestCase):
    def setUp(self):
        self.md = MultiDict()

    def test_setitem_single_value(self):
        self.md['a'] = 1
        self.assertEqual(self.md['a'], [1])

    def test_setitem_multiple_values(self):
        self.md['a'] = 1
        self.md['a'] = 2
        self.assertEqual(self.md['a'], [1, 2])

    def test_getitem(self):
        self.md['a'] = 1
        self.assertEqual(self.md['a'], [1])

    def test_delitem(self):
        self.md['a'] = 1
        del self.md['a']
        with self.assertRaises(KeyError):
            _ = self.md['a']

    def test_len(self):
        self.md['a'] = 1
        self.md['a'] = 2
        self.md['b'] = 3
        self.assertEqual(len(self.md), 2)   
        del self.md['a']
        self.assertEqual(len(self.md), 1)

    def test_repr(self):
        self.md['a'] = 1
        self.assertEqual(repr(self.md), repr(MultiDict({'a': [1]})))     

    def test_init_with_dict(self):
        try:
            d = {'a': 1, 'b': 2}
            md = MultiDict(d)
        except TypeError as e:
            self.assertEqual(str(e), "Value for key 'a' must be a list.")

if __name__ == '__main__':
    unittest.main()
