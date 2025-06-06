"""add foreign key to posts table

Revision ID: db17f7947247
Revises: 03bcf44fb98e
Create Date: 2025-06-05 23:09:15.426151

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'db17f7947247'
down_revision: Union[str, None] = '03bcf44fb98e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts' , sa.Column('owner_id' , sa.Integer() , nullable = False))
    op.create_foreign_key('post_users_fk' , source_table = 'posts' , referent_table = 'users' , 
                          local_cols = ['owner_id']  , remote_cols = ['id'] , ondelete = 'CASCADE'  )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('post_users_fk' , table_name = 'posts')
    op.drop_column('posts' , 'owner_id')
    pass
