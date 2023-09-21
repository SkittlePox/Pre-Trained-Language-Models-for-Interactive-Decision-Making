from gym.envs.registration import register

register(
    id='vh_graph-v0',
    entry_point='vh_mdp.vh_graph.envs:VhGraphEnv',
)

from .envs import *
