import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is another text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

        node2 = TextNode("this is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_check_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.url, "")

    def test_text_to_html(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = node.create_htmlLeafNode()
        self.assertEqual(html_node.tag, "")
        self.assertEqual(html_node.value, "This is a text node")


if __name__ == "__main__":
    unittest.main()
