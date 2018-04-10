"""add about_me and last_seen fields to User model

Revision ID: 6680c8bc60f9
Revises: 60ae9f5ea6d5
Create Date: 2018-04-03 06:26:41.311341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6680c8bc60f9'
down_revision = '60ae9f5ea6d5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
