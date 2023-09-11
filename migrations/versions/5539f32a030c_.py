"""empty message

Revision ID: 5539f32a030c
Revises: 8e7dcaaa6568
Create Date: 2023-09-09 20:52:54.190021

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5539f32a030c'
down_revision = '8e7dcaaa6568'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('basic_info', schema=None) as batch_op:
        batch_op.add_column(sa.Column('create_time', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('update_time', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('delete_time', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('basic_info', schema=None) as batch_op:
        batch_op.drop_column('delete_time')
        batch_op.drop_column('update_time')
        batch_op.drop_column('create_time')

    # ### end Alembic commands ###
