from urllib import request,parse
from html.parser import HTMLParser
from html.entities import name2codepoint

class myqiushibaike(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.CurrentData = ''
        self.content = False

    def handle_starttag(self, tag, attrs):
        if tag != 'p':
            self.CurrentData = tag

        if self.CurrentData == 'div':
            for k, v in attrs:
                print(k, v)
                if v == 'countent':
                    self.CurrentData = 'content'
    def handle_endtag(self, tag):
        if tag == 'div':
            self.content = False
            self.CurrentData = ''

    def handle_data(self, data):
        if self.CurrentData == 'content':
            print('content:', content)
        elif self.CurrentData == 'username':
            print('usename:', data)
    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

def requesturl(url):
    req = request.Request(url)
    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')

    # 获取html返回值
    with request.urlopen(req) as f:
        data = f.read().decode('utf-8')
    return data;

if __name__ == '__main__':
    parser = myqiushibaike();
    url = 'http://www.qiushibaike.com/';
    parser.feed(requesturl(url))
