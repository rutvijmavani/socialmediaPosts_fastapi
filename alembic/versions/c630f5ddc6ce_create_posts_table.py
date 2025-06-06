"""create posts table

Revision ID: c630f5ddc6ce
Revises: 
Create Date: 2025-06-05 22:01:24.394829

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c630f5ddc6ce'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('posts' , sa.Column('id' , sa.Integer() , nullable = False , primary_key = True),
                    sa.Column('title' , sa.String() , nullable = False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('posts')
    pass
