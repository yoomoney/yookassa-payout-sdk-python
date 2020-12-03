# -*- coding: utf-8 -*-
import unittest
from yookassa_payout.domain.common.xml_helper import XMLHelper, Object2XML, XML2Object


class TestXMLHelper(unittest.TestCase):

    def test_object_to_xml(self):
        obj = self.get_obj()
        comp = '<root param1="param1" param2="param2"><params p1="p1" p2="p2" /></root>'

        res = XMLHelper.object_to_xml(obj)
        self.assertEqual(res, comp)

        res = XMLHelper.object_to_xml({"xml": ["p1", "p2", None]})
        self.assertEqual(res, '<xml>p1p2</xml>')

        res = XMLHelper.object_to_xml(["p1", "p2", None])
        self.assertEqual(res, 'p1p2')

        res = XMLHelper.object_to_xml(None)
        self.assertEqual(res, "")

    def test_xml_to_object(self):
        obj = self.get_obj()
        comp = '<root param1="param1" param2="param2"><params p1="p1" p2="p2" /></root>'

        res = XMLHelper.xml_to_object(comp)
        self.assertEqual(res, dict(obj))

    def test_object_parse(self):
        o = Object2XML()

        res = o.parse([{"p1": "p1", "p2": ["p2"]}], 'items')
        self.assertEqual(res, '<items><item p1="p1"><p2>p2</p2></item></items>')

        res = o.parse('test', 'root')
        self.assertEqual(res, '<root>test</root>')

        res = o.parse(["test"], 'root')
        self.assertEqual(res, '<root>test</root>')

        res = o.parse([{"p1": "p1"}], 'items')
        self.assertEqual(res, '<items><item p1="p1" /></items>')

        res = o.parse({"root": ["test"]})
        self.assertEqual(res, '<root>test</root>')

        res = o.parse({"root": [""]})
        self.assertEqual(res, '<root></root>')

        res = o.parse([""], "root")
        self.assertEqual(res, '<root></root>')

        res = o.parse([None], "root")
        self.assertEqual(res, '<root></root>')

        res = o.parse({"root": None})
        self.assertEqual(res, '')

        res = o.parse(None, "root")
        self.assertEqual(res, '')

        # var_dump(res)

    def test_xml_parse(self):

        x = XML2Object()

        with self.assertRaises(ValueError):
            x.parse('')

        res = x.parse('<test/>')
        self.assertEqual(res, {'test': []})

        res = x.parse('<root><params></params></root>')
        self.assertEqual(res, {"root": [[]]})

        res = x.parse('<root><params>text</params></root>')
        self.assertEqual(res, {"root": [["text"]]})

        res = x.parse('<root param1="param1" param2="param2"><params p1="p1" p2="p2" /></root>')
        self.assertEqual(res, self.get_obj())

        res = x.to_string()
        self.assertEqual(res, b'<root param1="param1" param2="param2"><params p1="p1" p2="p2"/></root>')
        self.assertEqual(res.decode(), '<root param1="param1" param2="param2"><params p1="p1" p2="p2"/></root>')

    @staticmethod
    def get_obj():
        return {
            "root": {
                "param1": "param1",
                "param2": "param2",
                "params": {
                    "p1": "p1",
                    "p2": "p2",
                },
            }
        }
