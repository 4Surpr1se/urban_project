"""initial migrate

Revision ID: b38e16cca450
Revises:
Create Date: 2024-08-10 12:41:16.350173

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b38e16cca450'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('permissions',
                    sa.Column('id', sa.UUID(), nullable=False),
                    sa.Column('name', sa.String(), nullable=True),
                    sa.Column('description', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_permissions_id'), 'permissions', ['id'], unique=True)
    op.create_index(op.f('ix_permissions_name'), 'permissions', ['name'], unique=True)
    op.create_table('roles',
                    sa.Column('id', sa.UUID(), nullable=False),
                    sa.Column('name', sa.String(), nullable=True),
                    sa.Column('description', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_roles_id'), 'roles', ['id'], unique=False)
    op.create_index(op.f('ix_roles_name'), 'roles', ['name'], unique=True)
    op.create_table('users',
                    sa.Column('id', sa.UUID(), nullable=False),
                    sa.Column('username', sa.String(), nullable=True),
                    sa.Column('email', sa.String(), nullable=True),
                    sa.Column('hashed_password', sa.String(), nullable=True),
                    sa.Column('is_active', sa.Boolean(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('loginhistory',
                    sa.Column('id', sa.UUID(), nullable=False),
                    sa.Column('user_id', sa.UUID(), nullable=True),
                    sa.Column('ip_address', sa.String(), nullable=True),
                    sa.Column('user_agent', sa.String(), nullable=True),
                    sa.Column('login_at', sa.DateTime(), nullable=True),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_loginhistory_id'), 'loginhistory', ['id'], unique=True)
    op.create_table('role_permissions',
                    sa.Column('role_id', sa.UUID(), nullable=True),
                    sa.Column('permission_id', sa.UUID(), nullable=True),
                    sa.ForeignKeyConstraint(['permission_id'], ['permissions.id'], ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ondelete='CASCADE')
                    )
    op.create_table('user_roles',
                    sa.Column('user_id', sa.UUID(), nullable=True),
                    sa.Column('role_id', sa.UUID(), nullable=True),
                    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_roles')
    op.drop_table('role_permissions')
    op.drop_index(op.f('ix_loginhistory_id'), table_name='loginhistory')
    op.drop_table('loginhistory')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_roles_name'), table_name='roles')
    op.drop_index(op.f('ix_roles_id'), table_name='roles')
    op.drop_table('roles')
    op.drop_index(op.f('ix_permissions_name'), table_name='permissions')
    op.drop_index(op.f('ix_permissions_id'), table_name='permissions')
    op.drop_table('permissions')
    # ### end Alembic commands ###
