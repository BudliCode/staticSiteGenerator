from enum import Enum


class TextType(Enum):
    TEXT = "text"
    BOLD = "bond"
    ITALIC = "image"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

    def get_html_code(self):
        match self:
            case self.TEXT:
                return ""
            case self.BOLD:
                return "b"
            case self.ITALIC:
                return "i"
            case self.CODE:
                return "code"
            case self.LINK:
                return "a"
            case self.IMAGE:
                return "img"
