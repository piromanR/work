"""101

Revision ID: 2414a095f52e
Revises: 9b02ba23b5ee
Create Date: 2024-04-17 00:14:47.569183

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2414a095f52e'
down_revision: Union[str, None] = '9b02ba23b5ee'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_projects_id'), 'projects', ['id'], unique=False)
    op.create_index(op.f('ix_projects_nameofproject'), 'projects', ['nameofproject'], unique=False)
    op.add_column('roles', sa.Column('permissions', sa.String(), nullable=True))
    op.create_index(op.f('ix_roles_id'), 'roles', ['id'], unique=False)
    op.drop_constraint('roles_whomakeit_fkey', 'roles', type_='foreignkey')
    op.drop_column('roles', 'whomakeit')
    op.add_column('users', sa.Column('role', sa.String(), nullable=True))
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_column('users', 'role')
    op.add_column('roles', sa.Column('whomakeit', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('roles_whomakeit_fkey', 'roles', 'users', ['whomakeit'], ['id'])
    op.drop_index(op.f('ix_roles_id'), table_name='roles')
    op.drop_column('roles', 'permissions')
    op.drop_index(op.f('ix_projects_nameofproject'), table_name='projects')
    op.drop_index(op.f('ix_projects_id'), table_name='projects')
    # ### end Alembic commands ###