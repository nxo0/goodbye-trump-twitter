import time
import urllib

from tqdm import tqdm
import schedule
import cv2
import numpy as np

from app.finder import Finder
from app.profiler import Profiler
from app.config import Config
from app.time_parser import timestr2sec
from app.logger import Logger


class Main:
    def __init__(self):
        config = Config()
        self.profiler = Profiler()
        self.finder = Finder()
        self.tl_iv, self.foll_iv = config.get_check_interval_time()


    def users_checker(self, users):
        Logger.info("users checking...")
        for user in tqdm(users):
            image = self.url2image(user.profile_image_url_https)
            if self.check_trump(image):
                Logger.info("find Trump! ,name:" + user.screen_name)
                # BLOCK
                self.profiler.block(user.user_id)
                Logger.info("===BLOCKED===    :", + user.screen_name)
        Logger.info("users check DONE!")

    def followers_check(self):
        Logger.info("followers check START")
        users = self.profiler.get_followers()
        Logger.info("followers getted")
        self.users_checker(users)
        Logger.info("followers check DONE!")

    def timeline_check(self):
        Logger.info("timeline check START")
        users = self.profiler.get_timeline_users()
        Logger.info("timeline users getted")
        self.users_checker(users)
        Logger.info("followers check DONE!")

    def url2image(self, url):
        resp = urllib.urlopen(url)
        image = np.asarray(bytearray(resp.read()), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        return image

    def check_trump(self, img):
        return self.finder.frame_finder(img)

    def once(self):
        self.timeline_check()

    def run(self):
        schedule.every(timestr2sec(self.tl_iv)).seconds.do(self.timeline_check)
        schedule.every(timestr2sec(self.foll_iv)).seconds.do(self.followers_check)
        Logger.info("schedule subscribed")
        while True:
            schedule.run_pending()
            time.sleep(1)

