from dataclasses import dataclass

@dataclass
class Service():
    title: str
    url: str
    interval: int