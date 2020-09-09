"""products_table

Revision ID: 3429116eae15
Revises: a167c47db23e
Create Date: 2020-09-09 17:55:37.839060

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "3429116eae15"
down_revision = "a167c47db23e"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "products",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("is_available", sa.Boolean(), default=1),
        sa.Column("name", sa.String(), unique=True, index=True),
        sa.Column("author_id", sa.Integer, sa.ForeignKey("users.id"), nullable=False),
        sa.Column(
            "category_id", sa.Integer, sa.ForeignKey("categories.id"), nullable=False
        ),
    )


def downgrade():
    op.drop_table("products")
