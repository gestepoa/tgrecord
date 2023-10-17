"""empty message

Revision ID: 927d2bfc6d63
Revises: 41f63c4aee9d
Create Date: 2023-10-17 23:25:29.214871

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '927d2bfc6d63'
down_revision = '41f63c4aee9d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('edu_info', schema=None) as batch_op:
        batch_op.alter_column('enrollment',
               existing_type=mysql.DATETIME(),
               type_=sa.Date(),
               existing_comment='入学时间',
               existing_nullable=True)

    with op.batch_alter_table('family', schema=None) as batch_op:
        batch_op.alter_column('birthday',
               existing_type=mysql.DATETIME(),
               type_=sa.Date(),
               existing_comment='出生日期',
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('family', schema=None) as batch_op:
        batch_op.alter_column('birthday',
               existing_type=sa.Date(),
               type_=mysql.DATETIME(),
               existing_comment='出生日期',
               existing_nullable=True)

    with op.batch_alter_table('edu_info', schema=None) as batch_op:
        batch_op.alter_column('enrollment',
               existing_type=sa.Date(),
               type_=mysql.DATETIME(),
               existing_comment='入学时间',
               existing_nullable=True)

    # ### end Alembic commands ###
