from dataclasses import dataclass

@dataclass
class User:
    user_name: str
    apps: list[str]