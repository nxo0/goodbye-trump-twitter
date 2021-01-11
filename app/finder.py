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
        return fr.compare_faces([self.trump_encoding], unknown_encoding)


    def frame_finder(self, image) -> bool:
        rgb_image = image[:, :, ::-1]
        ues = fr.face_encodings(rgb_image)
        if not ues:
            return False
        unknown_encoding = ues[0]
        return fr.compare_faces([self.trump_encoding], unknown_encoding)



if __name__ == "__main__":
    import cv2
    url = 'https://pbs.twimg.com/profile_images/1345429722444906497/sdAYml94_normal.jpg'
    img = cv2.imread("./demo/trump.jpeg")
    fi = Finder()
    yuki = fi.image_finder("./demo/yuki.png")
    trump = fi.image_finder("./demo/trump.jpeg")
    trumpim = fi.frame_finder(img)

    print("yuki", yuki)
    print("trump", trump)
    print(trumpim)
    
