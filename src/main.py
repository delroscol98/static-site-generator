from textnode import TextNode, TextType


def main():
    print("Hello world!")

    dummy2 = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")

    print(dummy2)


main()
