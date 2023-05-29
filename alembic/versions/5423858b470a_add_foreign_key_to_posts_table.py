"""add foreign key to posts table

Revision ID: 5423858b470a
Revises: b2592d3cf2c5
Create Date: 2023-05-29 10:11:49.375333

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5423858b470a'
down_revision = 'b2592d3cf2c5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key(
        'posts_users_fk',
          source_table="posts", 
          referent_table="users",
          local_cols=['owner_id'],
          remote_cols=['id'],
          ondelete="CASCADE"
    )


def downgrade() -> None:
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
