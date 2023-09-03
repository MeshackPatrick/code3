"""Empty Init

Revision ID: eabd4e55f87d
Revises: 487702ad159d
Create Date: 2023-09-03 21:33:06.101109

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eabd4e55f87d'
down_revision: Union[str, None] = '487702ad159d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
