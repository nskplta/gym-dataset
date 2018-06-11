import gym
from gym import error, spaces, utils
from gym.utils import seeding

class DatasetEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
    ...
  def step(self, action):
      
    return observation, reward, episode_over
  def reset(self):
    muestraelegida = np.random.choice(dataset.shape[0], 1, replace=False)
    muestraelegida = np.asscalar(muestraelegida)
    initial_state = dataset[muestraelegida, :]
    return initial_state
  def render(self, mode='human', close=False):
    pass
  def get_action_space(self):
    return 2
  

#make() for creating the environment and returning a reference to it.
#step() for taking a step in the environment and returning a tuple (observation images, reward float value, done boolean, any other info).
#reset() for resetting the environment to the initial state.
#get_observation_space() for returning an object with attribute tuple shape representing the shape of the observation space.
#get_action_space() for returning an object with attribute n representing the number of possible actions in the environment.
#render() for rendering the environment if appropriate.
