from src.graph import Graph
from copy import deepcopy

class MaximumStableMachting:
    def __init__(self):
        self.students_quantity = 0
        self.matching = dict()
        
    def output(self):
        for(project, students) in self.matching.items():
            print(f"{project} -->> {[s.id for s in students]}")

ans = MaximumStableMachting()
graph = Graph()



graph.build_graph()
for _ in range(10):
    graph.reset_graph()
    graph.GaleShapley()


    if(ans.students_quantity < graph.getStudentsSelectedQuantity()):
        ans.students_quantity = graph.getStudentsSelectedQuantity()
        ans.matching = deepcopy(graph.project_matching)




ans.output()