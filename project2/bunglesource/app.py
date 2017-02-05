import os

# Change working directory so relative paths (and template lookup) work again
os.chdir(os.path.dirname(__file__))

import bottle

import project2

application = bottle.default_app()
