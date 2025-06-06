"""add user table

Revision ID: 03bcf44fb98e
Revises: cb7907ffc15d
Create Date: 2025-06-05 22:42:57.923005

"""
from pydoc import text
from time import timezone
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '03bcf44fb98e'
down_revision: Union[str, None] = 'cb7907ffc15d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('users' ,
                    sa.Column('id' , sa.Integer() , nullable = False , primary_key = True) , 
                    sa.Column('email' , sa.String() , nullable = False) , 
                    sa.Column('password' , sa.String() , nullable = False),
                    sa.Column('created_at' , sa.TIMESTAMP(timezone = True), 
                              server_default = sa.text('now()') , nullable = False),
                              sa.UniqueConstraint('email')
                              )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('users')
    pass
