"""init lessons and teachers

Revision ID: 141a168772f6
Revises: 9940720af183
Create Date: 2020-11-26 01:18:52.153413

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '141a168772f6'
down_revision = '9940720af183'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lessons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teachers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('middle_name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('teachers')
    op.drop_table('lessons')
    # ### end Alembic commands ###
