from app import create_app,db
from flask_script import Manager,Server
from app.models import User, Role, Pitch
from  flask_migrate import Migrate, MigrateCommand

# Creating app instance
<<<<<<< HEAD
app = create_app('production')
=======
app = create_app('development')
>>>>>>> 5e8386819438b482f418774b64bbd2b55e253006

manager = Manager(app)
manager.add_command('server',Server)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.command
def test():
   pass

@manager.shell
def make_shell_context():
<<<<<<< HEAD
   return dict(app = app,db = db,User = User, Role = Role, Pitch = Pitch)

if __name__=='__main__':
   manager.run()
=======
    return dict(app = app,db = db,User = User, Role = Role, Pitch = Pitch)

if __name__=='__main__':
    manager.run()
>>>>>>> 5e8386819438b482f418774b64bbd2b55e253006
