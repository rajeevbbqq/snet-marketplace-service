"""create banner and cta

Revision ID: 5ae9b3bdc7ce
Revises: a5b328b4edec
Create Date: 2021-02-04 16:21:07.677755

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5ae9b3bdc7ce'
down_revision = 'a5b328b4edec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('banner',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image', sa.VARCHAR(length=256), nullable=True),
    sa.Column('image_alignment', sa.VARCHAR(length=128), nullable=True),
    sa.Column('alt_text', sa.VARCHAR(length=256), nullable=True),
    sa.Column('title', sa.VARCHAR(length=256), nullable=True),
    sa.Column('rank', sa.Integer(), nullable=True),
    sa.Column('description', sa.TEXT(), nullable=True),
    sa.Column('row_created', mysql.TIMESTAMP(), nullable=True),
    sa.Column('row_updated', mysql.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cta',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('banner_id', sa.Integer(), nullable=True),
    sa.Column('text', sa.VARCHAR(length=256), nullable=True),
    sa.Column('url', sa.VARCHAR(length=256), nullable=True),
    sa.Column('type', sa.VARCHAR(length=256), nullable=True),
    sa.Column('variant', sa.VARCHAR(length=256), nullable=True),
    sa.Column('rank', sa.Integer(), nullable=True),
    sa.Column('row_created', mysql.TIMESTAMP(), nullable=True),
    sa.Column('row_updated', mysql.TIMESTAMP(), nullable=True),
    sa.ForeignKeyConstraint(['banner_id'], ['banner.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index('uq_srvc_grp', table_name='service_group')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('uq_srvc_grp', 'service_group', ['org_id', 'service_id', 'group_id'], unique=True)
    op.drop_table('cta')
    op.drop_table('banner')
    # ### end Alembic commands ###
