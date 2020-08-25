class Vertex:
    def __init__(self,data):
        self.data = data
        self.edges = {}

    def add_edge(self,data,cost,time):
        self.edges[data] = {"cost":cost,"time":time}

    def get_edges(self):
        return self.edges

    def get_edge(self,vertex_b):
        return self.edges[vertex_b.data]

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self,vertex):
        self.vertices[vertex.data] = vertex

    def add_edge(self,vertex_a,vertex_b,cost,time):
        self.vertices[vertex_a.data].add_edge(vertex_b.data,cost,time)
        self.vertices[vertex_b.data].add_edge(vertex_a.data,cost,time)

    def path_exists(self,vertex_a,vertex_b):
        edges = vertex_a.get_edges()
        for i in edges:
            if i == vertex_b:
                return True
        return False

    def find_vertex(self,city):
        for i in self.vertices:
            if i == city:
                vertex = self.vertices[i]
                return vertex

    def get_cities(self,from_city = None):
        cities = list(self.vertices)
        final_cities = []
        if from_city != None:
            final_cities = [self.vertices[i] for i in cities if i != from_city and self.path_exists(from_city,i)]
        else:
            final_cities = [self.vertices[i] for i in cities]
        return final_cities


flights = Graph()

kuwait = Vertex("Kuwait")
dubai = Vertex("Dubai")
colombo = Vertex("Colombo")
doha = Vertex("Doha")
male = Vertex("Male")
tokyo = Vertex("Tokyo")
oslo = Vertex("Oslo")

flights.add_vertex(kuwait)
flights.add_vertex(dubai)
flights.add_vertex(colombo)
flights.add_vertex(doha)
flights.add_vertex(male)
flights.add_vertex(tokyo)
flights.add_vertex(oslo)

flights.add_edge(kuwait, dubai, 120, 2)
flights.add_edge(kuwait, colombo, 200, 4)
flights.add_edge(colombo, male, 60, 1)
flights.add_edge(dubai, doha, 100, 1.5)
flights.add_edge(doha, tokyo, 500, 11)
flights.add_edge(dubai, oslo, 300, 6)

cities = flights.get_cities()
count = 1
print("\n------------Cities------------")
for i in cities:
    print("%s- %s"%(count,i.data))
    count+= 1

from_city = input("\ninsert the city you're travelling from: ")
from_vertex = flights.find_vertex(from_city)

cities_available = flights.get_cities(from_vertex)
count = 1
print("\n--------Cities You Can Travel To--------")
for i in cities_available:
    print("%s- %s"%(count,i.data))
    count+= 1

to_city = input("\ninsert the city you're travelling to: ")
to_vertex = flights.find_vertex(to_city)
if to_vertex in cities_available:
    print("\nYour flight's duration: %s\nYour flight's cost: %s"%(from_vertex.get_edge(to_vertex)["time"],from_vertex.get_edge(to_vertex)["cost"]))
