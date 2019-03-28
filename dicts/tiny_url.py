import urlparse, urllib
import hashlib

class Codec:

    def __init__(self):
        self.urldict = {}
        
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        
        md5sum_url = hashlib.md5(longUrl.encode()).hexdigest()
        parse_result = urlparse.urlsplit(longUrl)
        
        self.urldict[longUrl] = "http://tinyurl.com/{0}".format(md5sum_url)
        
        return self.urldict[longUrl]

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        
        for k,v in self.urldict.iteritems():
            if v == shortUrl:
                return k

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
