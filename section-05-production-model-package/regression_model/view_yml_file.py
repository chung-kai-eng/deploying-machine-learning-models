# from strictyaml import load # (need to specify as the string)
import yaml

def read_config(config_file='config.yml'):
    with open(config_file) as in_file:
        data = yaml.load(in_file) # dictionary format
    return data

dictionary = read_config()

for key, value in dictionary.items():
    print(f'{key}: {value}')

# yaml.load(in_file, Loader=SafeLoader) 
# SafeLoader: Loads subset of the YAML safely, mainly used if the input is from an unstruted source
# Baseloader: loads all the basic yaml scalars as strings