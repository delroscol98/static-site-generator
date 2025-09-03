import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_is_instance(self):
        p = LeafNode("p", "This is a paragraph tag", {"class": "para"})

        self.assertIsInstance(p, LeafNode)

    def test_to_html(self):
        p = LeafNode("p", "This is a paragraph tag", {"id": "text", "class": "para"})
        p_html = p.to_html()

        h1 = LeafNode("h1", "This is a heading tag")
        h1_html = h1.to_html()

        self.assertEqual(
            p_html, '<p id="text" class="para">This is a paragraph tag</p>'
        )
        self.assertEqual(h1_html, "<h1>This is a heading tag</h1>")


if __name__ == "__main__":
    unittest.main()
