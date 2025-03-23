import unittest

from leafnode import LeafNode


class Test_LeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_with_props_to_html(self):
        res = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
        self.assertEqual('<a href="https://www.google.com">Click me!</a>', res)

    def test_no_tag(self):
        node = LeafNode("", "Hello, world!")
        self.assertEqual("Hello, world!", node.to_html())

    def test_no_value(self):
        node = LeafNode("p", "")
        self.assertRaises(ValueError, node.to_html)

    def test_no_tag_and_value(self):
        node = LeafNode("", "")
        self.assertRaises(ValueError, node.to_html)
