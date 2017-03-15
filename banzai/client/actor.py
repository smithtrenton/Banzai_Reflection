from banzai.client import node


class Renderable(node.Node):
    def get_model_height(self):
        """Return model height of renderable."""
        pass


class Actor(Renderable):
    def get_queue_x(self):
        """Return reference to actor queue x value array."""
        pass

    def get_queue_y(self):
        """Return reference to actor queue y value array."""
        pass

    def get_queue(self):
        """Return list of actor tile queue."""
        pass

    def get_queue_size(self):
        """Return size of actor queue."""
        pass

    def get_world_x(self):
        """Return raw value of actor x coordinate."""
        pass

    def get_world_y(self):
        """Return raw value of actor y coordinate."""
        pass

    def get_position(self):
        """Return raw position of actor."""
        pass

    def get_interacting_index(self):
        """Return actor interacting index."""
        pass


class NPC(Actor):
    def get_definition(self):
        """Return NPCDefinition of NPC."""
        pass

    def get_id(self):
        """Return id from NPC's NPCDefinition."""
        pass

    def get_name(self):
        """Return name from NPC's NPCDefinition."""
        pass

    def get_combat_level(self):
        """Return combat level from NPC's NPCDefinition."""
        pass


class NPCDefinition(node.Node):
    def get_actions(self):
        """Return list of actions of NPCDefinition."""
        pass

    def get_name(self):
        """Return name of NPCDefinition."""
        pass

    def get_id(self):
        """Return id of NPCDefinition."""
        pass

    def get_combat_level(self):
        """Return combat level of NPCDefinition."""
        pass


class Player(Actor):
    def get_name(self):
        """Return name of player."""
        pass

    def get_combat_level(self):
        """Return combat level of player."""
        pass


# static client accessors and helper functions


def get_npcs():
    """Return an array of local NPC's."""
    pass


def get_local_npcs():
    """Return reference to client static npc array."""
    pass


def get_npc_indices():
    """Return reference to client static npc index array."""
    pass


def get_npc_indices_size():
    """Return length of client static npc index array."""
    pass


def get_local_player():
    """Return reference to client current player."""
    pass


def get_local_players():
    """Return reference to client static player array."""
    pass


def get_local_player_index():
    """Return index of the current player in the client static player array."""
    pass
