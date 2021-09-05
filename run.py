"""Main file of our application.

When ran with:
$ python run.py
it will reset the database and start the webserver.
"""

from os import getenv
from todo import app, db


if __name__ == "__main__":
    PORT = getenv("PORT", default="5000")
    HOST = getenv("HOST", default="127.0.0.1")

    db.drop_all()
    db.create_all()

    app.run(host=HOST, port=PORT)
