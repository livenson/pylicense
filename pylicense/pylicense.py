#!/usr/bin/env python

""" 
A script for extraction of the license metainformation from the python eggs in the specified folders.
Expects the license information to be present in the distribution's metadata.

BSD License

(c) Ilja Livenson

"""

import pkg_resources
import argparse


def extract_license(egg_folder):
    for i in pkg_resources.find_distributions('eggs'):
        current_egg = '%s' % i
        current_egg_version = None  # it can happen that the license is not there
        for j in i._get_metadata('PKG-INFO'):
            if j.startswith('License:'):
                current_egg_version = j[9:]  # strip the initial License: part
                break
        print '%s, %s' % (current_egg, current_egg_version)


parser = argparse.ArgumentParser(description='Extract license information from the egg files in specified folders.')
parser.add_argument('eggdirs', metavar='eggdir', type=str, nargs='+', help='A path containing python eggs')


def run():
    args = parser.parse_args()
    for eggdir in args.eggdirs:
        extract_license(eggdir)


if __name__ == "__main__":
    run()

