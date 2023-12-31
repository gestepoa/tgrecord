"""empty message

Revision ID: b607a99d0eab
Revises: 32486850b5c5
Create Date: 2023-12-05 23:44:32.009077

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b607a99d0eab'
down_revision = '32486850b5c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('ideology', schema=None) as batch_op:
        batch_op.drop_column('political_view')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('ideology', schema=None) as batch_op:
        batch_op.add_column(sa.Column('political_view', mysql.ENUM('精英政治', '民粹主义'), nullable=True, comment='政治观点'))

    # ### end Alembic commands ###
