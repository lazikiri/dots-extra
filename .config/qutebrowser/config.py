c = c
config = config

# Load config in browser
config.load_autoconfig()

# Block third party cookies
c.content.cookies.accept = 'no-3rdparty'
# Uncomment the line below to delete cookies at the end of sessions
# c.content.cookies.store = False

# Uncomment the line below to disable javascript globally
# c.content.javascript.enabled = False

# Privacy stuff
c.content.webgl = False
c.content.canvas_reading = False
c.content.geolocation = False
c.content.autoplay = False
c.content.dns_prefetch = False
c.content.hyperlink_auditing = False
c.content.webrtc_ip_handling_policy = 'disable-non-proxied-udp'

# User agent spoofing
c.content.headers.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.3'
c.content.headers.accept_language = 'en-US,en;q=0.5'
c.content.headers.custom = {'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}

# Ad blocking (install python-adblock package)
c.content.blocking.enabled = True
c.content.blocking.method = 'both'
c.content.blocking.adblock.lists = [
    "https://easylist.to/easylist/easylist.txt",
    "https://easylist.to/easylist/easyprivacy.txt",
    "https://easylist.to/easylist/fanboy-social.txt"
]

# Dark mode
c.colors.webpage.darkmode.enabled = True
c.colors.webpage.preferred_color_scheme = 'dark'

# Search engines
c.url.searchengines = {
    'DEFAULT': 'https://duckduckgo.com/?q={}',
    '!aw': 'https://wiki.archlinux.org/?q={}'
}

# Binds
config.bind('<Escape>', 'mode-leave ;; jseval -q document.activeElement.blur()', mode='insert')
