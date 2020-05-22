import logging

import shapely.geos

# This should hopefully show Shapely GEOS logging
logging.basicConfig(level=logging.DEBUG)

def doit():
    # Show the loaded GEOS library.
    print(shapely.geos._lgeos)


if __name__ == '__main__':
    doit()
