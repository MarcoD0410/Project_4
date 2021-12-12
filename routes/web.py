"""Web Routes."""

from masonite.routes import Get, Post, Put, Delete, RouteGroup

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),

    RouteGroup([
        Get("/", "ListController@index").name("index"),
        Get("/@id", "ListController@show").name("show"),
        Post("/", "ListController@create").name("create"),
        Put("/@id", "ListController@update").name("update"),
        Delete("/@id", "ListController@destroy").name("destroy")
    ], prefix="/list", name="list")
]
