import unittest

from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_is_instance(self):
        h1 = LeafNode("h1", "This is a heading tag")
        p = LeafNode("p", "This is a paragraph tag")
        div = ParentNode("div", [h1, p])

        self.assertIsInstance(div, ParentNode)

    def test_no_tag(self):
        with self.assertRaises(ValueError):
            invalid = ParentNode(None, [])
            invalid.to_html()

    def test_no_children(self):
        with self.assertRaises(ValueError):
            invalid = ParentNode("div", None)
            invalid.to_html()

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_with_children_props(self):
        p = LeafNode("p", "This is a paragraph tag", {"id": "text__main"})
        a = LeafNode("a", "Click me", {"href": "https://www.example.com"})
        div = ParentNode("div", [p, a])
        self.assertEqual(
            div.to_html(),
            '<div><p id="text__main">This is a paragraph tag</p><a href="https://www.example.com">Click me</a></div>',
        )

    def test_with_grandchildren_props(self):
        h1 = LeafNode("h1", "This is a heading", {"id": "heading-left"})
        p = LeafNode("p", "This is a paragraph", {"id": "paragraph-left"})
        h2 = LeafNode("h2", "This is another heading")

        article = ParentNode("article", [h1, p])
        section = ParentNode("section", [article, h2])

        self.assertEqual(
            section.to_html(),
            '<section><article><h1 id="heading-left">This is a heading</h1><p id="paragraph-left">This is a paragraph</p></article><h2>This is another heading</h2></section>',
        )


if __name__ == "__name__":
    unittest.main()
