import json


def readConfigs():
    config_file = open("configs.txt", "r")
    configs = config_file.read()
    config_file.close()
    return configs


def getConfigValue(config):
    configs = json.loads(readConfigs())
    server_config = configs[config]
    return server_config


def setConfig(config, value):
    configs = json.loads(readConfigs())
    configs[config] = value
    with open('configs.txt', 'wb') as fp:
        json.dump(configs, fp)
