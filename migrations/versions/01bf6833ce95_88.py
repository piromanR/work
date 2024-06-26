"""88

Revision ID: 01bf6833ce95
Revises: a7887350326d
Create Date: 2024-04-17 00:01:49.634801

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '01bf6833ce95'
down_revision: Union[str, None] = 'a7887350326d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('users_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('hashed_password', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('role',sa.VARCHAR(),autoincrement=False,default='user'),
    sa.PrimaryKeyConstraint('id', name='users_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('roles',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('permissions', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='roles_pkey')
    )
    op.create_table('projects',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('nameofproject', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('owner_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], name='projects_owner_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='projects_pkey')
    )
    # ### end Alembic commands ###
