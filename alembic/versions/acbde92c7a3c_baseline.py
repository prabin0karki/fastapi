"""baseline

Revision ID: acbde92c7a3c
Revises:
Create Date: 2020-09-08 14:43:58.572766

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "acbde92c7a3c"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("first_name", sa.String),
        sa.Column("last_name", sa.String),
        sa.Column("email", sa.String, unique=True, index=True),
        sa.Column("password", sa.String),
    )


def downgrade():
    op.drop_table("users")
