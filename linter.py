#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Authors: Luc Bettaieb, Carlos Asmat.
#
# License: MIT
#

"""This module exports the Roslint plugin class."""

from SublimeLinter.lint import Linter, STREAM_STDERR
import os


class Roslint(Linter):
    """Provides an interface to roslint."""
    distro = os.environ["ROS_DISTRO"]
    cmd = ('/opt/ros/{}/lib/roslint/cpplint'.format(distro), '-')
    regex = r'^.+:(?P<line>\d+):\s+(?P<message>.+)\s+\s\[(?P<code>.+)\]\s\[(?P<col>\d+)\]'
    error_stream = STREAM_STDERR
    defaults = {
        'selector': 'source.c++'
    }
