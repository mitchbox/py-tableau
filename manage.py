from flask.ext.script import Manager
from application import app


manager = Manager(app)

if __name__ == '__main__':
    manager.run()
