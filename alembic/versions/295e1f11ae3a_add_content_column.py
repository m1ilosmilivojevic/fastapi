"""add content column

Revision ID: 295e1f11ae3a
Revises: cd729e45cbf1
Create Date: 2023-12-20 19:38:01.638723

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '295e1f11ae3a'
down_revision: Union[str, None] = 'cd729e45cbf1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(255), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
