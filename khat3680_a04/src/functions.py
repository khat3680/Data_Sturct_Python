"""
-------------------------------------------------------
[program functions]
-------------------------------------------------------
Author:  Anshul Khatri
ID:      193313680
Email:   khat3680@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-02-06"
-------------------------------------------------------
"""

from Priority_Queue_array import Priority_Queue

def pq_split_key(source, key):
    """
    -------------------------------------------------------
    Splits a priority queue into two depending on an external
    priority key. The source priority queue is empty when the method
    ends.
    Use: target1, target2 = pq_split_key(source, key)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
        key - a data object (?)
    Returns:
        target1 - a priority queue that contains all values
            with priority higher than key (Priority_Queue)
        target2 - priority queue that contains all values with
            priority lower than or equal to key (Priority_Queue)
    -------------------------------------------------------
    """
    target1 = Priority_Queue()
    target2 = Priority_Queue()
    while source.is_empty()==False:
        value = source.remove()
        
        if value<key:

            target1.insert(value)
        else:
            target2.insert(value)           
    return target1, target2

def pq_split_alt(source):
    """
    -------------------------------------------------------
    Splits a priority queue into two with values going to alternating
    priority queues. The source priority queue is empty when the method
    ends. The order of the values in source is preserved.
    Use: target1, target2 = pq_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
    Returns:
        target1 - a priority queue that contains alternating values
            from source (Priority_Queue)
        target2 - priority queue that contains  alternating values
            from source (Priority_Queue)
    -------------------------------------------------------
    """
    target1 = Priority_Queue()
    target2 = Priority_Queue()
    i = 1
    while source.is_empty()==False:
        if i==1:
            target1.insert(source.remove())
            i=2
        elif i==2:
            target2.insert(source.remove())
            i=1
    return target1, target2
            
from Graph import Graph          
def prims(graph, start_node):
    """
    -------------------------------------------------------
    Applies Prim's Algorithm to a graph.
    Use: edges, total = prims(graph, node)
    -------------------------------------------------------
    Parameters:
        graph - graph to evaluate (Graph)
        start_node - name of node to start evaluation from (str)
    Returns:
        edges - the list of the edges traversed (list of Edge)
        total - total distance of all edges traversed (int)
    -------------------------------------------------------
    """
    
    total = 0
    edges = []
    all_edges = Priority_Queue()
    done_nodes = [start_node]
    node_names = graph.node_names()
    while len(done_nodes)!=len(node_names):
        done_nodes.append(start_node)
        
        node_edges = graph.edges_by_node(start_node)
        
        for edge in node_edges:
            if edge.end() not in done_nodes:
                all_edges.insert(edge)
        ed = all_edges.remove()
        while ed.end() in done_nodes and all_edges.is_empty()==False:
            ed = all_edges.remove()
        if all_edges.is_empty()==False:
            edges.append(ed)
        
        start_node = ed.end()
    
    for i in edges:
        total+=i.distance
    
    return edges, total
                

    
    
    
    