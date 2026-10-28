from src import app

import sys

args = sys.argv

if len(args) < 2:
    raise Exception("ERROR: Invalid php path")

phpproject = args[1]

botot = app.App()
botot.create_app("Meu primeiro app", 3011, phpproject)

botot.run()