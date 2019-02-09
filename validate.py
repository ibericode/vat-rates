#!/usr/bin/env python

import json
import unittest

class SchemaTest(unittest.TestCase):
    def test(self):
        file = open('vat-rates.json')
        data = json.load(file)
        self.assertEqual(len(data['items']), 28)
       
        for country, periods in data['items'].items():
            self.assertEqual(type(country), str)
            self.assertEqual(type(periods), list)

            for p in periods:
                self.assertEqual(type(p), dict)
                self.assertEqual(type(p['effective_from']), str)
                self.assertEqual(type(p['rates']), dict)
                self.assertIsInstance(p['rates']['standard'], (int, float))

        file.close()

if __name__ == '__main__':
    unittest.main()
