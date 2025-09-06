import unittest

from markdown_to_html import markdown_to_html_node


class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_heading_block(self):
        md = """# This is a first level heading

## This is a second level heading

### This is a third level heading

This is some paragraph text
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is a first level heading</h1><h2>This is a second level heading</h2><h3>This is a third level heading</h3><p>This is some paragraph text</p></div>",
        )

    def test_ul(self):
        md = """
## List 1

- List item 1
- List item 2
- List item 3

## List 2

- List item 1
- List item 2
- List item 3
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h2>List 1</h2><ul><li>List item 1</li><li>List item 2</li><li>List item 3</li></ul><h2>List 2</h2><ul><li>List item 1</li><li>List item 2</li><li>List item 3</li></ul></div>",
        )

    def test_ol(self):
        md = """
## List 1

1. List item 1
2. List item 2
3. List item 3

## List 2

1. List item 1
2. List item 2
3. List item 3
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h2>List 1</h2><ol><li>List item 1</li><li>List item 2</li><li>List item 3</li></ol><h2>List 2</h2><ol><li>List item 1</li><li>List item 2</li><li>List item 3</li></ol></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )


if __name__ == "__main__":
    unittest.main()
