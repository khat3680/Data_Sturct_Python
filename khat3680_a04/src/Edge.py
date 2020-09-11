"""
-------------------------------------------------------
[program Edge]
-------------------------------------------------------
Author:  Anshul Khatri
ID:      193313680
Email:   khat3680@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-02-06"
-------------------------------------------------------
"""

class Edge:
    """
    Contains information about an graph edge.
    nodes: names of edge nodes stored in alphabetical order
    distance: arbitrary numeric distance between nodes
    """

    def __init__(self, nodes, distance):
        """
        -------------------------------------------------------
        Initializes an Edge object.
        Use: e = Edge(nodes, distance)
        -------------------------------------------------------
        Parameters:
            nodes - list of node names (list of str, len(nodes) == 2)
            distance - distance between start and end (int > 0)
        Returns:
            None
        -------------------------------------------------------
        """
        assert len(nodes) == 2, "Must have two node names"

        # Sort the node names into alphabetical order
        self.nodes = nodes
        self.distance = distance
        return

    def reverse(self):
        """
        -------------------------------------------------------
        Returns an Edge object with the start and end nodes reversed.
        Use: e2 = e1.reverse()
        -------------------------------------------------------
        Returns:
            new_edge - an Edge object with the node names swapped (Edge)
        -------------------------------------------------------
        """
        new_edge = Edge([self.nodes[1], self.nodes[0]], self.distance)
        return new_edge

    def __str__(self):
        """
        -------------------------------------------------------
        Returns a string representation of the edge.
        Use: s = str(e) or print(e)
        -------------------------------------------------------
        Returns:
            A string representation of the edge.
        -------------------------------------------------------
        """
        return "{} - {}: {}".format(self.nodes[0], self.nodes[1], self.distance)

    def __eq__(self, target):
        """
        -------------------------------------------------------
        Compares two edges for equality of distance.
        Use: source == target
        -------------------------------------------------------
        Parameters:
            target - another edge (Edge)
        Returns:
            Whether the distance of two edges are the same. (bool)
        -------------------------------------------------------
        """
        return self.distance == target.distance

    def __lt__(self, target):
        """
        -------------------------------------------------------
        Compares distance of two edges.
        Use: source < target
        -------------------------------------------------------
        Parameters:
            target - another edge (Edge)
        Returns:
            True if distance of edge < distance of target,
                False otherwise. (bool)
        -------------------------------------------------------
        """
        return self.distance < target.distance

    def le(self, target):
        """
        -------------------------------------------------------
        Compares distance of two edges.
        Use: source <= target
        -------------------------------------------------------
        Parameters:
            target - another edge (Edge)
        Returns:
            True if distance of edge <= distance of target,
                False otherwise. (bool)
        -------------------------------------------------------
        """
        return self == target or self < target

    def start(self):
        """
        -------------------------------------------------------
        Returns name of starting node of edge.
        Use: edge = source.start()
        -------------------------------------------------------
        Returns:
            Name of starting node of edge (str)
        -------------------------------------------------------
        """
        return self.nodes[0]

    def end(self):
        """
        -------------------------------------------------------
        Returns name of ending node of edge.
        Use: edge = source.end()
        -------------------------------------------------------
        Returns:
            Name of ending node of edge (str)
        -------------------------------------------------------
        """
        return self.nodes[1]


