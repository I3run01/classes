import urllib
import urllib.request

try:
    urllib.request.urlopen('http://www.pudim.com.br/')
    print('\033[1;32mSite acessivel\033[m')
except:
    print('	\033[1;31mSite não acessível\033[m')
