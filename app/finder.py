import os

import face_recognition as fr


class Finder:
    def __init__(self):
        path = os.path.dirname(os.path.realpath(__file__))
        trump_image = fr.load_image_file(path + "/trumps/001.jpg")
        self.trump_encoding = fr.face_encodings(trump_image)[0]

    
    def image_finder(self, filename) -> bool:
        unknown_image = fr.load_image_file(filename)
        ues = fr.face_encodings(unknown_image)
        if not ues:
            return False
        unknown_encoding = ues[0]
        return fr.compare_faces([self.trump_encoding], unknown_encoding)[0]


    def frame_finder(self, image) -> bool:
        rgb_image = image[:, :, ::-1]
        ues = fr.face_encodings(rgb_image)
        if not ues:
            return False
        unknown_encoding = ues[0]
        return fr.compare_faces([self.trump_encoding], unknown_encoding)[0]



if __name__ == "__main__":
    import cv2
    try:
        from main import Main
    except ImportError:
        from app.main import Main
    url = 'https://pbs.twimg.com/profile_images/1157851233962491905/PG6j5Q6H.jpg'
    img = Main.url2image(url)
    path = os.path.dirname(os.path.realpath(__file__))

    fi = Finder()
    yuki = fi.image_finder(path + "/demo/yuki.png")
    print('yuki   is', yuki)
    trump = fi.image_finder(path + "/demo/trump.jpeg")
    print('trump  is', yuki)
    urlim = fi.frame_finder(img)
    print("urlimg is", urlim)
    
