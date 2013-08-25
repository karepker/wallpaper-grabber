#! /usr/bin/python3

"""
Grabs the bing image of the day at given resolution
"""

__author__ = "karepker@gmail.com (Kar Epker)"
__copyright__ = "2013 Kar Epker (karepker@gmail.com)"

import itertools
import re
import urllib.parse
import urllib.request

from wallpaper_grabber import WallpaperGrabber

class BingGrabber(WallpaperGrabber):
    """
    A class that gets the picture of the day from Bing
    """

    def __init__(self, **options):
        self.REQUEST_PARAMS = {'format': 'xml', 'idx': 0, 'mkt': 'en-US', 
            'n': 1}
        self.REQUEST_BASE_URL = 'http://www.bing.com/HPImageArchive.aspx'
        self.IMAGE_DOMAIN = 'http://www.bing.com'
        self.DEFAULT_IMAGE_SIZE = (1920, 1080)
        self.image_size = (options['size'] if 'size' in options else
            self.DEFUALT_IMAGE_SIZE)
        self.IMAGE_EXT = '.jpg'
        self.NAME = 'bing'
        super().__init__(self.IMAGE_EXT, self.NAME)

    def get_page(self):
        """
        Gets the data from the page

        Yields:
            URLs (strings) of images to be retrieved
            
        Raises: 
            urllib.error.URLError: Couldn't find the feed URL
        """
        # make the request to get the page
        request_params_string = urllib.parse.urlencode(self.REQUEST_PARAMS)
        request_url = self.REQUEST_BASE_URL + '?' + request_params_string
        response = urllib.request.urlopen(request_url).read().decode('utf-8')

        # find the image urls with a regex
        image_matches = re.findall(r'.*\<image\>.*\<urlBase\>(\S+)'
            r'\<\/urlBase\>.*\<\/image\>.*', response, re.MULTILINE)
        image_size_string = "_%sx%s" % (self.image_size)

        # yield all images found
        for image_base_url in image_matches:
            yield (self.IMAGE_DOMAIN + image_base_url + image_size_string + 
                self.IMAGE_EXT)
