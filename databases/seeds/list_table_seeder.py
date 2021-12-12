"""ListTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.List import List


class ListTableSeeder(Seeder):
    def run(self):
        List.create({"item": "Milk", "amount": "3"})
        List.create({"item": "rice", "amount": "2"})
        List.create({"item": "eggs", "amount": "128"})