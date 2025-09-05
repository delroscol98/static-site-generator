import unittest

from markdown_block import BlockType, block_to_block_type, markdown_to_blocks


class TestMarkDownBlock(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """This is **bolded** paragraph









This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_heading(self):
        block1 = "#This is a heading"
        block2 = "##This is a heading"
        block_type1 = block_to_block_type(block1)
        block_type2 = block_to_block_type(block2)

        self.assertEqual(block_type1, BlockType.HEADING)
        self.assertEqual(block_type2, BlockType.HEADING)

    def test_block_to_code(self):
        block = """```
            console.log("This is JavaScript in Python")
        ```"""
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, BlockType.CODE)

    def test_block_to_quote(self):
        block = "> With great power comes great responsibility"
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, BlockType.QUOTE)

    def test_block_to_unordered_single(self):
        block = "- There is one item"
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_block_to_unordered_multiple(self):
        block = "- This is one item\n- This is another item\n- This is the final item"
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_block_to_ordered_single(self):
        block = "1. There is one item"
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_block_to_ordered_multiple(self):
        block = (
            "1. This is one item\n2. This is another item\n3. This is the final item"
        )
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, BlockType.ORDERED_LIST)


if __name__ == "__main__":
    unittest.main()
