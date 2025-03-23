import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_values(self):
        node1 = HTMLNode("d", "pupukaka", props={"hu": "hihi", "blah": "meh"})
        print(node1)

    def test_to_html(self):
        node1 = HTMLNode("d", "pupukaka", props={"hu": "hihi", "blah": "meh"})
        self.assertEqual(' hu="hihi" blah="meh"', node1.props_to_html())

    def test_to_html_no_props(self):
        node1 = HTMLNode("d", "pupukaka")
        self.assertEqual("", node1.props_to_html())
