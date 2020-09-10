"""Add a column to product

Revision ID: a9aa6c26a6b1
Revises: 3429116eae15
Create Date: 2020-09-10 12:37:15.552521

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a9aa6c26a6b1"
down_revision = "3429116eae15"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("products", sa.Column("price", sa.Integer, default=250)),


def downgrade():
    op.drop_column("products", "price")
