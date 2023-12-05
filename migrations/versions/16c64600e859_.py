"""empty message

Revision ID: 16c64600e859
Revises: b607a99d0eab
Create Date: 2023-12-05 23:46:42.296106

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '16c64600e859'
down_revision = 'b607a99d0eab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('ideology', schema=None) as batch_op:
        batch_op.drop_column('war_view')
        batch_op.drop_column('nation_view')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('ideology', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nation_view', mysql.ENUM('汉族主义', '完整公民权', '中华民族'), nullable=True, comment='民族观点'))
        batch_op.add_column(sa.Column('war_view', mysql.ENUM('沙文主义', '和平主义'), nullable=True, comment='战争观点'))

    # ### end Alembic commands ###
