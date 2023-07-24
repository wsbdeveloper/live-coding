"""Model: ConsultPouplation

Revision ID: ba0ab7f7e214
Revises: 
Create Date: 2023-07-24 00:22:27.267127

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy import FLOAT, INTEGER, VARCHAR, Column, DateTime, func

# revision identifiers, used by Alembic.
revision = 'ba0ab7f7e214'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
    "consults_populations_climate",
    Column("id", INTEGER, primary_key=True),
    Column("population", FLOAT, nullable=False),
    Column("temp", VARCHAR(50), nullable=True),
    Column("city", VARCHAR(40), nullable=True),
    Column("created_at", DateTime, default=func.now(), onupdate=func.now()),
    Column("updated_at", DateTime, default=func.now(), onupdate=func.now())
)

def downgrade() -> None:
    op.drop_table("consults_populations_climate")
