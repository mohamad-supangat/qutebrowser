# import dracula.draw
from theme import tampilan
tampilan(c)
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
c.content.geolocation = False
c.content.autoplay  = False


# adblock
c.content.blocking.enabled  = True
c.content.blocking.hosts.block_subdomains = True
c.content.blocking.method = 'both'
c.content.tls.certificate_errors = 'block'

c.content.blocking.hosts.lists = [
    'https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts',
    # 'https://pgl.yoyo.org/adservers/serverlist.php?hostformat=hosts&showintro=1&mimetype=plaintext&_=223428',
    'https://adaway.org/hosts.txt',
    # 'https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-gambling-porn-social/hosts',
]
c.content.blocking.adblock.lists = ['https://easylist.to/easylist/easylist.txt',
                                    'https://easylist.to/easylist/easyprivacy.txt',
                                    'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters.txt',
                                    'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2021.txt',
                                    'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/legacy.txt',
                                    'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/privacy.txt',
                                    'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/badware.txt',
                                    'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/resource-abuse.txt',
                                    'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/unbreak.txt',
                                    'https://raw.githubusercontent.com/brave/adblock-lists/master/brave-lists/brave-social.txt']

# download manager
c.downloads.position = 'bottom'
c.downloads.location.remember = False
c.downloads.location.suggestion = "both"
c.downloads.remove_finished = 30000

config.set('content.headers.user_agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36', 'global')

config.set('content.images', True, 'chrome-devtools://*')
config.set('content.cookies.accept', 'all', 'chrome-devtools://*')
config.set('content.images', True, 'devtools://*')



c.content.pdfjs = True


c.editor.command = ['alacritty', '-e', 'nvim', '{file}']
c.fileselect.single_file.command = ['alacritty', '-e', 'ranger', '--choosefile={}']
c.fileselect.multiple_files.command = ['alacritty', '-e', 'ranger', '--choosefiles={}']
c.fileselect.folder.command = ['alacritty', '-e', 'ranger', '--choosedir={}']
c.input.insert_mode.auto_load = False
c.scrolling.smooth = True


c.statusbar.show = 'always'
c.statusbar.position = 'bottom'
c.statusbar.widgets = ['progress', 'keypress', 'url', 'scroll', 'history', 'tabs']
c.tabs.favicons.show = 'always'
c.tabs.background = True
c.tabs.last_close = 'ignore'
c.tabs.position = 'top'
c.tabs.show = 'multiple'
c.tabs.favicons.scale = 0.8
c.tabs.indicator.width = 10




c.url.start_pages = str('~/.config/qutebrowser/startpage/index.html')

## Dark Mode
c.colors.webpage.preferred_color_scheme = 'dark'
# c.colors.webpage.darkmode.enabled = True
c.colors.webpage.darkmode.policy.images = 'never'


c.fonts.default_family = 'Iosevka'
c.url.default_page = c.url.start_pages

## Search Enginge
c.url.searchengines = {"DEFAULT": "https://google.com/search?q={}"}
c.url.searchengines['a'] = 'https://wiki.archlinux.org/?search={}'
c.url.searchengines['g'] = 'http://www.google.com/search?hl=en&source=hp&ie=ISO-8859-l&q={}'
c.url.searchengines['y'] = 'https://www.youtube.com/results?search_query={}'
c.url.searchengines['gh'] = 'https://github.com/search?q={}'
c.url.searchengines['red'] = 'https://libredd.it/r/popular/search?q={}&restrict_sr=on'
c.url.searchengines['aur'] = 'https://aur.archlinux.org/packages?O=0&K={}'
c.url.searchengines['d'] = 'https://duckduckgo.com/?q={}&hps=1'




# Spawn with URL
config.bind('C','spawn --userscript container-open')
config.bind('<Alt-c>','set-cmd-text -s :spawn --userscript container-open')
config.bind('<Alt-f>','hint links userscript container-open')
config.bind('<Alt-b>','spawn --userscript qute-bitwarden')
config.bind('X', 'spawn --userscript add-nextcloud-bookmarks')
config.bind(',dark', 'spawn --userscript dark-toogle')


## alias
c.aliases = {
    'q': 'close',
    'qa': 'quit',
    'w': 'session-save',
    'wq': 'quit --save',
    'wqa': 'quit --save',
    'bitwarden': 'spawn --userscript qute-bitwarden'
}
c.aliases['container-open'] = 'spawn --userscript container-open'
c.aliases['container-ls'] = 'spawn --userscript container-ls'
c.aliases['container-add'] = 'spawn --userscript container-add'
c.aliases['container-rm'] = 'spawn --userscript container-rm'
c.aliases['nextcloud-bookmarks-import'] = 'spawn --userscript import-nextcloud-bookmarks'


