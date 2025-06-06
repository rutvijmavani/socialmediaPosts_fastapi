"""add content column to posts table

Revision ID: cb7907ffc15d
Revises: c630f5ddc6ce
Create Date: 2025-06-05 22:29:37.114898

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cb7907ffc15d'
down_revision: Union[str, None] = 'c630f5ddc6ce'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts' , sa.Column('content' , sa.String() , nullable = False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts' , 'content')
    pass
