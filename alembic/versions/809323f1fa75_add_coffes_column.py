"""Add Coffes column

Revision ID: 809323f1fa75
Revises: f24e33416132
Create Date: 2024-01-08 17:09:07.237454

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '809323f1fa75'
down_revision: Union[str, None] = 'f24e33416132'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('coffes',
    sa.Column('coffe_id', sa.Integer(), nullable=False),
    sa.Column('coffe_name', sa.String(), nullable=False),
    sa.Column('coffe_addres', sa.String(), nullable=False),
    sa.Column('coffe_phone_number', sa.String(), nullable=False),
    sa.Column('coffe_email', sa.String(), nullable=True),
    sa.Column('coffe_status', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('coffe_id')
    )
    op.add_column('users', sa.Column('status', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'status')
    op.drop_table('coffes')
    # ### end Alembic commands ###
