"""change in alert timestamp

Revision ID: 94aa51280c69
Revises: 8518b6dbb28b
Create Date: 2023-12-07 23:35:39.778103

"""
import datetime
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '94aa51280c69'
down_revision: Union[str, None] = '8518b6dbb28b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("Alerts", "Alert_Timestamp")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("Alerts", sa.Column("Alert_Timestamp", sa.DateTime,default = datetime.utcnow))
    # ### end Alembic commands ###