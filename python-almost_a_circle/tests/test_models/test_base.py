#!/usr/bin/python3
"""Unittest for "Base" class"""
import unittest
from models.base import Base


class tests_base0(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Base().id, 1)

    def test_2(self):
        self.assertEqual(Base().id, 2)

    def test_3(self):
        self.assertEqual(Base(59).id, 59)

    def test_4(self):
        self.assertEqual(Base().to_json_string([]), '[]')

    def test_5(self):
        self.assertEqual(Base().from_json_string(None), [])

    def test_6(self):
        self.assertEqual(Base().from_json_string("[]"), [])

    def test_7(self):
        self.assertEqual(Base().from_json_string('[{ "id": 89 }]'), [{'id': 89}])