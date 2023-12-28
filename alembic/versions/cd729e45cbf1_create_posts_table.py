"""create posts table

Revision ID: cd729e45cbf1
Revises: 
Create Date: 2023-12-20 19:28:30.728497

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cd729e45cbf1'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id',sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(256), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
