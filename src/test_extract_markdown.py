import unittest

from extract_markdown import extract_images, extract_links, extract_title


class TestExtract(unittest.TestCase):
    def test_extractn_images(self):
        matches = extract_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_links(self):
        matches = extract_links("This is text with an [link](https://www.google.com)")
        self.assertListEqual([("link", "https://www.google.com")], matches)

    def test_extract_title(self):
        match = extract_title("# This is a title")
        self.assertEqual(match, "This is a title")
        with self.assertRaises(ValueError):
            extract_title("This is a title")


if __name__ == "__name__":
    unittest.main()
