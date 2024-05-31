from typing import Literal, TypedDict


class SystemPrompts(TypedDict):
    html_tailwind: str
    react_tailwind: str
    bootstrap: str
    ionic_tailwind: str
    vue_tailwind: str
    svg: str
    react_antd_tailwind: str


Stack = Literal[
    "html_tailwind",
    "react_tailwind",
    "bootstrap",
    "ionic_tailwind",
    "vue_tailwind",
    "svg",
    "react_antd_tailwind",
]
