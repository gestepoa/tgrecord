"""empty message

Revision ID: 822f0429678c
Revises: 16c64600e859
Create Date: 2023-12-05 23:47:19.374594

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '822f0429678c'
down_revision = '16c64600e859'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('ideology', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nation_view', sa.Enum('汉族主义', '完整公民权', '有限公民权', '中华民族叙事'), nullable=True, comment='民族观点'))
        batch_op.add_column(sa.Column('war_view', sa.Enum('沙文主义', '和平主义', '解放台湾'), nullable=True, comment='战争观点'))
        batch_op.add_column(sa.Column('political_view', sa.Enum('精英政治', '民粹主义'), nullable=True, comment='政治观点'))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('ideology', schema=None) as batch_op:
        batch_op.drop_column('political_view')
        batch_op.drop_column('war_view')
        batch_op.drop_column('nation_view')

    # ### end Alembic commands ###
