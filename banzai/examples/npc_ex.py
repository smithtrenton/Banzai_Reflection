import banzai
from banzai.api import npcs

banzai.init()

bankers = npcs.get_all(name_id='Banker')
for banker in bankers:
    print(banker.get_position())

banzai.terminate()
