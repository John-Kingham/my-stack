import unittest
from stack import *


class TestStack(unittest.TestCase):

    def test_push(self):
        s = Stack(2)
        s.push(1)
        self.assertEqual(s.peek(), 1)
        s.push(2)
        self.assertEqual(s.peek(), 2)
        s.push(3)
        self.assertEqual(s.peek(), 2)

    def test_pop(self):
        s = Stack()
        for i in range(3):
            s.push(i+1)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.peek(), 2)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)
        self.assertIsNone(s.pop())

    def test_peek(self):
        s = Stack()
        s.push(1)
        self.assertEqual(s.peek(), 1)
        self.assertEqual(s.peek(), 1)
