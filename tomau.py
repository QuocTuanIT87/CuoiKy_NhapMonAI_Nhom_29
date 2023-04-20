graph = {
    'Thành phố Thủ Đức': ['Quận 1', 'Quận 4', 'Quận 7', 'Quận 12', 'Quận Bình Thạnh'],
    'Quận 1': ['Quận 3', 'Quận 4', 'Quận 5', 'Thành phố Thủ Đức', 'Quận Bình Thạnh', 'Quận Phú Nhuận'],
    'Quận 3': ['Quận 1', 'Quận 10', 'Quận Phú Nhuận', 'Quận Tân Bình'],
    'Quận 4': ['Thành phố Thủ Đức', 'Quận 1', 'Quận 5', 'Quận 7', 'Quận 8'],
    'Quận 5': ['Quận 1', 'Quận 4', 'Quận 6', 'Quận 8', 'Quận 10', 'Quận 11'],
    'Quận 6': ['Quận 5', 'Quận 8', 'Quận 11', 'Quận Bình Tân', 'Quận Tân Phú'],
    'Quận 7': ['Thành phố Thủ Đức', 'Quận 4', 'Quận 8', 'Huyện Bình Chánh', 'Huyện Nhà Bè'],
    'Quận 8': ['Quận 4', 'Quận 5', 'Quận 6', 'Quận 7', 'Quận Bình Tân', 'Huyện Bình Chánh'],
    'Quận 10': ['Quận 3', 'Quận 5', 'Quận 11', 'Quận Tân Bình'],
    'Quận 11': ['Quận 5', 'Quận 6', 'Quận 10', 'Quận Tân Bình', 'Quận Tân Phú'],
    'Quận 12': ['Thành phố Thủ Đức', 'Quận Bình Tân', 'Quận Bình Thạnh', 'Quận Gò Vấp', 'Quận Tân Bình', 'Quận Tân Phú', 'Huyện Hóc Môn'],
    'Quận Bình Tân': ['Quận 6', 'Quận 8', 'Quận 12', 'Quận Tân Phú', 'Huyện Bình Chánh', 'Huyện Hóc Môn'],
    'Quận Bình Thạnh': ['Thành phố Thủ Đức', 'Quận 1', 'Quận 12', 'Quận Gò Vấp', 'Quận Phú Nhuận'],
    'Quận Gò Vấp': ['Quận 12', 'Quận Bình Thạnh', 'Quận Phú Nhuận', 'Quận Tân Bình'],
    'Quận Phú Nhuận': ['Quận 1', 'Quận 3', 'Quận Bình Thạnh', 'Quận Gò Vấp', 'Quận Tân Bình'],
    'Quận Tân Bình': ['Quận 3', 'Quận 10', 'Quận 11', 'Quận 12', 'Quận Gò Vấp', 'Quận Phú Nhuận', 'Quận Tân Phú'],
    'Quận Tân Phú': ['Quận 6', 'Quận 11', 'Quận 12', 'Quận Bình Tân', 'Quận Tân Bình'],
    'Huyện Bình Chánh': ['Quận 7', 'Quận 8', 'Quận Bình Tân', 'Huyện Hóc Môn', 'Huyện Nhà Bè'],
    'Huyện Cần Giờ': ['Huyện Nhà Bè'],
    'Huyện Củ Chi': ['Huyện Hóc Môn'],
    'Huyện Hóc Môn': ['Quận 12', 'Quận Bình Tân', 'Huyện Bình Chánh', 'Huyện Củ Chi'],
    'Huyện Nhà Bè': ['Quận 7', 'Huyện Bình Chánh', 'Huyện Cần Giờ']
}

# Phương pháp thử


def graph_coloring_trial(graph, colors):
    nodes = sorted(list(graph.keys()))
    node_colors = {}
    for node in nodes:
        available_colors = colors.copy()
        for neighbor in graph[node]:
            if neighbor in node_colors:
                if node_colors[neighbor] in available_colors:
                    available_colors.remove(node_colors[neighbor])
        node_colors[node] = available_colors[0]
    return node_colors

# Phương pháp quay lui


def graph_coloring_backtrack(graph, colors):
    nodes = sorted(list(graph.keys()))
    node_colors = {}
    return backtrack_coloring(graph, nodes, node_colors, colors)


def backtrack_coloring(graph, nodes, node_colors, colors):
    if len(node_colors) == len(nodes):
        return node_colors
    node = select_unassigned_node(graph, node_colors)
    for color in colors:
        if is_color_legal(graph, node, color, node_colors):
            node_colors[node] = color
            result = backtrack_coloring(graph, nodes, node_colors, colors)
            if result is not None:
                return result
            del node_colors[node]
    return None


def select_unassigned_node(graph, node_colors):
    nodes = sorted(list(graph.keys()))
    for node in nodes:
        if node not in node_colors:
            return node
    return None


def is_color_legal(graph, node, color, node_colors):
    for neighbor in graph[node]:
        if neighbor in node_colors:
            if node_colors[neighbor] == color:
                return False
    return True


# Khởi chạy thuật toán tô màu đồ thị

colors = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
node_colors_trial = graph_coloring_trial(graph, colors)
node_colors_backtrack = graph_coloring_backtrack(graph, colors)

# In kết quả

print("Phương pháp thử: ")
for node, color in node_colors_trial.items():
    print(node + ':', 'màu', color)

print("\nPhương pháp quay lui: ")
for node, color in node_colors_backtrack.items():
    print(node + ':', 'màu', color)
