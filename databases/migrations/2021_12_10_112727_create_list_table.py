"""CreateListTable Migration."""

from masoniteorm.migrations import Migration


class CreateListTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("list") as table:
            table.increments("id")
            table.string("item")
            table.string("amount")
            table.timestamps()


    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("list")
