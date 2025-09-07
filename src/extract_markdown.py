import re


def extract_images(markdown):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", markdown)
    return matches


def extract_links(markdown):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", markdown)
    return matches


def extract_title(markdown):
    match = re.search(r"[#].*", markdown)
    if match is None:
        raise ValueError("There is no title in markdown")
    return match.group(0).lstrip("# ")
