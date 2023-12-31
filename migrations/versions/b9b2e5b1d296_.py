"""empty message

Revision ID: b9b2e5b1d296
Revises: f79d6f4f9c7a
Create Date: 2023-09-19 11:44:41.546558

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9b2e5b1d296'
down_revision = 'f79d6f4f9c7a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('data', schema=None) as batch_op:
        batch_op.drop_index('response')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('data', schema=None) as batch_op:
        batch_op.create_index('response', ['response'], unique=False)

    # ### end Alembic commands ###
