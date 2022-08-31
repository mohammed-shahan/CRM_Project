import sys
from os import path

this_dir = path.abspath(path.join(path.dirname("__file__")))
app_root = path.dirname(this_dir)

sys.path.append(path.abspath(app_root))
sys.path.append(path.abspath(this_dir))

from apps import create_app
from apps.config import Config

if __name__ == "__main__":
    app_factory = create_app()

    # print(app_factory.config)
    app_factory.run(host='0.0.0.0', port=5050)
