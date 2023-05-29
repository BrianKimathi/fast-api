"""add content column to posts table

Revision ID: ce82b58e8a89
Revises: 07855ec83705
Create Date: 2023-05-28 07:02:47.360781

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce82b58e8a89'
down_revision = '07855ec83705'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))

def downgrade() -> None:
    op.drop_column('posts', 'content')
