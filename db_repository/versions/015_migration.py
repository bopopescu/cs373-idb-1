from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
characters = Table('characters', post_meta,
    Column('character_id', Integer),
    Column('episode_id', Integer),
)

episode = Table('episode', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR),
    Column('season', INTEGER),
    Column('characters', VARCHAR),
    Column('predecessor', VARCHAR),
    Column('successor', VARCHAR),
    Column('imageLink', VARCHAR),
    Column('nr', INTEGER),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['characters'].create()
    pre_meta.tables['episode'].columns['characters'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['characters'].drop()
    pre_meta.tables['episode'].columns['characters'].create()
