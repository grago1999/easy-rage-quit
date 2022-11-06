import subprocess
import cv2
import numpy
import mss
import sys
import time
sys.path.append("../shared")
import img_to_num

# alll the valid games and their HP locations
EXE_MAP = {
    "csgo": ("csgo.exe", 80, 155, 1378, 1422),
    "tf2": ("hl2.exe", 270, 330, 1240, 1280)
}
# HP threshold to quit the game
MIN_HP = 10

def quit_game(game_exe):
    # 5 quit the game exe (windows)
    subprocess.call("TASKKILL /F /IM "+game_exe, shell=True)

def test(game, x_start, x_end, y_start, y_end):
    resized_img = cv2.resize(cv2.imread(game+"_test.jpg"), (2560, 1440))
    cropped_img = numpy.array(resized_img)[y_start:y_end, x_start:x_end]
    print(game, "test", img_to_num.from_img(cropped_img, game+" test", True, True))

def main(screens, monitor):
    # 1: validating the game param (should be one of the keys in EXE_MAP)
    if len(sys.argv) < 2:
        print("please input a valid game")
        sys.exit(1)

    game = sys.argv[1]
    if game not in EXE_MAP.keys():
        print("please input a valid game")
        sys.exit(1)

    print("starting in 5 seconds")
    time.sleep(5)
    game_exe, x_start, x_end, y_start, y_end = EXE_MAP[game]

    # 2: extra param to specifiy that we should use a single test image
    # rather than the real-time screen
    if len(sys.argv) == 3:
        is_test = sys.argv[2] == "test"
        if is_test:
            test(game, x_start, x_end, y_start, y_end)
            sys.exit(1)

    print("starting quitter")

    # 3: repeatedly get the current screen frame/image, and crop
    # image to HP location
    while True:
        img = screens.grab(monitor)
        resized_img = cv2.resize(numpy.array(img), (2560, 1440))
        cropped_img = resized_img[y_start:y_end, x_start:x_end]

        # 4: convert image to int to compare against treshold, and quit
        # game if below
        current_hp = img_to_num.from_img(cropped_img, should_invert=True)
        if current_hp is not None:
            print("hp:", current_hp)
            if current_hp <= MIN_HP:
                quit_game(game_exe)
                sys.exit(1)

# 0: start of the program with the current screen
with mss.mss() as screens:
    monitor = screens.monitors[1]
    main(screens, monitor)