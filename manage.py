from app import create_app, db
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app.models import User,Pitch,Comment
# instances for the create_app
app = create_app('production')
