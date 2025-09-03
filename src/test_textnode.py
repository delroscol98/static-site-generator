import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_node_is_instance_of_TextNode(self):
        node = TextNode("This is a text node", TextType.TEXT)
        self.assertIsInstance(node, TextNode)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.google.com")
        self.assertEqual(
            node.__repr__(),
            "TextNode(This is a text node, TextType.BOLD, www.google.com)",
        )

    def test_invalid_text_type(self):
        with self.assertRaises(TypeError):
            invalid_text_node = TextNode("test", "not valid")
            text_node_to_html_node(invalid_text_node)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.to_html(), "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")
        self.assertEqual(html_node.to_html(), "<b>This is a bold node</b>")

    def test_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")
        self.assertEqual(html_node.to_html(), "<i>This is an italic node</i>")

    def test_code(self):
        node = TextNode('print("Hello world!")', TextType.CODE)
        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, 'print("Hello world!")')
        self.assertEqual(html_node.to_html(), '<code>print("Hello world!")</code>')

    def test_link(self):
        node = TextNode("Click me", TextType.LINK, "https://www.example.com")
        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click me")
        self.assertEqual(html_node.props, {"href": "https://www.example.com"})
        self.assertEqual(
            html_node.to_html(), '<a href="https://www.example.com">Click me</a>'
        )

    def test_image(self):
        node = TextNode("example alt text", TextType.IMAGE, "./example.png")
        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props, {"src": "./example.png", "alt": "example alt text"}
        )
        self.assertEqual(
            html_node.to_html(),
            '<img src="./example.png" alt="example alt text"></img>',
        )


if __name__ == "__main__":
    unittest.main()
