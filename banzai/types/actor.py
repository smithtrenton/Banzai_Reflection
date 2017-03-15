from banzai.types import node


class Renderable(node.Node):
    def get_model_height(self):
        pass


class Actor(Renderable):
    def get_queue_x(self):
        pass

    def get_queue_y(self):
        pass

    def get_queue(self):
        pass

    def get_queue_size(self):
        pass

    def get_world_x(self):
        pass

    def get_world_y(self):
        pass

    def get_position(self):
        pass

    def get_interacting_index(self):
        pass


class NPC(Actor):
    def get_definition(self):
        pass


class NPCDefinition(node.Node):
    def get_actions(self):
        pass

    def get_name(self):
        pass

    def get_id(self):
        pass

    def get_combat_level(self):
        pass


class Player(Actor):
    def get_name(self):
        pass

    def get_combat_level(self):
        pass


class Static:
    @staticmethod
    def get_local_npcs():
        pass

    @staticmethod
    def _get_local_npcs():
        pass

    @staticmethod
    def get_npc_indices():
        pass

    @staticmethod
    def get_npc_indices_size():
        pass

    @staticmethod
    def get_local_player():
        pass

    @staticmethod
    def get_local_players():
        pass

    @staticmethod
    def get_local_player_index():
        pass
