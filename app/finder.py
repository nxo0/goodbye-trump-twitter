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
        print(ues)
        if not ues:
            return False
        unknown_encoding = ues[0]
        res = fr.compare_faces([self.trump_encoding], unknown_encoding)
        return res[0]



if __name__ == "__main__":
    import cv2
    from main import Main
    #url = 'https://pbs.twimg.com/profile_images/1345429722444906497/sdAYml94.jpg'
    #url = 'https://pbs.twimg.com/profile_images/1092397546809556992/eoXhv9Gt.jpg'
    #url = 'https://pbs.twimg.com/profile_images/1312039541654482946/oeJOY4L_.jpg'
    url = 'https://pbs.twimg.com/profile_images/1157851233962491905/PG6j5Q6H.jpg'
    img = Main.url2image(url)

    #img = cv2.imread("./demo/trump.jpeg")
    fi = Finder()
    #yuki = fi.image_finder("./demo/yuki.png")
    #trump = fi.image_finder("./demo/trump.jpeg")
    for _ in range(30):
        trumpim = fi.frame_finder(img)
        print("img", trumpim)
    
