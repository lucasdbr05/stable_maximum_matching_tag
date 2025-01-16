from src.graph import Graph
from src.output import Output
from copy import deepcopy
class MaximumStableMachting:
    def __init__(self):
        self.students_quantity = 0
        self.matching = dict()

ans = MaximumStableMachting()
output = Output()
graph = Graph(output)


graph.build_graph()

for i in range(10):
    output.print(f"{"\n" if i>0 else ""}{i+1}-th iteration")
    graph.GaleShapley()
    print(graph.getStudentsSelectedQuantity())
    if(ans.students_quantity < graph.getStudentsSelectedQuantity()):
        ans.students_quantity = graph.getStudentsSelectedQuantity()
        ans.matching = deepcopy(graph.project_matching)

    graph.reset_graph()

output.print_result(ans.students_quantity, ans.matching)