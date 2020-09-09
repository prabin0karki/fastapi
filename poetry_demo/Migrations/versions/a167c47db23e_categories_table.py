"""categories_table

Revision ID: a167c47db23e
Revises: fbee1d8d1ad0
Create Date: 2020-09-09 17:54:51.841026

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a167c47db23e"
down_revision = "fbee1d8d1ad0"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "categories",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(), unique=True, index=True),
    )


def downgrade():
    op.drop_table("categories")
