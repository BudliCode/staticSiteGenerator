from typing import Dict, List, Self


class HTMLNode:
    def __init__(
        self,
        tag: str,
        value: str = "",
        children: List = list(),
        props: Dict[str, str] = dict(),
    ) -> None:
        self.tag: str = tag
        self.value: str = value
        self.children: List[Self] = children
        self.props: Dict[str, str] = props

    def to_html(self):
        children_html = ""
        for c in self.children:
            children_html += c.to_html()
        return f"<{self.tag}{self.props_to_html()}>{self.value}{children_html}</{self.tag}>"

    def props_to_html(self) -> str:
        return "".join(map(lambda x: f' {x[0]}="{x[1]}"', self.props.items()))

    def __repr__(self) -> str:
        return f"HTMLNode:\n  tag: {self.tag}\n  value: {self.value}\n  children: {self.children}\n  props: {self.props_to_html()}"
