"""adding unique constraints to department names

Revision ID: 73b2273db762
Revises: 6c2b0931d802
Create Date: 2017-12-06 17:44:39.903199

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73b2273db762'
down_revision = '6c2b0931d802'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'departments', ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'departments', type_='unique')
    # ### end Alembic commands ###
