""" A ListController Module """

from masonite.controllers import Controller
from masonite.request import Request
from app.List import List


class ListController(Controller):
    """Class Docstring Description
    """

    def __init__(self, request: Request):
        self.request = request

    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", BlogController)
        """
        id = self.request.param("id")
        return List.find(id)


        pass

    def index(self):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", TodoController)
        """
        return List.all()

        pass


    def create(self):
        item = self.request.input("item")
        amount = self.request.input("amount")
        list = List.create({"item": item, "amount": amount})
        return list


        pass

    

    def update(self):
        item = self.request.input("item")
        amount = self.request.input("amount")
        id = self.request.param("id")
        List.where("id", id).update({"item": item, "amount": amount})
        return List.where("id", id).get()


        pass

    def destroy(self):
        id = self.request.param("id")
        list = List.where("id", id).get()
        List.where("id", id).delete()
        return list

        pass