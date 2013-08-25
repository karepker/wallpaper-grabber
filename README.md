# Overview
This module provides framework and functionality for downloading pictures of the day from various sources. It is implemented with Python 3.

# Compatibility
This script has been tested on GNU/Linux, but should be compatible with Python 3 installations on all platforms. Note that the `usage_example.py` script is unlikely to work on platforms that do not use the directory `/tmp`.

# Usage
Run `python3 grab.py --help`. Read the arguments and choose appropriate values. For example, I might run `python3 grab.py 'bing' --size '1920,1080' --base_dir '/home/karepker/Pictures/wallpapers'`.

# Structure
`wallpaper_grabber.py` provides a base class for individual wallpaper grabbers to implement. Other files, named as `xxx_grab.py` provide functionality for grabbing images from specific sources. 

# Copyright and License
Copyright (C) 2013 Kar Epker (karepker@gmail.com)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see http://www.gnu.org/licenses/.
