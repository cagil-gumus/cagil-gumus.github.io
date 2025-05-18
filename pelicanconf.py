AUTHOR = 'Çağıl Gümüş'
SITENAME = 'Çağıl Gümüş Blog'
SITEURL = "https://cagil-gumus.github.io/"

PATH = "content"

THEME = 'themes/Pelican-Cid'

STATIC_PATHS = ['images', 'cv']

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

USE_CUSTOM_MENU = True
CUSTOM_MENUITEMS = (('About Me', 'pages/about'),)
CONTACTS = (("DESY-GitLab", "https://gitlab.desy.de/cagil.guemues"),
            ("GitHub", "https://github.com/cagil-gumus"),
            ("YouTube", "https://www.youtube.com/@CaglGumus"),
            ("SoundCloud", "https://soundcloud.com/cagilgumus"))

STATIC_PATHS = ['images', 'cv', 'FPGA/images']
