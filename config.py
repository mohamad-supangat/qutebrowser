# import dracula.draw

# Load existing settings made via :set
config.load_autoconfig()

dracula.draw.blood(c, {
    'spacing': {
        'vertical': 1,
        'horizontal': 2
    }
})

c.aliases = {
    'q': 'close',
    'qa': 'quit',
    'w': 'session-save',
    'wq': 'quit --save',
    'wqa': 'quit --save',
    'bitwarden': 'spawn --userscript qute-bitwarden'
}

c.auto_save.session = True
config.set('content.cookies.accept', 'all', 'chrome-devtools://*')
c.content.geolocation = False
c.content.autoplay  = False


# adblock
c.content.blocking.enabled  = True
c.content.blocking.hosts.block_subdomains = True
c.content.blocking.method = 'hosts'

c.content.blocking.hosts.lists = [
    'https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts',
    'https://pgl.yoyo.org/adservers/serverlist.php?hostformat=hosts&showintro=1&mimetype=plaintext&_=223428',
    'https://adaway.org/hosts.txt',
    'https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-gambling-porn-social/hosts',
]
c.content.blocking.adblock.lists = ['https://easylist.to/easylist/easylist.txt', 'https://easylist.to/easylist/easyprivacy.txt', 'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters.txt', 'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2021.txt', 'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/legacy.txt', 'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/privacy.txt', 'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/badware.txt', 'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/resource-abuse.txt', 'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/unbreak.txt', 'https://raw.githubusercontent.com/brave/adblock-lists/master/brave-lists/brave-social.txt']

# download manager
c.downloads.position = 'bottom'
c.downloads.location.remember = False
c.downloads.location.suggestion = "both"
c.downloads.remove_finished = 5000

config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}', 'https://web.whatsapp.com/')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:90.0) Gecko/20100101 Firefox/90.0', 'https://accounts.google.com/*')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99 Safari/537.36', 'https://*.slack.com/*')

config.set('content.images', True, 'chrome-devtools://*')
config.set('content.images', True, 'devtools://*')


c.content.pdfjs = True


c.editor.command = ['alacritty', '-e', 'nvim', '{file}']
c.fileselect.single_file.command = ['alacritty', '-e', 'ranger', '--choosefile={}']
c.fileselect.multiple_files.command = ['alacritty', '-e', 'ranger', '--choosefiles={}']
c.fileselect.folder.command = ['alacritty', '-e', 'ranger', '--choosedir={}']
c.input.insert_mode.auto_load = True
c.scrolling.smooth = True


c.statusbar.show = 'always'
c.statusbar.position = 'bottom'
c.statusbar.widgets = ['progress', 'keypress', 'url', 'scroll', 'history', 'tabs']
c.tabs.favicons.show = 'always'
c.tabs.background = True
c.tabs.last_close = 'ignore'
c.tabs.position = 'top'
c.tabs.show = 'multiple'


c.url.start_pages = 'https://google.com'

## Dark Mode
c.colors.webpage.preferred_color_scheme = 'dark'
c.colors.webpage.darkmode.enabled = True
c.colors.webpage.darkmode.policy.images = 'never'


c.fonts.default_family = 'Iosevka'
c.url.default_page = "https://google.com"

## Search Enginge
c.url.searchengines = {"DEFAULT": "https://google.com/search?q={}"}
c.url.searchengines['a'] = 'https://wiki.archlinux.org/?search={}'
c.url.searchengines['g'] = 'http://www.google.com/search?hl=en&source=hp&ie=ISO-8859-l&q={}'
c.url.searchengines['y'] = 'https://www.youtube.com/results?search_query={}'
c.url.searchengines['gh'] = 'https://github.com/search?q={}'



# Spawn with URL
config.bind('x', 'spawn l -u {url}')
config.bind('X', 'hint links spawn -u {hint-url}')


