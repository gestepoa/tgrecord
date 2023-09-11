"""edu info columns changed

Revision ID: 9b11bfaee3f6
Revises: 4cebe9acbb9d
Create Date: 2023-09-06 23:24:56.666203

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9b11bfaee3f6'
down_revision = '4cebe9acbb9d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('edu_info', schema=None) as batch_op:
        batch_op.add_column(sa.Column('isnational', sa.String(length=255), nullable=True))
        batch_op.alter_column('level',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('edu_info', schema=None) as batch_op:
        batch_op.alter_column('level',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)
        batch_op.drop_column('isnational')

    # ### end Alembic commands ###
