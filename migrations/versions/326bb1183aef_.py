"""empty message

Revision ID: 326bb1183aef
Revises: 7af99ede5f58
Create Date: 2023-09-07 00:00:44.453590

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '326bb1183aef'
down_revision = '7af99ede5f58'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('family', schema=None) as batch_op:
        batch_op.add_column(sa.Column('birthday', sa.DateTime(), nullable=True))
        batch_op.alter_column('name',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)
        batch_op.alter_column('relation',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('family', schema=None) as batch_op:
        batch_op.alter_column('relation',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)
        batch_op.alter_column('name',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)
        batch_op.drop_column('birthday')

    # ### end Alembic commands ###