from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('fname', String(length=120)),
    Column('lname', String(length=120)),
    Column('email', String(length=120)),
    Column('nickname', String(length=64)),
    Column('username', String(length=64)),
    Column('password', String(length=120)),
    Column('password_length', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['password'].create()
    post_meta.tables['user'].columns['password_length'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['password'].drop()
    post_meta.tables['user'].columns['password_length'].drop()
