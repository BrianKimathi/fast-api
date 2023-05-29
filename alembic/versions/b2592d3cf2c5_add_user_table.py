"""add user table

Revision ID: b2592d3cf2c5
Revises: ce82b58e8a89
Create Date: 2023-05-28 07:07:28.347899

"""
import email
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2592d3cf2c5'
down_revision = 'ce82b58e8a89'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                  server_default=sa.text('now()'), nullable=False
                ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )


def downgrade() -> None:
    op.drop_table('users')
    pass
