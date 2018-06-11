import gym
from gym import error, spaces, utils
from gym.utils import seeding

class DatasetEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
    ...
  def step(self, action, labels, estadoact_index):
    if labels[estadoact_index] == action: #se puede poner solo y[muestraelegida]?
        reward = 1
    else:
        reward = 0
    self.observ = np.random.choice(dataset.shape[0], 1, replace=False)
    self.observ = np.asscalar(self.observ) #supongo que action es un número aleatorio: self.action = np.random.choice(dataset.shape[0], 1, replace=False)  
    self.observation = dataset[self.observ, :] 
    return observation, reward, episode_over
  def reset(self, dataset):
    self.muestraelegida = np.random.choice(dataset.shape[0], 1, replace=False)
    self.muestraelegida = np.asscalar(self.muestraelegida)
    self.initial_state = dataset[self.muestraelegida, :]
    return self.initial_state #s_t = dataset_state, s_t = s_t.reshape((-1,1)), s_t = s_t.T
  def render(self, mode='human', close=False):
    pass
  def get_action_space(self):
    return 2
  def get_observation_space(self):
    return dataset.shape[0] #comprobar 
  

#make() for creating the environment and returning a reference to it.
#step() for taking a step in the environment and returning a tuple (observation images, reward float value, done boolean, any other info).
#reset() for resetting the environment to the initial state.
#get_observation_space() for returning an object with attribute tuple shape representing the shape of the observation space.
#get_action_space() for returning an object with attribute n representing the number of possible actions in the environment.
#render() for rendering the environment if appropriate.
