"""empty message

Revision ID: 30708d4847be
Revises: d5b117466d04
Create Date: 2023-09-12 01:14:12.654039

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '30708d4847be'
down_revision = 'd5b117466d04'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=mysql.INTEGER(),
               comment='用户id',
               existing_nullable=False,
               autoincrement=True)
        batch_op.alter_column('username',
               existing_type=mysql.VARCHAR(length=255),
               comment='用户名',
               existing_nullable=False)
        batch_op.alter_column('email',
               existing_type=mysql.VARCHAR(length=255),
               comment='邮箱',
               existing_nullable=True)
        batch_op.alter_column('password',
               existing_type=mysql.VARCHAR(length=255),
               comment='密码',
               existing_nullable=True)
        batch_op.alter_column('note',
               existing_type=mysql.VARCHAR(length=255),
               comment='备注',
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('note',
               existing_type=mysql.VARCHAR(length=255),
               comment=None,
               existing_comment='备注',
               existing_nullable=True)
        batch_op.alter_column('password',
               existing_type=mysql.VARCHAR(length=255),
               comment=None,
               existing_comment='密码',
               existing_nullable=True)
        batch_op.alter_column('email',
               existing_type=mysql.VARCHAR(length=255),
               comment=None,
               existing_comment='邮箱',
               existing_nullable=True)
        batch_op.alter_column('username',
               existing_type=mysql.VARCHAR(length=255),
               comment=None,
               existing_comment='用户名',
               existing_nullable=False)
        batch_op.alter_column('id',
               existing_type=mysql.INTEGER(),
               comment=None,
               existing_comment='用户id',
               existing_nullable=False,
               autoincrement=True)

    # ### end Alembic commands ###
