from leafnode import LeafNode
from texttype import TextType


class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str = "") -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, value) -> bool:
        return (
            self.text == value.text
            and self.text_type == value.text_type
            and self.url == value.url
        )

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

    def create_htmlLeafNode(self) -> LeafNode:
        props = {}
        if self.text_type == TextType.LINK:
            props["href"] = self.url
        if self.text_type == TextType.IMAGE:
            props["src"] = self.url
            props["alt"] = self.text

        return LeafNode(self.text_type.get_html_code(), self.text)
