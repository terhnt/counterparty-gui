import sys
from setuptools import setup, find_packages
import counterpartygui

APP_VERSION = "1.0.0"

required_packages = [
    'appdirs',
    'unoparty-cli'
]

setup_options = {
    'name': counterpartygui.APP_NAME,
    'version': counterpartygui.APP_VERSION,
    'author': 'Counterparty/Unoparty Foundation',
    'author_email': 'support@unobtanium.uno',
    'maintainer': 'Andrew K',
    'maintainer_email': 'info@unobtanium.uno',
    'url': 'http://unoparty.io',
    'license': 'MIT',
    'description': 'Unoparty Wallet',
    'long_description': '',
    'keywords': 'unoparty,unobtanium,xup',
    'classifiers': [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Office/Business :: Financial",
        "Topic :: System :: Distributed Computing"
    ],
    'download_url': 'https://github.com/terhnt/unoparty-gui/releases/tag/v' + counterpartygui.APP_VERSION,
    'provides': ['unopartygui'],
    'packages': find_packages(),
    'zip_safe': False,
    'install_requires': required_packages
}

setup(**setup_options)
