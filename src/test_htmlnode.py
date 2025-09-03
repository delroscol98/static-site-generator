import unittest

from htmlnode import HTMLNode
class TestTextNode(unittest.TestCase):
    def test_is_instance(self):
        node = HTMLNode(
            "p",
            "This is a paragraph tag",
            )
        self.assertIsInstance(node, HTMLNode)

    def test_to_html(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_repr(self):
        p = HTMLNode(
            "p",
            "This is a paragraph tag",
            None,
            {
                "class": "para-bold"
                }
        )
        button = HTMLNode(
                "button",
                "click me",
                None,
                {
                    "id": "submit-btn"
                }
        )
        div = HTMLNode(
            "div",
            None,
                [ p, button ],
                {
                    "class": "container"
                }
        )

        self.assertEqual(div.__repr__(),"HTMLNode(div, None, [HTMLNode(p, This is a paragraph tag, None, {'class': 'para-bold'}), HTMLNode(button, click me, None, {'id': 'submit-btn'})], {'class': 'container'})" )

    def test_props_to_html(self):
        input = HTMLNode(
            "input",
            None,
            None,
            {
                "type": "email",
                "name": "email",
                "id": "email",
                "placeholder": "info@example.com"
                }
        )

        res = input.props_to_html()

        self.assertEqual(res, 'type="email" name="email" id="email" placeholder="info@example.com"' )

