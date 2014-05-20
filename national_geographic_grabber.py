#! /usr/bin/python3

"""
Grabs the National Geographic photo of the day at given resolution
"""

__author__ = "karepker@gmail.com (Kar Epker)"
__copyright__ = "2014 Kar Epker (karepker@gmail.com)"

from wallpaper_grabber import WallpaperGrabber

import re
import urllib.request

class NationalGeographicGrabber(WallpaperGrabber):
    """
    A class that gets the photo of the day from National Geographic
    """

    def __init__(self, **options):
        self.REQUEST_FEED_URL = ('http://feeds.nationalgeographic.com/'
            'ng/photography/photo-of-the-day/')
        self.REQUEST_IMAGE_URL = ('http://images.nationalgeographic.com/'
            'exposure/core_media/ngphoto/image/')
        self.DEFAULT_IMAGE_SIZE = (1920, 1080)
        self.image_size = (options['size'] if 'size' in options else
            self.DEFUALT_IMAGE_SIZE)
        self.IMAGE_EXT = '.jpg'
        self.NAME = 'natgeo'
        super().__init__(self.IMAGE_EXT, self.NAME)

    def get_page(self):
        """
        Gets the data from the page

        Yields:
            URLs (strings) of images to be retrieved
            
        Raises: 
            urllib.error.URLError: Couldn't find the feed URL
        """
        # get the feed page
        request_url = self.REQUEST_FEED_URL 
        try:
            response = urllib.request.urlopen(request_url).read().decode(
                'utf-8')
        except urllib.error.URLError:
            print("Can't establish connection", file=sys.stderr)
            return
        
        # find the latest image URL with a regex
        latest_image = re.search(''.join([self.REQUEST_IMAGE_URL,
            r'(?P<image_id>\d+)_0_\d+x\d+.jpg']), response, re.MULTILINE)

        # replace the resolution in the photo url with the desired resolution
        if latest_image:
            yield ''.join([self.REQUEST_IMAGE_URL, 
                latest_image.group('image_id'), '_0_',
                str(self.DEFAULT_IMAGE_SIZE[0]), 'x',
                str(self.DEFAULT_IMAGE_SIZE[1]), '.jpg'])

        return
