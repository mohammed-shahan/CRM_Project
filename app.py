import sys
from os import path
this_dir = path.abspath(path.join(path.dirname("__file__")))
# get root of app, rip off one subdir ... go up
app_root = path.dirname(this_dir)
sys.path.append(path.abspath(app_root))
sys.path.append(path.abspath(this_dir))

from apps import create_app, setup_database
from apps.config import Config

if __name__ == "__main__":
    app_factory = create_app()
    # do not kill db, if exists
    if not path.isfile(Config.db_path):
        setup_database(app_factory)

    # print(app_factory.config)
    app_factory.run(host='0.0.0.0', port=5050)
