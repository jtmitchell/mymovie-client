#!/usr/bin/env python
# encoding: utf-8
'''
__main__ -- Main entry point for client to query movies and save favourites to MyMovie

__main__ is a client for MyMovie

@author:     James Mitchell

@copyright:  2015 James Mitchell. All rights reserved.

@license:    GPLv3

@contact:    james.mitchell@maungawhau.net.nz
@deffield    updated: 2015-08-10
'''

import argparse
import os
import sys

from mymovie.search import OMDB

from . import __version__, __author__


__all__ = []

DEBUG = 0
TESTRUN = 0
PROFILE = 0


def main(argv=None):
    '''Command line options.'''

    program_name = os.path.basename(sys.argv[0])
    program_version = __version__

    program_longdesc = ''''''  # optional - give further explanation about what the program does
    program_license = ["Copyright 2015 {0}".format(__author__),
                       "Licensed under the GPLv3.0",
                       "http://www.gnu.org/licenses/gpl.txt",
                       ]

    if argv is None:
        argv = sys.argv[1:]
    try:
        # setup option parser
        parser = argparse.ArgumentParser(
            description='\n'.join(program_license), epilog=program_longdesc)
        parser.add_argument('--version', action='version', version=program_version)
        parser.add_argument(
            "-s", "--search", dest="search_term", help="movie to search for", type=str)
        parser.add_argument(
            "-i", "--imdb_id", dest="imdb_id", help="IMDB id for the movie", type=str)
        parser.add_argument(
            "-v", "--verbose", dest="verbose", help="be more verbose", action="store_true")

        # process options
        args = parser.parse_args(argv)

        search_service = OMDB()
        if args.search_term:
            results = search_service.search(args.search_term)
            for result in results:
                print('"{0}" ({1} {2}) - id: {3}'.format(
                    result.get('Title'),
                    result.get('Year'),
                    result.get('Type'),
                    result.get('imdbID'),
                ))
                if args.verbose:
                    print('{0}\n'.format(result))
        if args.imdb_id:
            result = search_service.get(movie_id=args.imdb_id)
            if result:
                print('"{0}" ({1}) - id: {2}'.format(
                    result.get('Title'),
                    result.get('Year'),
                    result.get('imdbID'),
                ))
                if args.verbose:
                    print('{0}\n'.format(result))
            else:
                print('No result')

    except Exception as e:
        indent = len(program_name) * " "
        sys.stderr.write(program_name + ": " + repr(e) + "\n")
        sys.stderr.write(indent + "  for help use --help")
        return 2


if __name__ == "__main__":
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
