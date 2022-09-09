from data_types.web_account import Web_Account

def test_web_account_instantiation():
    nss = Web_Account(
        'https://negativespacesounds.com/',
        "Negative Space Sounds",
        )
    assert nss.root_url == 'https://negativespacesounds.com/'
    assert nss.site_name == 'Negative Space Sounds'