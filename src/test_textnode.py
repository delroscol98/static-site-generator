import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_node_is_instance_of_TextNode(self):
        node = TextNode("This is a text node", TextType.TEXT)
        self.assertIsInstance(node, TextNode)

    def test_invalid_text_type(self):
        with self.assertRaises(TypeError):
            TextNode("test", "not valid")

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.google.com")
        self.assertEqual(
                node.__repr__(),
                "TextNode(This is a text node, TextType.BOLD, www.google.com)"
        )


if __name__ == "__main__":
    unittest.main()
