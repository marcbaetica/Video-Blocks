import cv2


def split_mp4_to_jgp(video_uri, output_folder):
    vidcap = cv2.VideoCapture(video_uri)
    success, image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite(f'{output_folder}/frame_{count}.jpg', image)
        success, image = vidcap.read()
        print('Read a new frame: ', success)
        count += 1
