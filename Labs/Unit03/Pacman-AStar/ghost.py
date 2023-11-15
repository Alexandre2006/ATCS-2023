import pygame
import math

class Ghost(pygame.sprite.Sprite):
    TYPES = {"1": "Blinky", "2": "Pinky", "3": "Inky", "4": "Clyde"}
    RIGHT, LEFT, UP, DOWN = 0, 1, 2, 3

    def __init__(self, game, ghost_type, x=50, y=50):
        super().__init__()

        self.game = game
        self.name = self.TYPES[ghost_type]

        # Set up animations
        self.anim = []
        self.anim_count = 0
        self.anim_option = self.UP
        self.load_images()

        # Load initial image
        self.image = self.anim[self.UP][0]
        self.rect = self.image.get_rect()

        # Set rectangle
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect.x = x - self.width/2
        self.rect.y = y - self.height/2

        # Set velocity
        self.vel_y = 0
        self.vel_x = 0

        # Set constants for speed
        self.speed = 8

        # Set the current node to Null
        self.spawn_node = None
        self.scatter_node = None
        self.current_node = None

        # Set the path
        self.path = []

    def set_spawn_node(self, node):
        """
        Assigns the spawn node and sets the 
        current node to it.
        Args:
            node (PathNode): The node to spawn at
        """
        self.spawn_node = node
        self.set_current_node(node)
    
    def set_current_node(self, node):
        self.current_node = node
    
    def set_scatter_node(self, node):
        self.scatter_node = node

    def load_images(self):
        """
        Loads all images for animations
        """
        right_anim = self.load_image_directions("right")
        left_anim = self.load_image_directions("left")
        up_anim = self.load_image_directions("up")
        down_anim = self.load_image_directions("down")

        self.anim.append(right_anim)
        self.anim.append(left_anim)
        self.anim.append(up_anim)
        self.anim.append(down_anim)
    
    def load_image_directions(self, dir):
        """
        Loads the animations for the specific ghost
        in the provided direction
        Args:
            dir (String): "right", "left", "up", or "down"

        Returns:
            list: A list of the animation images
        """
        filepath = "Assets/" + self.name + "/" + dir
        anim = []
        for i in ["0", "1"]:
            anim.append(pygame.image.load(filepath+i+".png"))
        return anim

    def find_scatter_path(self):
        """
        Finds the path from the current node 
        to the ghost's spawn node
        """
        # self.find_dfs_path_helper(self.current_node, self.scatter_node)
        # self.find_bfs_path_helper(self.current_node, self.scatter_node)
        self.find_astar_path_helper(self.current_node, self.scatter_node)

    def find_dfs_path_helper(self, start_node, end_node):
        """
        Finds a path from the start_node to the end_node
        using DFS
        Args:
            start_node (PathNode): Node to start at
            end_node (PathNode): Node to end at
        """
        # Tracking vars
        visited = []
        stack = []
        parents = {}

        # Add start node to stack
        stack.append(start_node)
        
        while len(stack) != 0:
            # Pop off the top of the stack
            current_node = stack.pop()

            # If we're at the end node, we're done
            if current_node == end_node:
                break
            
            # Add all neighbors to the stack
            for neighbor in current_node.adjacent_nodes:
                if neighbor in visited:
                    continue
                visited.append(neighbor)
                parents[neighbor] = current_node
                stack.append(neighbor)
        
        # Reset the path
        self.path = []

        # Reverse path
        while current_node != start_node:
            self.path.append(current_node)
            current_node = parents[current_node]
        
        self.path.reverse()

    def find_bfs_path_helper(self, start_node, end_node):
        """
        Finds a path from the start_node to the end_node
        using BFS
        Args:
            start_node (PathNode): Node to start at
            end_node (PathNode): Node to end at
        """
        # Tracking vars
        visited = []
        stack = []
        parents = {}

        # Add start node to stack
        stack.append(start_node)
        
        while len(stack) != 0:
            # Pop off the top of the stack
            current_node = stack.pop(0)

            # If we're at the end node, we're done
            if current_node == end_node:
                break
            
            # Add all neighbors to the stack
            for neighbor in current_node.adjacent_nodes:
                if neighbor in visited:
                    continue
                visited.append(neighbor)
                parents[neighbor] = current_node
                stack.append(neighbor)
        
        # Reset the path
        self.path = []

        # Reverse path
        while current_node != start_node:
            self.path.append(current_node)
            current_node = parents[current_node]
        
        self.path.reverse()

    def find_astar_path_helper(self, start_node, end_node):
        """
        Finds a path from the start_node to the end_node
        using A* Search
        Args:
            start_node (PathNode): Node to start at
            end_node (PathNode): Node to end at
        """
        node_info = {}
        open_set = []
        parents = {}

        for node in self.game.path_nodes:
            # Initializes the info for every node
            node_info[node] = {"f": 0,
                               "g": 0,
                               "h": 0,
                               "in_closed_set": False}
        
        # Loop through all nodes and calculate the heuristic
        for node in self.game.path_nodes:
            node_info[node]["h"] = self.euclidean(node, end_node)
        
        # Main pathfinding loop
        open_set.append(start_node)
        while len(open_set) != 0:
            # Find the node with the lowest f value
            current_node = open_set[0]
            for node in open_set:
                if node_info[node]["f"] < node_info[current_node]["f"]:
                    current_node = node
            
            # Exit early if at the end node
            if current_node == end_node:
                break
            
            # Add current node to closed set
            open_set.remove(current_node)
            node_info[current_node]["in_closed_set"] = True

            # Add neighbors to open set
            for neighbor in current_node.adjacent_nodes:
                # ignore neighbors in the closed set
                if node_info[neighbor]["in_closed_set"]:
                    continue
                
                # Calculate g value
                g = node_info[current_node]["g"] + self.euclidean(current_node, neighbor)

                # if the new g value is greater than the old one, ignore it
                if neighbor in open_set and g >= node_info[neighbor]["g"]:
                    continue
                
                # Otherwise, update the neighbor's info
                parents[neighbor] = current_node
                node_info[neighbor]["g"] = g
                node_info[neighbor]["f"] = g + node_info[neighbor]["h"]

                # add neighbor to open set if not in open set
                if neighbor not in open_set:
                    open_set.append(neighbor)
            
        # Reset & Calculate the path
        self.path = []
        while current_node != start_node:
            self.path.append(current_node)
            current_node = parents[current_node]
        
        # Reverse path (because initially it goes from end to start :( )
        self.path.reverse()


    def euclidean(self, start_node, end_node):
        """
        Provides the euclidean distance from 
        the start_node to the end_node
        Args:
            start_node (PathNode):
            end_node (PathNode): 

        Returns:
            double: Euclidean distance calculated from the centers
        """
        return math.sqrt((end_node.rect.centerx - start_node.rect.centerx) ** 2 + (end_node.rect.centery - start_node.rect.centery) ** 2)
    
    def update_velocities(self):
        """
        Determines the direction of the next node
        in the path and sets the velocity towards
        that direction. Also modifies the 
        animation option appropriately.
        """
        # Reset velocities to 0
        self.stop()

        if len(self.path) == 0:
            return
        
        # Determine which direction to go
        next_node = self.path[0]

        diffx = next_node.rect.centerx - self.rect.centerx
        diffy = next_node.rect.centery - self.rect.centery

        # If we're there (or close enough), switch nodes
        if abs(diffx) <= self.speed and abs(diffy) <= self.speed:
            self.current_node = next_node
            self.path.pop(0)

            # update position to be the node's position
            self.rect.centerx = self.current_node.rect.centerx
            self.rect.centery = self.current_node.rect.centery
            return

        # If we're in line with x, we're going up or down
        if abs(diffx) < self.speed:
            if diffy > 0:
                # The node is below us
                self.anim_option = self.DOWN
                self.vel_y = self.speed
            else:
                self.anim_option = self.UP
                self.vel_y = -self.speed
        # Otherwise we're going left or right
        else:
            if diffx > 0:
                # The node is to the right
                self.anim_option = self.RIGHT
                self.vel_x = self.speed
            else:
                self.anim_option = self.LEFT
                self.vel_x = -self.speed

    
    def stop(self):
        self.vel_x = 0
        self.vel_y = 0

    def update(self, input=None):
        self.update_velocities()
        
        # Update position
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Update image for animation
        anim = self.anim[self.anim_option]
        self.anim_count = (self.anim_count + 1) % len(anim)
        self.image = anim[self.anim_count]
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x , self.rect.y ))