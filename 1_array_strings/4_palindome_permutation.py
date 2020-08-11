import unittest
from collections import Counter

def pal_perm(str1):
    count = Counter()
    total_element = 0
    for i in str1.lower():
        if i >= 'a' and i <= 'z':
            count[i] += 1
            total_element += 1
    app = True if total_element % 2 == 0 else False
    for key, val in count.items():
        if val % 2 == 1 and app:
            return False
        elif val % 2 == 1:
            app = True
    return True

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = pal_perm(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
