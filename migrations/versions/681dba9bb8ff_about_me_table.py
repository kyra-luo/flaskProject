"""about me table

Revision ID: 681dba9bb8ff
Revises: 631479a61e44
Create Date: 2024-05-14 15:01:42.203929

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '681dba9bb8ff'
down_revision = '631479a61e44'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profile')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profile',
    sa.Column('profile_id', sa.INTEGER(), nullable=False),
    sa.Column('about_me', sa.VARCHAR(length=250), nullable=False),
    sa.PrimaryKeyConstraint('profile_id')
    )
    # ### end Alembic commands ###
