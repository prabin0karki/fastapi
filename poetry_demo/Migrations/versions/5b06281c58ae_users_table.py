"""users_table

Revision ID: 5b06281c58ae
Revises: e33f55c81eda
Create Date: 2020-09-09 12:38:45.889480

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "5b06281c58ae"
down_revision = "e33f55c81eda"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("first_name", sa.String()),
        sa.Column("last_name", sa.String()),
        sa.Column("email", sa.String(), unique=True, index=True),
        sa.Column("password", sa.String()),
        sa.Column("is_active", sa.Boolean(), default=1),
        sa.Column("disabled", sa.Boolean(), default=0),
    )


def downgrade():
    op.drop_table("users")
