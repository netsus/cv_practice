import numpy as np
import cv2

# 아스키 이미지를 출력하는 함수입니다.


def print_ascii_img(ascii_img):
    for i in range(ascii_img.shape[0]):
        for j in range(ascii_img.shape[1]):
            print(ascii_img[i, j], end="")
        print()

# 이미지를 아스키로 변환하는 함수입니다.


def img2ascii(img, L, ascii_string):
    # 양자화를 수행하고 ascii 문자로 명도를 표현하세요.
    def f(x): return ascii_string[x]
    myfunc_vec = np.vectorize(f)
    ascii_img = myfunc_vec(img//len(ascii_string))
    return ascii_img


if __name__ == "__main__":
    ascii_string = "@#BPDQOUo=+*~-`."

    # 주어진 이미지를 읽어옵니다.
    img = cv2.imread("Lenna.png", cv2.IMREAD_GRAYSCALE)

    # 함수를 호출하여 결과를 확인합니다.
    ascii_img = img2ascii(img, 16, ascii_string)
    print_ascii_img(ascii_img)
