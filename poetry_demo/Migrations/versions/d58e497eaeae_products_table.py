"""products_table
Revision ID: d58e497eaeae
Revises: 5b06281c58ae
Create Date: 2020-09-09 12:55:17.566754

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "d58e497eaeae"
down_revision = "5b06281c58ae"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "products",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("is_available", sa.Boolean(), default=1),
    )


def downgrade():
    op.drop_table("products")
