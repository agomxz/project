"""Added Something

Revision ID: 6e8e1de168b6
Revises: 
Create Date: 2024-11-02 17:31:55.704605

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "6e8e1de168b6"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "address",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("street", sa.String(), nullable=False),
        sa.Column("city", sa.String(), nullable=False),
        sa.Column("state", sa.String(), nullable=False),
        sa.Column("zip", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_address_id"), "address", ["id"], unique=False)
    op.create_table(
        "task",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(), nullable=True),
        sa.Column("details", sa.String(), nullable=True),
        sa.Column("completed", sa.Boolean(), nullable=True),
        sa.Column("priority", sa.String(), nullable=True),
        sa.Column("date_created", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_task_id"), "task", ["id"], unique=False)
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_name", sa.String(), nullable=False),
        sa.Column("email", sa.String(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("first_name", sa.String(), nullable=True),
        sa.Column("last_name", sa.String(), nullable=True),
        sa.Column("mobile", sa.String(), nullable=True),
        sa.Column("address_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["address_id"],
            ["address.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("mobile"),
    )
    op.create_index(op.f("ix_user_address_id"), "user", ["address_id"], unique=True)
    op.create_index(op.f("ix_user_email"), "user", ["email"], unique=True)
    op.create_index(op.f("ix_user_id"), "user", ["id"], unique=False)
    op.create_index(op.f("ix_user_user_name"), "user", ["user_name"], unique=True)
    op.create_table(
        "task_assignments",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("task_id", sa.Integer(), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("accepted", sa.Boolean(), nullable=True),
        sa.ForeignKeyConstraint(
            ["task_id"],
            ["task.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_task_assignments_id"), "task_assignments", ["id"], unique=False
    )
    op.create_table(
        "task_notes",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("task_id", sa.Integer(), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("notes", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(
            ["task_id"],
            ["task.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_task_notes_id"), "task_notes", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_task_notes_id"), table_name="task_notes")
    op.drop_table("task_notes")
    op.drop_index(op.f("ix_task_assignments_id"), table_name="task_assignments")
    op.drop_table("task_assignments")
    op.drop_index(op.f("ix_user_user_name"), table_name="user")
    op.drop_index(op.f("ix_user_id"), table_name="user")
    op.drop_index(op.f("ix_user_email"), table_name="user")
    op.drop_index(op.f("ix_user_address_id"), table_name="user")
    op.drop_table("user")
    op.drop_index(op.f("ix_task_id"), table_name="task")
    op.drop_table("task")
    op.drop_index(op.f("ix_address_id"), table_name="address")
    op.drop_table("address")
    # ### end Alembic commands ###