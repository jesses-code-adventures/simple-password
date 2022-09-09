from dataclasses import dataclass, field

@dataclass
class Web_Account:
    root_url: str
    site_name: str
    password: str = field(default_factory=lambda: '')