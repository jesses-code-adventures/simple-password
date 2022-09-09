from dataclasses import dataclass, field
from data_types.identity import Identity

@dataclass
class User:
    user_name: str
    identities: list[Identity] = field(default_factory=lambda: [])