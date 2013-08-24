#! /usr/bin/python3

"""
Grabs the bing image of the day at given resolution
"""

__author__ = "Kar Epker"

import datetime
import itertools
import os
import re
import sys
import urllib.parse
import urllib.request

class WallpaperGetter:
    """
    A partially abstract class specifying methods for getting wallpapers
    """
    def __init__(self, image_ext, name):
        self.image_ext = image_ext
        self.name = name 

    def get_page(self):
        raise NotImplementedError

    def save_images(self, directory):
        """
        Saves images retrieved from page in specified directory

        Args:
            directory (string): The directory in which to save the images
        """
        for image_url in self.get_page():
            # determine an image name and get the image
            today_string = datetime.datetime.today().strftime('%Y-%m-%d')
            for i in itertools.count(start=0):
                image_name = '%s %d%s' % (today_string, i, self.IMAGE_EXT)
                if not os.path.exists(image_name):
                    directory = os.path.join(directory, self.name)
                    # make directory if it doesn't exist
                    if (not os.path.exists(directory) or not
                            os.path.isdir(directory)):
                        os.mkdirs(directory)
                    # save image
                    full_path = os.path.join(directory, image_name)
                    urllib.request.urlretrieve(image_url, full_path)
                    break


class BingWallpaperGetter(WallpaperGetter):
    """
    A class that gets the picture of the day from Bing
    """

    def __init__(self, **options):
        self.REQUEST_PARAMS = {'format': 'xml', 'idx': 0, 'mkt': 'en-US', 
            'n': 1}
        self.REQUEST_BASE_URL = 'http://www.bing.com/HPImageArchive.aspx'
        self.IMAGE_DOMAIN = 'http://www.bing.com'
        self.image_size = options['size'] if 'size' in options else (1920, 
            1080)
        self.IMAGE_EXT = '.jpg'
        self.NAME = 'bing'
        super().__init__(self.IMAGE_EXT, self.NAME)

    def get_page(self):
        """
        Gets the data from the page

        Raises: urllib.error.URLError if URL doesn't exist
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

    
if __name__ == '__main__':
    b = BingWallpaperGetter(size=(1920, 1080))
    b.save_images('/media/windows/Users/Kar/Pictures/wallpapers/')
