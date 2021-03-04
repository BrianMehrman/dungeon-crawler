from queue import PriorityQueue


class NpcController:
    """
    TODO: 
     - create nav mesh for all AI to use.
        - nav mesh should be a bunch of nodes that are linked to other nodes

     - add list/dict of nodes the Npc 'knows' about
        - these must be nodes they can get to. an npc can see players on nav mesh they dont have access too. 
    """
    def __init__(self, entity):
        """
        NPC Finite State Machine Controller

        This makes the npc seem smart
        """
        self.entity = entity

    def update(self, delta_time):
        """
        TODO: add later
        """
        pass


    # def find_path(self, grid, target):
    #     '''
    #     a-star path finder. only pass in a subset of visible nodes.

    #     grid: 2d array of nodes of any size
    #     target: node the target is in. The target node must be in the grid passed in.
    #     '''

    #     count = 0
    #     start = self.current_node

    #     open_set = PriorityQueue()
    #     open_set.put((0, count, start))
        
    #     came_from = {}
        
    #     g_score = { node: float("inf") for row in grid for node in row }
    #     g_score[start] = 0

    #     f_score = { node: float("inf") for row in grid for node in row }
    #     f_score[start] = h(start.get_pos(), target.get_pos())

    #     nodes_in_queue = {start}

    #     while not open_set.empty():
           
    #         current = open_set.get()[2]

    #         nodes_in_queue.remove(current)

    #         if current == target:
    #             return came_from

    #         for neighbor in current.neighbors:
    #             temp_g_score = g_score[current] + 1

    #             if temp_g_score < g_score[neighbor]:
    #                 came_from[neighbor] = current
    #                 g_score[neighbor] = temp_g_score
    #                 f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())

    #                 if neighbor not in nodes_in_queue:
    #                     count += 1
    #                     open_set.put((f_score[neighbor], count, neighbor))
    #                     nodes_in_queue.add(neighbor)
    #                     neighbor.change_state(OPEN)


    #         if current != start:
    #             current.change_state(CLOSED)

    #     return False


