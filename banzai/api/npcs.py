from banzai.client import actor


def get_all(name_id=None, filter_func=None):
    npcs = actor.get_npcs()
    if name_id is not None:
        if isinstance(name_id, str):
            npcs = list(filter(lambda npc: npc.get_name() == name_id, npcs))
        elif isinstance(name_id, int):
            npcs = list(filter(lambda npc: npc.get_id() == name_id, npcs))
    if filter_func is not None:
        if callable(filter_func):
            npcs = list(filter(filter_func, npcs))
    return npcs
