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

if __name__ == "__name__":
    unittest.main()
