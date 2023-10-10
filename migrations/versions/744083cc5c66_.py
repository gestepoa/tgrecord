"""empty message

Revision ID: 744083cc5c66
Revises: d5db9515d8af
Create Date: 2023-10-09 23:45:31.742236

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '744083cc5c66'
down_revision = 'd5db9515d8af'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('basic_info', schema=None) as batch_op:
        batch_op.drop_column('code')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('basic_info', schema=None) as batch_op:
        batch_op.add_column(sa.Column('code', mysql.VARCHAR(length=255), nullable=False, comment='编号'))

    # ### end Alembic commands ###