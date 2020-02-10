"""baseline

Revision ID: 54f83513e8f6
Revises: 
Create Date: 2020-02-07 13:24:51.697860

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '54f83513e8f6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('organization',
    sa.Column('uuid', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('org_id', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('org_type', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('origin', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('description', mysql.VARCHAR(length=1024), nullable=True),
    sa.Column('short_description', mysql.VARCHAR(length=1024), nullable=True),
    sa.Column('url', mysql.VARCHAR(length=512), nullable=True),
    sa.Column('duns_no', mysql.VARCHAR(length=36), nullable=True),
    sa.Column('contacts', mysql.JSON(), nullable=False),
    sa.Column('assets', mysql.JSON(), nullable=False),
    sa.Column('metadata_ipfs_hash', mysql.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('service_review_history',
    sa.Column('row_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('org_uuid', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('service_uuid', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('reviewed_service_data', mysql.JSON(), nullable=False),
    sa.Column('state', mysql.VARCHAR(length=64), nullable=False),
    sa.Column('reviewed_by', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('reviewed_on', mysql.TIMESTAMP(), nullable=False),
    sa.Column('created_on', mysql.TIMESTAMP(), nullable=False),
    sa.Column('updated_on', mysql.TIMESTAMP(), nullable=False),
    sa.PrimaryKeyConstraint('row_id')
    )
    op.create_table('group',
    sa.Column('row_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('id', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('org_uuid', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('payment_address', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('payment_config', mysql.JSON(), nullable=False),
    sa.Column('status', mysql.VARCHAR(length=128), nullable=True),
    sa.ForeignKeyConstraint(['org_uuid'], ['organization.uuid'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('row_id')
    )
    op.create_table('org_member',
    sa.Column('row_id', sa.Integer(), autoincrement=True, nullable=True),
    sa.Column('invite_code', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('org_uuid', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('role', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('username', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('address', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('status', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('transaction_hash', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('invited_on', mysql.TIMESTAMP(), nullable=True),
    sa.Column('created_on', mysql.TIMESTAMP(), nullable=True),
    sa.Column('updated_on', mysql.TIMESTAMP(), nullable=True),
    sa.ForeignKeyConstraint(['org_uuid'], ['organization.uuid'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('invite_code')
    )
    op.create_table('organization_address',
    sa.Column('row_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('org_uuid', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('address_type', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('street_address', mysql.VARCHAR(length=256), nullable=True),
    sa.Column('apartment', mysql.VARCHAR(length=256), nullable=True),
    sa.Column('city', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('pincode', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('state', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('country', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('created_on', mysql.TIMESTAMP(), nullable=True),
    sa.Column('updated_on', mysql.TIMESTAMP(), nullable=True),
    sa.ForeignKeyConstraint(['org_uuid'], ['organization.uuid'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('row_id')
    )
    op.create_table('organization_state',
    sa.Column('row_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('org_uuid', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('state', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('transaction_hash', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('user_address', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('created_by', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('created_on', mysql.TIMESTAMP(), nullable=True),
    sa.Column('updated_by', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('updated_on', mysql.TIMESTAMP(), nullable=True),
    sa.Column('approved_by', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('approved_on', mysql.TIMESTAMP(), nullable=True),
    sa.ForeignKeyConstraint(['org_uuid'], ['organization.uuid'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('row_id')
    )
    op.create_table('service',
    sa.Column('org_uuid', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('uuid', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('display_name', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('service_id', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('metadata_ipfs_hash', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('proto', mysql.JSON(), nullable=False),
    sa.Column('short_description', mysql.VARCHAR(length=1024), nullable=False),
    sa.Column('description', mysql.VARCHAR(length=1024), nullable=False),
    sa.Column('project_url', mysql.VARCHAR(length=512), nullable=True),
    sa.Column('assets', mysql.JSON(), nullable=False),
    sa.Column('ratings', mysql.JSON(), nullable=False),
    sa.Column('ranking', sa.Integer(), nullable=False),
    sa.Column('contributors', mysql.JSON(), nullable=False),
    sa.Column('tags', mysql.JSON(), nullable=False),
    sa.Column('mpe_address', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('created_on', mysql.TIMESTAMP(), nullable=False),
    sa.Column('updated_on', mysql.TIMESTAMP(), nullable=False),
    sa.ForeignKeyConstraint(['org_uuid'], ['organization.uuid'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('service_group',
    sa.Column('row_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('org_uuid', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('service_uuid', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('group_id', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('group_name', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('pricing', mysql.JSON(), nullable=False),
    sa.Column('endpoints', mysql.JSON(), nullable=False),
    sa.Column('daemon_address', mysql.JSON(), nullable=False),
    sa.Column('free_calls', sa.Integer(), nullable=False),
    sa.Column('free_call_signer_address', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('created_on', mysql.TIMESTAMP(), nullable=False),
    sa.Column('updated_on', mysql.TIMESTAMP(), nullable=False),
    sa.ForeignKeyConstraint(['service_uuid'], ['service.uuid'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('row_id'),
    sa.UniqueConstraint('group_id'),
    sa.UniqueConstraint('org_uuid', 'service_uuid', 'group_id', name='uq_org_srvc_grp')
    )
    op.create_table('service_state',
    sa.Column('row_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('org_uuid', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('service_uuid', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('state', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('transaction_hash', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('created_by', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('updated_by', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('approved_by', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('created_on', mysql.TIMESTAMP(), nullable=False),
    sa.Column('updated_on', mysql.TIMESTAMP(), nullable=False),
    sa.ForeignKeyConstraint(['service_uuid'], ['service.uuid'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('row_id'),
    sa.UniqueConstraint('org_uuid', 'service_uuid', name='uq_org_srvc'),
    sa.UniqueConstraint('service_uuid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('service_state')
    op.drop_table('service_group')
    op.drop_table('service')
    op.drop_table('organization_state')
    op.drop_table('organization_address')
    op.drop_table('org_member')
    op.drop_table('group')
    op.drop_table('service_review_history')
    op.drop_table('organization')
    # ### end Alembic commands ###
