"""empty message

Revision ID: 5514d26922e6
Revises: f9994a57f9fe
Create Date: 2021-02-22 22:05:18.344784

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5514d26922e6'
down_revision = 'f9994a57f9fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Artist', 'image_link',
               existing_type=sa.VARCHAR(length=500),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Artist', 'image_link',
               existing_type=sa.VARCHAR(length=500),
               nullable=False)
    # ### end Alembic commands ###
