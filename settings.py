from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
}

SESSION_CONFIGS = [
    {
        "name": "my_simple_survey",
        "display_name": "調査を作ってみた",
        "num_demo_participants": 1,
        "app_sequence": ["my_survey"],
    },
    {
        "name": "two_four_six_experience",
        "display_name": "2-4-6課題",
        "num_demo_participants": 1,
        "app_sequence": ["two_four", "six_task"],
    }
    #{
    #    'name': 'public_goods',
    #    'display_name': "Public Goods",
    #    'num_demo_participants': 3,
    #    'app_sequence': ['public_goods', 'payment_info'],
    #},
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'i@@dumpd^uk45x91xspsk0y!x5upu85@ok-jf&b3*19^t-^lch'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
