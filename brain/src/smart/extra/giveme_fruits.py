import sys
import os
import heapq
import cv2 as cv
import numpy as np
import networkx as nx

# Add parent directory to path for helper functions
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import helper_functions as hf

SHOW_IMGS = True  # Toggle for visualization

# ------------------------- Graph Operations -------------------------
def load_fruits(filename):
    """Load fruit checkpoints from a text file"""
    fruits = set()
    with open(filename, 'r') as file:
        fruits.update(line.strip() for line in file)
    print(f"Loaded {len(fruits)} fruit checkpoints")
    return fruits

def dijkstra(graph, start):
    """Compute shortest paths from start node using Dijkstra's algorithm"""
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    heap = [(0, start)]
    
    while heap:
        cost, node = heapq.heappop(heap)
        for neighbor in graph.get(node, []):
            if (new_cost := cost + 1) < distances[neighbor]:
                distances[neighbor] = new_cost
                heapq.heappush(heap, (new_cost, neighbor))
    return distances

def build_fruit_graph(full_graph, fruits, start):
    """Create reduced graph containing only fruits and start node"""
    important_nodes = [start] + list(fruits)
    fruit_graph = {}
    
    for node in important_nodes:
        distances = dijkstra(full_graph, node)
        fruit_graph[node] = {n: distances[n] for n in important_nodes 
                           if n != node and distances[n] != float('inf')}
    
    print(f"Built fruit graph with {len(fruit_graph)} nodes")
    return fruit_graph

def greedy_collect(fruit_graph, start, fruits):
    """Collect fruits using nearest-neighbor approach"""
    path = [start]
    current = start
    
    while fruits:
        next_node = min(fruits, key=lambda x: fruit_graph[current].get(x, float('inf')))
        if fruit_graph[current].get(next_node, float('inf')) == float('inf'):
            break  # No reachable fruits left
        path.append(next_node)
        fruits.remove(next_node)
        current = next_node
    
    return len(path) - 1, path  # Return count and path

# ------------------------- Visualization -------------------------
def get_node_coordinates(node, graph):
    """Convert graph node to real-world coordinates"""
    x = float(graph.nodes[node]['x'])
    y = float(graph.nodes[node]['y'])
    return hf.mR2pix(hf.mL2mR(np.array([x, y])))

def visualize_path(path, graph, map_image, fruit_order, frame_delay=300):
    """Animate path drawing with OpenCV"""
    # Base map setup
    base_img = cv.imread(map_image)
    fruit_labels = {fruit: str(i+1) for i, fruit in enumerate(fruit_order[1:])}
    
    # Draw all nodes
    for node in graph.nodes:
        pos = get_node_coordinates(node, graph)
        cv.circle(base_img, pos, 5, (0, 0, 255), -1)
        cv.putText(base_img, node, pos, cv.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
    
    # Add fruit labels
    for fruit, label in fruit_labels.items():
        if fruit in graph.nodes:
            pos = get_node_coordinates(fruit, graph)
            cv.putText(base_img, label, (pos[0]+5, pos[1]-5), 
                       cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    
    # Animate path progression
    path_coords = [get_node_coordinates(n, graph) for n in path]
    for i in range(1, len(path_coords)):
        frame = base_img.copy()
        
        # Draw path segments
        for j in range(1, i+1):
            start_pt = path_coords[j-1]
            end_pt = path_coords[j]
            cv.line(frame, start_pt, end_pt, (200, 200, 0), 4, lineType=cv.LINE_AA)
            cv.circle(frame, end_pt, 4, (255, 0, 0), 1)
        
        # Draw current position marker
        cv.circle(frame, path_coords[i], 20, (0, 139, 243), -1)
        
        if SHOW_IMGS:
            cv.imshow('Path Animation', frame)
            if cv.waitKey(frame_delay) == 27:  # ESC to exit
                break
    
    if SHOW_IMGS:
        cv.waitKey(0)
        cv.destroyAllWindows()

# ------------------------- Main Program -------------------------
def reconstruct_full_path(high_level_path, graph):
    """Convert high-level fruit path to detailed node path"""
    detailed_path = []
    
    for i in range(len(high_level_path)-1):
        start, end = high_level_path[i], high_level_path[i+1]
        
        # Calculate path segment using Dijkstra
        distances = {node: float('inf') for node in graph}
        predecessors = {}
        distances[start] = 0
        heap = [(0, start)]
        
        while heap:
            cost, node = heapq.heappop(heap)
            for neighbor in graph.get(node, []):
                if (new_cost := cost + 1) < distances[neighbor]:
                    distances[neighbor] = new_cost
                    predecessors[neighbor] = node
                    heapq.heappush(heap, (new_cost, neighbor))
        
        # Backtrack to get path
        if end not in predecessors:
            print(f"No path between {start} and {end}")
            continue
        
        segment = []
        current = end
        while current != start:
            segment.append(current)
            current = predecessors[current]
        detailed_path.extend([start] + segment[::-1][:-1])  # Avoid duplicates
    
    return detailed_path + [end]

if __name__ == "__main__":
    # Configuration
    GRAPH_FILE = "final_graph.graphml"
    FRUITS_FILE = "fruits.txt"
    MAP_FILE = "../data/2024_VerySmall.png"
    START_NODE = "472"
    
    # Load data
    road_graph = nx.read_graphml(GRAPH_FILE)
    graph_dict = {str(n): [str(neigh) for neigh in road_graph.neighbors(n)] 
                for n in road_graph.nodes}
    fruits = load_fruits(FRUITS_FILE)
    
    # Calculate optimal fruit path
    fruit_gr = build_fruit_graph(graph_dict, fruits, START_NODE)
    _, best_path = greedy_collect(fruit_gr, START_NODE, set(fruits))
    
    print(f"\nCollected {len(best_path)-1} fruits")
    print("Optimal path:", " → ".join(best_path))
    
    # Generate detailed path and visualize
    full_path = reconstruct_full_path(best_path, graph_dict)
    visualize_path(full_path, road_graph, MAP_FILE, best_path,250)