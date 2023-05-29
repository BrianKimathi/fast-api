"""create posts table

Revision ID: 07855ec83705
Revises: 
Create Date: 2023-05-28 06:44:01.153641

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07855ec83705'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
