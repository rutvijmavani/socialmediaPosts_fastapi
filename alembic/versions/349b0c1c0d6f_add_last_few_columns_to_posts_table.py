"""add last few columns to posts table

Revision ID: 349b0c1c0d6f
Revises: db17f7947247
Create Date: 2025-06-05 23:19:21.438908

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '349b0c1c0d6f'
down_revision: Union[str, None] = 'db17f7947247'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts' , sa.Column('published' , sa.Boolean() , nullable = False , server_default = 'True'))
    op.add_column('posts' , sa.Column(
        'created_at' , sa.TIMESTAMP(timezone = True) , nullable = False , server_default = sa.text('NOW()') 
    ))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts' , 'published')
    op.drop_column('posts' , 'created_at')
    pass
