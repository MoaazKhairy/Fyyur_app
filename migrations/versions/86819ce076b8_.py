"""empty message

Revision ID: 86819ce076b8
Revises: ee660d60ec85
Create Date: 2021-02-24 12:38:26.580253

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86819ce076b8'
down_revision = 'ee660d60ec85'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('seeking_description', sa.String(length=300), nullable=True))
    op.add_column('Venue', sa.Column('seeking_talent', sa.Boolean(), nullable=True))
    op.add_column('Venue', sa.Column('website', sa.String(length=300), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'website')
    op.drop_column('Venue', 'seeking_talent')
    op.drop_column('Venue', 'seeking_description')
    # ### end Alembic commands ###
