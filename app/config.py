import os
import configparser

from app.logger import Logger

CONFIGFILE_PATH = os.environ["HOME"] + "/.gbtt.conf"

class Config:
    def __init__(self):
        isExist = os.path.exists(CONFIGFILE_PATH)
        self._load()
        if not isExist:
            self.all_reset()
    
    def _load(self):
        self.config = configparser.ConfigParser()
        self.config.read(CONFIGFILE_PATH)


    def all_reset(self):
        self.config["TwitterAPIKey"] = {
                "CA": "",
                "CS": "",
                "AT": "",
                "AS": ""
                }
        self.config["CheckInterval"] = {
                "timeline": "10m",
                "follower": "1d",
                }
        with open(CONFIGFILE_PATH, "w") as f:
            self.config.write(f)

    def get_twitter_api_key(self) -> (str,str,str,str):
        """ return: CA, CS, AT, AS """
        try:
            twk = self.config["TwitterAPIKey"] 
            CA,CS,AT,AS = twk["CA"], twk["CS"], twk["AT"], twk["AS"]
            return CA,CS,AT,AS
        except KeyError:
            Logger.error("twitter api key not found. \n run $gbtrump reset")
            exit(0)

    def get_check_interval_time(self) -> (str, str):
        """ return: timeline, follower """
        try:
            ci = self.config["CheckInterval"]
            return ci["timeline"], ci["follower"]
        except KeyError:
            Logger.error("CheckInterval not found. \n run $gbtrump reset")
            exit(0)


if __name__ == "__main__":
    conf = Config()
    print('api     :', conf.get_twitter_api_key())
    print('interval:', conf.get_check_interval_time())
