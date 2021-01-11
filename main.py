# -*- coding: UTF-8 -*-
import tweepy
import numpy as np
import cv2

CA = "TOKEN"
CS = "TOKEN"
AT = "TOKEN"
AS = "TOKEN"
auth = tweepy.OAuthHandler(CA, CS)
auth.set_access_token(AT, AS)
api = tweepy.API(auth)

print(api.me().profile_image_url_https)

#参考になると思われるサイト
# https://quzee.hatenablog.com/entry/2018/09/11/233752
# https://note.nkmk.me/python-opencv-numpy-image-difference/
