import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('http://www.cel.ro/casti/casti-serioux-srxs_h350v-pNyMxND0-l/')
soup = bs.BeautifulSoup(sauce, 'lxml')
print(soup.find_all('p'))