"""add last few columns to posts table

Revision ID: e6314c5068a4
Revises: 5423858b470a
Create Date: 2023-05-29 10:29:13.987205

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6314c5068a4'
down_revision = '5423858b470a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'posts', 
        sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    
    op.add_column(
        'posts', 
        sa.Column(
                'created_at', 
                sa.TIMESTAMP(timezone=True), 
                    nullable=False, server_default=sa.text('NOW()')),
            )
    
    



def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
