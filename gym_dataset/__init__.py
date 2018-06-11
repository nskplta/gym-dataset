from gym.envs.registration import register

register(
    id='dataset-v0',
    entry_point='gym_dataset.envs:DatasetEnv',
)
