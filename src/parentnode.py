from typing import Dict, List
from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: List, props: Dict[str, str] = {}) -> None:
        super().__init__(tag, "", children, props)

    def to_html(self):
        if self.tag == "":
            raise ValueError("parent node needs an tag")
        if self.value != "":
            raise ValueError("parent node is not supposed to have a value")
        return super().to_html()
