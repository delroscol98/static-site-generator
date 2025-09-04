import unittest

from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
        )

    def test_split_bold(self):
        node = TextNode("This is text with a **BOLD** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("BOLD", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
        )

    def test_split_italic(self):
        node = TextNode("This is text with a _ITALIC_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("ITALIC", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
        )

    def test_missing_closing_delimiter(self):
        with self.assertRaises(ValueError):
            node = TextNode("This is a `mistake", TextType.TEXT)
            split_nodes_delimiter([node], "`", TextType.CODE)


if __name__ == "__main__":
    unittest.main()
