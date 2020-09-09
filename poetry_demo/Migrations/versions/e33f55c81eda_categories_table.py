"""categories_table
Revision ID: e33f55c81eda
Revises: 1c13284f2007
Create Date: 2020-09-09 12:28:42.498349

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "e33f55c81eda"
down_revision = "1c13284f2007"
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
