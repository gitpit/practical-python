import os
import sys
import dotenv
import logging

dv = dotenv.load_dotenv

env1 = os.environ.get('OPENAI_API_KEY')
print(env1)
env2 = os.getenv('POSH_THEMES_PATH')
print(env2)

# read all env variables
def read_env():
    env = {}
    for key, value in os.environ.items():
        env[key] = value
    return env
env = read_env()

for key, value in env.items():
    print(f"{key}: {value}")