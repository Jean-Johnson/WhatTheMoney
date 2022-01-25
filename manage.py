from multiprocessing import managers
import os
import unittest
from app import create_app
from flask_script import Manager, Shell

print(os.environ.get("Moneyconfig"))
if os.environ.get("Moneyconfig") is not None:
    app = create_app(os.environ.get("Moneyconfig"))
else:
    app = create_app("dev")
manager = Manager(app)

def make_shell_context():
    return dict(app=app)

manager.add_command("shell",Shell(make_context=make_shell_context))

@manager.command
def test():
    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestResult(verbosity=2).run(tests)

if __name__ == "__main__":
    manager.run()