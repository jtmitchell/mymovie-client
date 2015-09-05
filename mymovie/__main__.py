#!/usr/bin/env python
# encoding: utf-8
'''
__main__ -- Main entry point for client to query movies and save favourites to MyMovie

__main__ is a client for MyMovie

@author:     James Mitchell

@copyright:  2015 James Mitchell. All rights reserved.

@license:    GPLv2

@contact:    james.mitchell@maungawhau.net.nz
@deffield    updated: 2015-08-10
'''

from optparse import OptionParser
import os
import sys

from . import __version__, __author__

__all__ = []

DEBUG = 1
TESTRUN = 0
PROFILE = 0


def main(argv=None):
    '''Command line options.'''

    program_name = os.path.basename(sys.argv[0])
    program_version = __version__

    program_version_string = '%%prog %s'.format(program_version)
    program_longdesc = ''''''  # optional - give further explanation about what the program does
    program_license = "Copyright 2015 {0}".format(__author__) +                                            \
        "Licensed under the GPLv2.0\nhttp://www.gnu.org/licenses/old-licenses/gpl-2.0.txt"

    if argv is None:
        argv = sys.argv[1:]
    try:
        # setup option parser
        parser = OptionParser(
            version=program_version_string, epilog=program_longdesc, description=program_license)
        parser.add_option(
            "-s", "--search", dest="search_term", help="movie to search for", metavar="WORDS")
        # set defaults
        parser.set_defaults(serach_term="")

        # process options
        (opts, args) = parser.parse_args(argv)

        if opts.search_term:
            print("search_term= {}".format(opts.search_term))

        # MAIN BODY #

    except Exception as e:
        indent = len(program_name) * " "
        sys.stderr.write(program_name + ": " + repr(e) + "\n")
        sys.stderr.write(indent + "  for help use --help")
        return 2


if __name__ == "__main__":
    if DEBUG:
        sys.argv.append("-h")
    if TESTRUN:
        import doctest
        doctest.testmod()
    if PROFILE:
        import cProfile
        import pstats
        profile_filename = '__main___profile.txt'
        cProfile.run('main()', profile_filename)
        statsfile = open("profile_stats.txt", "wb")
        p = pstats.Stats(profile_filename, stream=statsfile)
        stats = p.strip_dirs().sort_stats('cumulative')
        stats.print_stats()
        statsfile.close()
        sys.exit(0)
    sys.exit(main())
