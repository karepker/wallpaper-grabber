#! /usr/bin/python3

"""
Usage of wallpaper grabbers
"""

__author__ = "karepker@gmail.com (Kar Epker)"
__copyright__ = "2013 Kar Epker (karepker@gmail.com)"

import argparse

from bing_grabber import BingGrabber
from national_geographic_grabber import NationalGeographicGrabber

# dict of grabber name to grabber
# specify grabbers in `grabbers` argument by their names given here
GRABBERS = {
    'bing': BingGrabber,
    'natgeo': NationalGeographicGrabber
}

def make_size_tuple(to_convert):
    """
    Makes a size tuple from the given string
    
    Args:
        to_convert (string): A string of the form "width,height" to convert

    Returns:
        A tuple of the form (width, height)
    """
    return tuple(int(i) for i in to_convert.split(',', 1))


if __name__ == '__main__':
    # set up arguments
    parser = argparse.ArgumentParser(description='Download daily wallpapers')
    parser.add_argument('grabbers', help='Which grabbers to run, choices: %s' 
        % (', '.join(list(GRABBERS.keys()))), type=lambda x: x.split(','))
    parser.add_argument('--size', '-s',  help='Size of images to grab '
        '(when available)', type=make_size_tuple, default="1920,1080")
    parser.add_argument('--base_dir', '-b', help='Where to save images',
        type=str, default='/tmp')
    args = parser.parse_args()

    # create the grabbers
    grabbers = []
    for grabber in args.grabbers:
        grabbers.append(GRABBERS[grabber](size=args.size))

    # save images
    for grabber in grabbers:
        grabber.save_images(args.base_dir)
