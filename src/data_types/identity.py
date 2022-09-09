from dataclasses import dataclass, field
from data_types.web_account import Web_Account

@dataclass
class Identity:
    '''
        An identity can have one email address.
        Allows for people with accounts across many emails.

    '''
    email: str
    name: str
    web_accounts: list[Web_Account] = field(
        default_factory=lambda: [])