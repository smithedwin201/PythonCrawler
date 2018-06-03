import string
from urllib import request
from urllib.parse import quote


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
     #防止特殊字符，其实不加也能跑
     #   url_ = quote(url, safe=string.printable)
     #    response = request.urlopen(url_)
        response = request.urlopen(url)
        if response.getcode() != 200:
            return None

        return response.read()
