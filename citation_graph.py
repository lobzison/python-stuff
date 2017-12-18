"""
Provided code for Application portion of Module 1

Imports physics citation graph
"""

# general imports
import urllib2
import graph_degees_calc
import matplotlib.pyplot as plt
# Set timeout for CodeSkulptor if necessary
#import codeskulptor
# codeskulptor.set_timeout(20)


###################################
# Code for loading citation graph

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"


def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph

    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[: -1]

    print "Loaded graph with", len(graph_lines), "nodes"

    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1: -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph


def plot_in_degree_dist():
    """
    Plotting log in degree to log amount of nodes of loaded grapth
    """
    citation_graph = load_graph(CITATION_URL)

    in_degrees = graph_degees_calc.in_degree_distribution(citation_graph)

    total = float(sum(in_degrees.keys()))
    in_degrees_norm = {key: val / total for key, val in in_degrees.iteritems()}

    plt.xscale('log')
    plt.yscale('log')
    plt.plot(in_degrees_norm.keys(), in_degrees_norm.values(), "bo")
    plt.xlabel("log(In degree)")
    plt.ylabel("log(Amount of nodes)")
    plt.title("Distribution of in degree of nodes")
    plt.show()


#plot_in_degree_dist()


def plot_graph(graph):
    in_degrees = graph_degees_calc.in_degree_distribution(graph)

    total = float(sum(in_degrees.keys()))
    in_degrees_norm = {key: val / total for key, val in in_degrees.iteritems()}

    plt.xscale('log')
    plt.yscale('log')
    plt.plot(in_degrees_norm.keys(), in_degrees_norm.values(), "bo")
    plt.xlabel("log(In degree)")
    plt.ylabel("log(Amount of nodes)")
    plt.title("Distribution of in degree of nodes")
    plt.show()


def calc_average_out_degree(digraph):
    out_degree = graph_degees_calc.compute_out_degree(digraph)
    num = graph_degees_calc.node_count(digraph)
    total_out = sum(out_degree.values())
    return total_out / num

#plot_rnd_graph()

# graph_rnd = graph_degees_calc.rnd_graph
# plot_graph(graph_rnd)

#print calc_average_out_degree(load_graph(CITATION_URL))

plot_graph(graph_degees_calc.make_dpa_graph(27000, 13))

