"""merge head and head

Revision ID: fca5db88f84e
Revises: 753a46794e77, e062955ad5f7
Create Date: 2024-05-16 00:26:07.262064

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fca5db88f84e'
down_revision = ('753a46794e77', 'e062955ad5f7')
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
