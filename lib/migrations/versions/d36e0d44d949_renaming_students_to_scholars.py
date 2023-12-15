"""Renaming students to scholars

Revision ID: d36e0d44d949
Revises: 791279dd0760
Create Date: 2023-12-15 14:27:03.549003

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd36e0d44d949'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')