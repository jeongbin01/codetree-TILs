class Node:
    def __init__(self, id, color, max_depth):
        self.id = id
        self.color = color
        self.max_depth = max_depth
        self.children = []

class Tree:
    def __init__(self):
        self.nodes = {}

    def add_node(self, id, parent_id, color, max_depth):
        if parent_id == -1:
            self.nodes[id] = Node(id, color, max_depth)
        else:
            parent = self.nodes.get(parent_id)
            if parent and self._can_add(parent, max_depth):
                new_node = Node(id, color, max_depth)
                parent.children.append(new_node)
                self.nodes[id] = new_node

    def _can_add(self, parent, max_depth):
        return len(parent.children) + 1 <= parent.max_depth and max_depth <= parent.max_depth

    def change_color(self, node_id, new_color):
        node = self.nodes.get(node_id)
        if node:
            self._dfs_change_color(node, new_color)

    def _dfs_change_color(self, node, new_color):
        node.color = new_color
        for child in node.children:
            self._dfs_change_color(child, new_color)

    def get_color(self, node_id):
        return self.nodes[node_id].color if node_id in self.nodes else None

    def calculate_score(self):
        score = 0
        for node in self.nodes.values():
            score += self._calculate_node_value(node) ** 2
        return score

    def _calculate_node_value(self, node):
        distinct_colors = set()
        self._dfs_collect_colors(node, distinct_colors)
        return len(distinct_colors)

    def _dfs_collect_colors(self, node, distinct_colors):
        distinct_colors.add(node.color)
        for child in node.children:
            self._dfs_collect_colors(child, distinct_colors)

# 명령 입력 받기
Q = int(input())
tree = Tree()

for _ in range(Q):
    command = input().split()
    if command[0] == '100':  # 노드 추가
        id, parent_id, color, max_depth = map(int, command[1:])
        tree.add_node(id, parent_id, color, max_depth)
    elif command[0] == '200':  # 색상 변경
        id, new_color = map(int, command[1:])
        tree.change_color(id, new_color)
    elif command[0] == '300':  # 색상 조회
        id = int(command[1])
        print(tree.get_color(id))
    elif command[0] == '400':  # 점수 계산
        print(tree.calculate_score())