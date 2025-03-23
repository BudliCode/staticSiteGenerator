from typing import Dict
import htmlnode
from texttype import TextType


class LeafNode(htmlnode.HTMLNode):
    def __init__(self, tag: str, value: str, props: Dict[str, str] = {}) -> None:
        super().__init__(tag, value=value, props=props)

    def to_html(self):
        if self.value == "" and self.tag != TextType.IMAGE:
            raise ValueError("LeafNode needs an value")

        if len(self.children) != 0:
            raise ValueError("LeafNode is not supposed to have children")
        if self.tag == "":
            return self.value

        return super().to_html()
