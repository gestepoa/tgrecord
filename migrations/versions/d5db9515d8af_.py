"""empty message

Revision ID: d5db9515d8af
Revises: c6d3e769ae1f
Create Date: 2023-09-24 20:03:37.580541

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd5db9515d8af'
down_revision = 'c6d3e769ae1f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('position',
    sa.Column('id', sa.Integer(), nullable=False, comment='职务信息id'),
    sa.Column('name', sa.String(length=255), nullable=True, comment='姓名'),
    sa.Column('position_name', sa.String(length=255), nullable=True, comment='职务名称'),
    sa.Column('position_domains', sa.String(length=255), nullable=True, comment='职务领域'),
    sa.Column('position_level', sa.String(length=255), nullable=True, comment='职务等级'),
    sa.Column('note', sa.String(length=255), nullable=True, comment='说明'),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('delete_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('resume', schema=None) as batch_op:
        batch_op.alter_column('local',
               existing_type=mysql.DATETIME(),
               type_=sa.String(length=255),
               existing_comment='所在县市',
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('resume', schema=None) as batch_op:
        batch_op.alter_column('local',
               existing_type=sa.String(length=255),
               type_=mysql.DATETIME(),
               existing_comment='所在县市',
               existing_nullable=True)

    op.drop_table('position')
    # ### end Alembic commands ###
