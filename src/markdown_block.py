import re
from enum import Enum

BlockType = Enum(
    "BlockType",
    ["PARAGRAPH", "HEADING", "CODE", "QUOTE", "UNORDERED_LIST", "ORDERED_LIST"],
)


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)

    return filtered_blocks


def block_to_block_type(block):
    if block.count("#") > 0:
        return BlockType.HEADING
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        return BlockType.QUOTE
    if block.startswith("- "):
        return BlockType.UNORDERED_LIST

    lines = block.split("\n")
    for line in lines:
        if line[0].isdigit() and line[1] == ".":
            return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
