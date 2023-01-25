# import dracula.draw
# from theme import tampilan
# tampilan(c)
# Load existing settings made via :set
config.load_autoconfig()

# dracula.draw.blood(c, {
#     'spacing': {
#         'vertical': 1,
#         'horizontal': 2
#     }
# })
#


c.auto_save.session = True
c.session.lazy_restore = True
c.completion.shrink = True
c.completion.use_best_match = True
c.content.notifications.presenter = "libnotify"
c.content.fullscreen.window = True
c.content.geolocation = False
c.content.autoplay = False


# adblock
c.content.blocking.enabled = True
c.content.blocking.hosts.block_subdomains = True
c.content.blocking.method = "both"
c.content.tls.certificate_errors = "block"

c.content.blocking.hosts.lists = [
    "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts",
    # 'https://pgl.yoyo.org/adservers/serverlist.php?hostformat=hosts&showintro=1&mimetype=plaintext&_=223428',
    "https://adaway.org/hosts.txt",
    # 'https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-gambling-porn-social/hosts',
]
c.content.blocking.adblock.lists = [
    "https://easylist.to/easylist/easylist.txt",
    "https://easylist.to/easylist/easyprivacy.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2021.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/legacy.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/privacy.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/badware.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/resource-abuse.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/unbreak.txt",
    "https://raw.githubusercontent.com/brave/adblock-lists/master/brave-lists/brave-social.txt",
]

# download manager
c.downloads.position = "bottom"
c.downloads.location.remember = True
c.downloads.location.suggestion = "both"
c.downloads.remove_finished = 30000


#  ╭──────────────────────────────────────────────────────────╮
#  │ Useragent for mobile view and desktop                    │
#  ╰──────────────────────────────────────────────────────────╯
desktop_ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15"

mobile_ua = "Mozilla/5.0 (X11; CrOS aarch64 15183.59.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.75 Safari/537.36"
# config.set('content.headers.user_agent', old_chrome_ua, 'steamdb.info')
# config.set('content.headers.user_agent', old_chrome_ua, 'www.nginx.com')
# config.set('content.headers.user_agent', old_chrome_ua, 'gitlab.com/users/sign_in')

mobile_url = ["facebook.com", "x.facebook.com", "www.facebook.com", "m.facebook.com"]
for url in mobile_url:
    config.set("content.headers.user_agent", mobile_ua, url)
config.set("content.headers.user_agent", desktop_ua, "global")

config.set("content.images", True, "chrome-devtools://*")
config.set("content.cookies.accept", "all", "chrome-devtools://*")
config.set("content.images", True, "devtools://*")


c.content.pdfjs = True


c.editor.command = ["alacritty", "-e", "nvim", "{file}"]
c.fileselect.single_file.command = ["alacritty", "-e", "ranger", "--choosefile={}"]
c.fileselect.multiple_files.command = ["alacritty", "-e", "ranger", "--choosefiles={}"]
c.fileselect.folder.command = ["alacritty", "-e", "ranger", "--choosedir={}"]
c.input.insert_mode.auto_load = False
c.scrolling.smooth = True


c.statusbar.show = "always"
c.statusbar.position = "bottom"
c.statusbar.widgets = ["progress", "keypress", "url", "scroll", "history", "tabs"]
c.tabs.favicons.show = "always"
c.tabs.background = True
c.tabs.last_close = "ignore"
c.tabs.position = "top"
c.tabs.show = "multiple"
c.tabs.favicons.scale = 0.8
c.tabs.indicator.width = 10


c.url.start_pages = str("~/.config/qutebrowser/startpage/index.html")

# Dark Mode
c.colors.webpage.preferred_color_scheme = "dark"
# c.colors.webpage.darkmode.enabled = True
c.colors.webpage.darkmode.policy.images = "never"


c.fonts.default_family = "Iosevka"
c.url.default_page = c.url.start_pages

# Search Enginge
c.url.searchengines = {
    "DEFAULT": "https://google.com/search?q={}",
    "a": "https://wiki.archlinux.org/?search={}",
    "g": "http://www.google.com/search?hl=en&source=hp&ie=ISO-8859-l&q={}",
    "y": "https://invidious.snopyta.org/search?q={}",
    "gh": "https://github.com/search?q={}",
    "gf": "https://greasyfork.org/en/scripts?filter_locale=0&q={}",
    "red": "https://libreddit.spike.codes/r/popular/search?q={}&restrict_sr=on",
    "aur": "https://aur.archlinux.org/packages?O=0&K={}",
    "d": "https://duckduckgo.com/?q={}&hps=1",
    "npm": "https://www.npmjs.com/search?q={}",
    "npms": "https://npms.io/search?q={}",
    "pa": "https://packagist.org/?query={}",
    "fdroid": "https://search.f-droid.org/?q={}",
    "apkmirror": "https://www.apkmirror.com/?s={}",
}


c.qt.environ = {"NODE_PATH": "/home/deve/.local/share/pnpm/global/5/node_modules"}

# Spawn with URL
config.bind("C", "spawn --userscript container-open")
config.bind("<Alt-c>", "set-cmd-text -s :spawn --userscript container-open")
config.bind("<Alt-f>", "hint links userscript container-open")
config.bind("<Alt-b>", "spawn --userscript qute-bitwarden")
config.bind("X", "spawn --userscript add-nextcloud-bookmarks")
config.bind(",dark", "spawn --userscript dark-toogle")


# alias
c.aliases = {
    "q": "close",
    "qa": "quit",
    "w": "session-save",
    "wq": "quit --save",
    "wqa": "quit --save",
    "bitwarden": "spawn --userscript qute-bitwarden",
    "container-open": "spawn --userscript container-open",
    "container-ls": "spawn --userscript container-ls",
    "container-add": "spawn --userscript container-add",
    "container-rm": "spawn --userscript container-rm",
    "nextcloud-bookmarks-import": "spawn --userscript import-nextcloud-bookmarks",
}


config.source("gruvbox.py")
