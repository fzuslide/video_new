#coding=utf-8

import urllib
from BeautifulSoup import BeautifulSoup

from flask import Module, render_template

spider = Module(__name__, url_prefix='')

VIDEO_LIST_LIMIT = 35


class Parser(object):

    def __init__(self):
        self.video_sites = {}

    
    def open(self, url):
        resp = urllib.urlopen(url)
        if resp.code == 200:
            return resp.read()
        return ''

    def process_tom365(self):
        try:
            url = 'http://www.tom365.com/'
            url_prefix = 'http://www.tom365.com/'
            content = self.open(url)
            if not content:
                return None

            soup = BeautifulSoup(content)
            new_div = soup.findAll(id='new')[0]
            li_list = new_div.findAll('li')
            video_list = []
            for li in li_list:
                video_list.append([li.a.text, url_prefix + li.a['href'],  li.em.string])
            self.video_sites[url] = video_list[:VIDEO_LIST_LIMIT]
        except:
            import traceback; traceback.print_exc()
            pass

    def process_2kk(self):
        try:
            url = 'http://www.2kk.cc/'
            url_prefix = 'http://www.2kk.cc'
            content = self.open(url)
            if not content:
                return None

            soup = BeautifulSoup(content)
            new_div = soup.findAll('div', {"class": "navType2 c_b"})[1]
            li_list = new_div.findAll('li')
            video_list = []
            for li in li_list:
                video_list.append([li.a['title'], url_prefix + li.a['href'],  li.b.string])
            self.video_sites[url] = video_list[:VIDEO_LIST_LIMIT]
        except:
            import traceback; traceback.print_exc()
            pass

    def process_an80(self):
        try:
            url = 'http://www.an80.org/'
            url_prefix = 'http://www.an80.org'
            content = self.open(url)
            content = content.decode('gbk')
            if not content:
                return None

            soup = BeautifulSoup(content)
            new_ul = soup.findAll('ul', {"class": "movie_index_list"})[0]
            li_list = new_ul.findAll('li')
            video_list = []
            for li in li_list:
                video_list.append([li.a.text, url_prefix + li.a['href'],  li.font.text])
            self.video_sites[url] = video_list[:VIDEO_LIST_LIMIT]
        except:
            import traceback; traceback.print_exc()
            pass


    def process_maku(self):
        try:
            url = 'http://www.maku.cc/'
            url_prefix = 'http://www.maku.cc'
            content = self.open(url)
            content = content.decode('gbk')
            if not content:
                return None

            soup = BeautifulSoup(content)
            new_div = soup.findAll('div', id="right")[0]
            li_list = new_div.div.findAll('li')
            video_list = []
            for li in li_list:
                video_list.append([li.a['title'], url_prefix + li.a['href'],  li.span.text])
            self.video_sites[url] = video_list[:VIDEO_LIST_LIMIT]
        except:
            import traceback; traceback.print_exc()
            pass



    def process_3gdyy(self):
        try:
            url = 'http://www.3gdyy.cc/'
            url_prefix = 'http://www.3gdyy.cc'
            content = self.open(url)
            if not content:
                return None

            soup = BeautifulSoup(content)
            new_ul = soup.findAll('ul')[3]
            li_list = new_ul.findAll('li')
            video_list = []
            for li in li_list:
                a = li.findAll('a')[1]
                video_list.append([a['title'], url_prefix + a['href'],  li.span.font.text])
            self.video_sites[url] = video_list[:VIDEO_LIST_LIMIT]
        except:
            import traceback; traceback.print_exc()
            pass

    def process_8090kk(self):
        try:
            url = 'http://www.8090kk.com/index.php?s=ajax-show.html'
            url_prefix = 'http://www.8090kk.com'
            content = self.open(url)
            if not content:
                return None

            soup = BeautifulSoup(content)
            new_div = soup.findAll('div', id="div_2")[3]
            li_list = new_div.findAll('li')
            video_list = []
            for li in li_list:
                a = li.findAll('a')[1]
                date = li.text.split('] [')[0][1:]
                video_list.append([a.text, url_prefix + a['href'],  date])
            self.video_sites[url] = video_list[:VIDEO_LIST_LIMIT]
        except:
            import traceback; traceback.print_exc()
            pass

    def process_uobb(self):
        try:
            url = 'http://www.uobb.net/'
            url_prefix = 'http://www.uobb.net/'
            content = self.open(url)
            content = content.decode('gbk')
            if not content:
                return None

            soup = BeautifulSoup(content)
            new_div = soup.findAll('div', {"class":"left_box8"})[0]
            li_list = new_div.findAll('li')
            video_list = []
            for li in li_list:
                a = li.findAll('a')[1]
                date = ''
                video_list.append([a['title'], url_prefix + a['href'],  date])
            self.video_sites[url] = video_list[:VIDEO_LIST_LIMIT]
        except:
            import traceback; traceback.print_exc()
            pass 

    def process_uobb(self):
        try:
            url = 'http://www.uobb.net/'
            url_prefix = 'http://www.uobb.net/'
            content = self.open(url)
            content = content.decode('gbk')
            if not content:
                return None

            soup = BeautifulSoup(content)
            new_div = soup.findAll('div', {"class":"left_box8"})[0]
            li_list = new_div.findAll('li')
            video_list = []
            for li in li_list:
                a = li.findAll('a')[1]
                date = ''
                video_list.append([a['title'], url_prefix + a['href'],  date])
            self.video_sites[url] = video_list[:VIDEO_LIST_LIMIT]
        except:
            import traceback; traceback.print_exc()
            pass


    def process_3gyys(self):
        try:
            url = 'http://www.3gyys.com/ajax-show.html'
            url_prefix = 'http://www.3gyys.com'
            content = self.open(url)
            if not content:
                return None

            soup = BeautifulSoup(content)
            new_div = soup.findAll('div', {"class": "ajaxnew"})[0]
            li_list = new_div.findAll('li')
            video_list = []
            for li in li_list:
                a = li.findAll('a')[1]
                date = li.text.split('[')[2][:-1]
                video_list.append([a.text, url_prefix + a['href'],  date])
            self.video_sites[url] = video_list[:VIDEO_LIST_LIMIT]
        except:
            import traceback; traceback.print_exc()
            pass

    def process_7788dy(self):
        try:
            url = 'http://www.7788dy.com/'
            url_prefix = 'http://www.7788dy.com'
            content = self.open(url)
            if not content:
                return None

            soup = BeautifulSoup(content)
            td_list = soup.findAll('td', {"class":"tabb", "width": "100%", "colspan": "2"})
            video_list = []
            for td in td_list:
                li_list = td.div.ul.findAll('li')
                for li in li_list:
                    font = li.div.findAll('font', color="#ff0000")
                    if font:
                        date = font[0].text.split(']')[0][1:]
                    else:
                        date = li.div.text.split(']')[0][1:]
                    video_list.append([li.div.a.text.split('(')[0], li.div.a['href'], date])
            self.video_sites[url] = video_list[:VIDEO_LIST_LIMIT]
        except:
            import traceback; traceback.print_exc()
            pass



    def process_hao41(self):
        try:
            url = 'http://www.hao41.com/'
            url_prefix = 'http://www.hao41.com'
            content = self.open(url)
            content = content.decode('gbk')
            if not content:
                return None

            soup = BeautifulSoup(content)
            new_div =  soup.findAll('div', {"class": "hbd12 ssv"})[0]
            video_list = []
            li_list = new_div.findAll('li')
            for li in li_list:
                video_list.append([li.a['title'], li.a['href'], li.span.text])
            self.video_sites[url] = video_list[:VIDEO_LIST_LIMIT]
        except:
            import traceback; traceback.print_exc()
            pass


@spider.route('/')
def list_new_video():
    parser = Parser()
    parser.process_tom365()
    parser.process_2kk()
    parser.process_an80()
    parser.process_maku()
    parser.process_3gdyy()
    parser.process_8090kk()
    parser.process_uobb()
    parser.process_3gyys()
    parser.process_7788dy()
    parser.process_hao41()
    return render_template('list_new_video.html', video_sites=parser.video_sites) 
