import networkx as nx

#Grafo dirigido para los proyectos
proyectos = nx.DiGraph()

#Añadir proyectos
proyectos.add_node("Proyecto A", habilidades_requeridas=["Python"], prioridad="Alta")
proyectos.add_node("Proyecto B", habilidades_requeridas=["JavaScript"], prioridad="Media")
proyectos.add_node("Proyecto C", habilidades_requeridas=["HTML"], prioridad="Baja")
proyectos.add_node("Proyecto D", habilidades_requeridas=["CSS"], prioridad="Alta")
proyectos.add_node("Proyecto E", habilidades_requeridas=["Django"], prioridad="Media")

#Prioridad de los proyectos
proyectos.add_edge("Proyecto A", "Proyecto B")
proyectos.add_edge("Proyecto A", "Proyecto C")
proyectos.add_edge("Proyecto B", "Proyecto D")
proyectos.add_edge("Proyecto C", "Proyecto E")
proyectos.add_edge("Proyecto D", "Proyecto E")

#Arbol
recursos = nx.DiGraph()

#Nodos de desarrolladores y nivel de experiencia
recursos.add_node("Gerente", role="Manager", experiencia="Senior")
recursos.add_node("Desarrollador 1", habilidades=["Python", "JavaScript"], experiencia="Senior")
recursos.add_node("Desarrollador 2", habilidades=["Python", "HTML"], experiencia="Junior")
recursos.add_node("Desarrollador 3", habilidades=["CSS", "HTML"], experiencia="Mid")
recursos.add_node("Desarrollador 4", habilidades=["Django", "JavaScript"], experiencia="Mid")
recursos.add_node("Desarrollador 5", habilidades=["Django", "CSS"], experiencia="Senior")

#Jerarquia
recursos.add_edge("Gerente", "Desarrollador 1")
recursos.add_edge("Gerente", "Desarrollador 5")
recursos.add_edge("Desarrollador 1", "Desarrollador 2")
recursos.add_edge("Desarrollador 1", "Desarrollador 3")
recursos.add_edge("Desarrollador 5", "Desarrollador 4")

#DFS y BFS
dfs_orden = list(nx.dfs_postorder_nodes(proyectos, source="Proyecto A"))
bfs_orden = list(nx.bfs_edges(proyectos, source="Proyecto A"))

print("Orden de ejecución de proyectos según DFS:", dfs_orden)
print("Niveles de proyecto según BFS:", [edge for edge in bfs_orden])