#!/usr/bin/env python

import json
import unittest
import datetime 

class SchemaTest(unittest.TestCase):
    def test(self):
        file = open('vat-rates.json')
        data = json.load(file)
        self.assertEqual(len(data['items']), 28)
       
        for country, periods in data['items'].items():
            self.assertEqual(type(country), str)
            self.assertEqual(type(periods), list)
            prev = None

            for p in periods:
                self.assertEqual(type(p), dict)
                self.assertEqual(type(p['effective_from']), str)
                self.assertEqual(type(p['rates']), dict)
                self.assertIsInstance(p['rates']['standard'], (int, float))

                date = datetime.datetime.strptime(p['effective_from'].replace('0000', '2000'), '%Y-%m-%d') 
                if prev:
                    self.assertLess(date, prev, "periods for {} are not sorted with most recent period first".format(country))
                prev = date


        file.close()

if __name__ == '__main__':
    unittest.main()
