import os

basedir = os.path.abspath(os.path.dirname(__file__))

url = os.environ.get("DATABASE_URL") or "sqlite:///" + os.path.join(basedir, "app.db")
# url = "postgresql://postgres:postgres@127.0.0.1:5433/temp"