# people.py
from bulbs.config import Config, DEBUG
from bulbs.model import Node, Relationship
from bulbs.property import String, Integer, DateTime
from bulbs.utils import current_datetime


class Person(Node):

    element_type = "person"

    name = String(nullable=False)
    age = Integer()


class Knows(Relationship):

    label = "knows"

    created = DateTime(default=current_datetime, nullable=False)

from bulbs.rexster import Graph

config = Config("http://titan:8182")
config.set_logger(DEBUG)
g = Graph(config)
g.add_proxy("people", Person)
g.add_proxy("knows", Knows)

james = g.people.create(name="James")
julie = g.people.create(name="Julie")
g.knows.create(james, julie)
