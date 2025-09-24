c = c
config = config
config.load_autoconfig()


# Search engines
c.url.searchengines = {
    'DEFAULT': 'https://duckduckgo.com/?q={}',
    '!aw': 'https://wiki.archlinux.org/?search={}'
}

# Disable autoplay
c.content.autoplay = False

# Enable blocking and tracker blocking
c.content.blocking.enabled = True

# Enable brave adblocker, install python-adblock package
c.content.blocking.method = 'both'

# Disables webgl
c.content.webgl = False

# Disables canvas
c.content.canvas_reading = False

# Sets useragent to Firefox on Windows
c.content.headers.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.3'

# Set accept language header
c.content.headers.accept_language = 'en-US,en;q=0.5'
c.content.headers.custom = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}

# Adblock lists
c.content.blocking.adblock.lists = [
    "https://easylist.to/easylist/easylist.txt",
    "https://easylist.to/easylist/easyprivacy.txt",
    "https://easylist.to/easylist/fanboy-social.txt",
]

# Disable geolocation
c.content.geolocation = False

# Cookie acceptance policy
c.content.cookies.accept = 'no-3rdparty'

# Disable DNS prefetching
c.content.dns_prefetch = False

# Enables darkmode
c.colors.webpage.darkmode.enabled = True
