"""
create table users

Revision ID: ver1
Revises: ver0
Create Date: 2025-05-21
"""

from typing import Sequence, Union

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "ver1"
down_revision: Union[str, None] = "ver0"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            primary_key=True,
            server_default=sa.text("gen_random_uuid()"),
        ),
        sa.Column("name", sa.String(length=50), nullable=True),
        sa.Column("email", sa.String(length=100), nullable=True, unique=True),
        sa.Column("mfa_enabled", sa.Boolean(), nullable=True, server_default="false"),
        sa.Column("del_flag", sa.Boolean(), nullable=True, server_default="false"),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=False),
            server_default=sa.func.current_timestamp(),
            nullable=True,
        ),
        sa.Column("created_by", sa.String(length=255), nullable=True),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=False),
            server_default=sa.func.current_timestamp(),
            nullable=True,
        ),
        sa.Column("updated_by", sa.String(length=255), nullable=True),
    )


def downgrade():
    op.drop_table("users")
