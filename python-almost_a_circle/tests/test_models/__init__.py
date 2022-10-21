#!/usr/bin/python3
"""Unittest for "Base" class"""
import unittest
from models.base import Base


class testsNumber0(unittest.TestCase):
    def setUp(self):
        self.base1 = Base()

    def test_0(self):
        self.assertEqual(self.base1.id, 1)

    def test_1(self):
        self.assertEqual(self.base1.id, 2)
