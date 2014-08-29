# coding=utf-8
import re
import threading
import urllib2
from django.utils.text import slugify
from bs4 import BeautifulSoup

LANG = 'python'
if LANG == 'java':
    COMMENT_MARK = '//'
    FILE_EXT = 'java'
else:
    COMMENT_MARK = '#'
    FILE_EXT = 'py'


class DownloadThread(threading.Thread):

    def __init__(self, tr):
        threading.Thread.__init__(self)
        self.tr = tr

    def run(self):
        tr = self.tr
        a = tr.find_all('a')[0]
        rate = tr.find_all('td')[3].text
        name, url = slugify(a.text).replace('-', '_'), a['href']
        print name, url
        if url == '#':
            return
        with open(LANG + '/' + name + '.' + FILE_EXT, 'wb') as pyfile:
            subps_html = urllib2.urlopen(
                "https://oj.leetcode.com" + url).read()
            subps = BeautifulSoup(subps_html)
            res = [COMMENT_MARK + ' AC Rate: ' + rate.encode('utf-8'),
                COMMENT_MARK + ' SOURCE URL: https://oj.leetcode.com' + url.encode('utf-8')]
            subps = BeautifulSoup(subps_html)
            for i in subps.find_all('div', class_='question-content')[0].text.split('\n'):
                res.append(COMMENT_MARK + ' %s' % i.encode('utf-8'))

            codes = re.findall(
                r'scope\.code\.' + LANG + ' \= \'(.*?)\'', subps_html)
            res.append(
                '\n\n' + codes[0].replace('\\u000D\\u000A', '\n')
                .replace('\u003C', '<')
                .replace('\u003E', '>')
                .replace('\u003D', '=')
                .replace('\u002D', '-'))
            pyfile.write('\n'.join(res))


ps = urllib2.urlopen("https://oj.leetcode.com/problems/").read()
ps = BeautifulSoup(ps)
ts = []
for tr in ps.find_all('table')[1].find_all('tr'):
    if len(tr.find_all('td')) == 4:
        t = DownloadThread(tr)
        ts.append(t)
        t.start()


for t in ts:
    t.join()
