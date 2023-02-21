class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self,level):
        if self.get_level() > level:
            return
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(level)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_product_tree():
    world = TreeNode("Global")

    india = TreeNode("India")
    india.add_child(TreeNode("Gujarat"))
    india.add_child(TreeNode("Karnataka"))


    usa = TreeNode("USA")
    usa.add_child(TreeNode("New Jersey"))
    usa.add_child(TreeNode("California"))

    world.add_child(india)
    world.add_child(usa)

    return world
if __name__ == '__main__':
    root_node = build_product_tree()
    root_node.print_tree(4)