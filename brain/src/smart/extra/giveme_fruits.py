import sys
import os
import heapq
import cv2 as cv
import numpy as np
import networkx as nx

# Add parent directory to path for helper functions
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import helper_functions as hf
from path_planning4_mod import PathPlanning 
SHOW_IMGS = True

# ------------------------- Load & Utility -------------------------
def load_fruits(filename):
    fruits = set()
    with open(filename, 'r') as file:
        fruits.update(line.strip() for line in file)
    print(f"Loaded {len(fruits)} fruit checkpoints")
    return fruits

def get_node_coordinates(node, graph):
    data = graph.nodes[node]
    x = float(data.get('x', data.get('d0')))
    y = float(data.get('y', data.get('d1')))
    return hf.mR2pix(hf.mL2mR(np.array([x, y])))

def resize_image(image, max_width=1000, max_height=800):
    h, w = image.shape[:2]
    scale = min(max_width / w, max_height / h)
    if scale < 1:
        image = cv.resize(image, (int(w * scale), int(h * scale)), interpolation=cv.INTER_AREA)
    return image

# ------------------------- Graph Algorithms -------------------------
def dijkstra(graph, start):
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
    important = [start] + list(fruits)
    fruit_graph = {}
    for node in important:
        dist = dijkstra(full_graph, node)
        fruit_graph[node] = {n: dist[n] for n in important if n != node and dist[n] != float('inf')}
    print(f"Built fruit graph with {len(fruit_graph)} nodes")
    return fruit_graph

def greedy_collect(fruit_graph, start, fruits):
    path = [start]
    current = start
    while fruits:
        next_node = min(fruits, key=lambda x: fruit_graph[current].get(x, float('inf')))
        if fruit_graph[current].get(next_node, float('inf')) == float('inf'):
            break
        path.append(next_node)
        fruits.remove(next_node)
        current = next_node
    return len(path) - 1, path

# ------------------------- Path Reconstruction -------------------------
def reconstruct_full_path(high_level_path, graph):
    full = []
    for i in range(len(high_level_path) - 1):
        start, end = high_level_path[i], high_level_path[i + 1]
        distances = {node: float('inf') for node in graph}
        prev = {}
        distances[start] = 0
        heap = [(0, start)]
        while heap:
            cost, node = heapq.heappop(heap)
            for neighbor in graph.get(node, []):
                if (new_cost := cost + 1) < distances[neighbor]:
                    distances[neighbor] = new_cost
                    prev[neighbor] = node
                    heapq.heappush(heap, (new_cost, neighbor))
        if end not in prev:
            print(f"No path between {start} and {end}")
            continue
        segment = []
        cur = end
        while cur != start:
            segment.append(cur)
            cur = prev[cur]
        full.extend([start] + segment[::-1][:-1])
    return full + [high_level_path[-1]]

# ------------------------- Visualization -------------------------
def visualize_path(path, graph, map_image, fruit_order, frame_delay=300):
    base_img = cv.imread(map_image)
    fruit_labels = {fruit: str(i+1) for i, fruit in enumerate(fruit_order[1:])}

    for node in graph.nodes:
        pos = get_node_coordinates(node, graph)
        cv.circle(base_img, pos, 5, (0, 0, 255), -1)
        cv.putText(base_img, node, pos, cv.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)

    for fruit, label in fruit_labels.items():
        if fruit in graph.nodes:
            pos = get_node_coordinates(fruit, graph)
            cv.putText(base_img, label, (pos[0]+5, pos[1]-5),
                       cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    path_coords = [get_node_coordinates(n, graph) for n in path]
    for i in range(1, len(path_coords)):
        frame = base_img.copy()
        for j in range(1, i + 1):
            pt1 = path_coords[j - 1]
            pt2 = path_coords[j]
            cv.line(frame, pt1, pt2, (200, 200, 0), 4, lineType=cv.LINE_AA)
            cv.circle(frame, pt2, 4, (255, 0, 0), 1)
        cv.circle(frame, path_coords[i], 20, (0, 139, 243), -1)

        if SHOW_IMGS:
            resized = resize_image(frame)
            cv.imshow('Path Animation', resized)
            if cv.waitKey(frame_delay) == 27:
                break

    if SHOW_IMGS:
        final = resize_image(base_img)
        cv.imshow('Path Animation', final)
        cv.waitKey(0)
        cv.destroyAllWindows()

def compute_optimal_path(start_node='472'):
    graph_file = os.path.join(os.path.dirname(__file__), "final_graph.graphml")
    fruits_file = os.path.join(os.path.dirname(__file__), "fruits.txt")
    map_file = os.path.join(os.path.dirname(__file__), "../data/2024_VerySmall.png")

    if not os.path.exists(graph_file):
        raise FileNotFoundError(f"Graph file not found: {graph_file}")
    
    road_graph = nx.read_graphml(graph_file)
    graph_dict = {str(n): [str(neigh) for neigh in road_graph.neighbors(n)] for n in road_graph.nodes}
    fruits = load_fruits(fruits_file)

    fruit_graph = build_fruit_graph(graph_dict, fruits, str(start_node))
    _, best_path = greedy_collect(fruit_graph, str(start_node), set(fruits))

    path = [int(node) for node in best_path]
    return path


# ------------------------- Optional Execution -------------------------
if __name__ == "__main__":
    GRAPH_FILE = "final_graph.graphml"
    FRUITS_FILE = "fruits.txt"
    MAP_FILE = "../data/2024_VerySmall.png"
    START_NODE = '94'

    # Compute and visualize
    path = compute_optimal_path(START_NODE)
    print(f"\nCollected {len(path)-1} fruits")
    print("Optimal path:", " → ".join(map(str, path)))
    print(path)

    # Reconstruct full and visualize
    road_graph = nx.read_graphml(GRAPH_FILE)
    graph_dict = {str(n): [str(neigh) for neigh in road_graph.neighbors(n)] for n in road_graph.nodes}
    full_path = reconstruct_full_path(list(map(str, path)), graph_dict)
    visualize_path(full_path, road_graph, MAP_FILE, list(map(str, path)), 250)
