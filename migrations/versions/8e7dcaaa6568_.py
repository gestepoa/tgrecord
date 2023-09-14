"""empty message

Revision ID: 8e7dcaaa6568
Revises: 89d9301cb0f6
Create Date: 2023-09-07 23:45:14.358236

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8e7dcaaa6568'
down_revision = '89d9301cb0f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('family', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=mysql.INTEGER(),
               comment='家族信息id',
               existing_nullable=False,
               autoincrement=True)
        batch_op.alter_column('name',
               existing_type=mysql.VARCHAR(length=255),
               comment='姓名',
               existing_nullable=False)
        batch_op.alter_column('relation',
               existing_type=mysql.VARCHAR(length=255),
               comment='关系',
               existing_nullable=False)
        batch_op.alter_column('birthday',
               existing_type=mysql.DATETIME(),
               comment='出生日期',
               existing_nullable=True)
        batch_op.alter_column('remarks',
               existing_type=mysql.VARCHAR(length=255),
               comment='备注',
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('family', schema=None) as batch_op:
        batch_op.alter_column('remarks',
               existing_type=mysql.VARCHAR(length=255),
               comment=None,
               existing_comment='备注',
               existing_nullable=True)
        batch_op.alter_column('birthday',
               existing_type=mysql.DATETIME(),
               comment=None,
               existing_comment='出生日期',
               existing_nullable=True)
        batch_op.alter_column('relation',
               existing_type=mysql.VARCHAR(length=255),
               comment=None,
               existing_comment='关系',
               existing_nullable=False)
        batch_op.alter_column('name',
               existing_type=mysql.VARCHAR(length=255),
               comment=None,
               existing_comment='姓名',
               existing_nullable=False)
        batch_op.alter_column('id',
               existing_type=mysql.INTEGER(),
               comment=None,
               existing_comment='家族信息id',
               existing_nullable=False,
               autoincrement=True)

    # ### end Alembic commands ###