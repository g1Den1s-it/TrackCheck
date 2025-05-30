"""Added companies model

Revision ID: 156cd58adf47
Revises: 
Create Date: 2025-04-01 15:23:02.685183

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '156cd58adf47'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('companies',
    sa.Column('company_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('company_name', sa.String(length=124), nullable=False),
    sa.Column('company_address', sa.String(length=164), nullable=True),
    sa.Column('company_email', sa.String(length=124), nullable=False),
    sa.Column('company_phone', sa.String(length=18), nullable=True),
    sa.PrimaryKeyConstraint('company_id'),
    sa.UniqueConstraint('company_email'),
    sa.UniqueConstraint('company_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('companies')
    # ### end Alembic commands ###
