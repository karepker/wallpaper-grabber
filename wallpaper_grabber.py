#! /usr/bin/python3

"""
Contains the WallpaperGetter base class
"""

__author__ = "karepker@gmail.com (Kar Epker)"
__copyright__ = "2013 Kar Epker (karepker@gmail.com)"

import datetime
import itertools
import os
import urllib.request

class WallpaperGrabber:
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
        # make directory for specific grabber if it doesn't exist
        grabber_directory = os.path.join(directory, self.name)
        if (not os.path.exists(grabber_directory) or not
                os.path.isdir(grabber_directory)):
            os.mkdirs(directory)

        # save each of the images found
        for image_url in self.get_page():
            # determine an image name 
            today_string = datetime.datetime.today().strftime('%Y-%m-%d')
            for i in itertools.count(start=0):
                image_name = '%s %d%s' % (today_string, i, self.IMAGE_EXT)
                full_path = os.path.join(grabber_directory, image_name)
                if not os.path.exists(full_path):
                    # get and save image
                    urllib.request.urlretrieve(image_url, full_path)
                    break
