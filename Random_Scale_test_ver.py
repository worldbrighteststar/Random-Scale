import cv2
import random

ori_img = cv2.imread("data/cat.png")
scale_img = ori_img.copy() # 원본 훼손 방지


def randomScale(img, dist, d): # original img, distence between two lines, direction for scaling
    
    h, w, _ = img.shape
    x = w if d == 0 else h 

    n = int(x / dist) - 1 # number of lines
    lines = [i * dist for i in range(n + 2)] # initial idx of each line
    
    for i in range(1, len(lines) - 1):
        s, m, e = lines[i - 1], lines[i], lines[i + 1] # start, middle, end Lines
        plusminus = random.randrange(0,2) # 0 = plus, 1 = minus
        scale_range = random.randrange(int(dist / 4),int(dist / 2) + 1) # number of pixels for scaling
        scale_range *= 1 if plusminus == 0 else -1

        # scaling 
        firstB = cv2.resize(img[0:h, s:m], (m - s + scale_range, h)) if d == 0 else cv2.resize(img[s:m, 0:w], (w, m - s + scale_range))
        secondB = cv2.resize(img[0:h, m:e], (e - m - scale_range, h)) if d == 0 else cv2.resize(img[m:e, 0:w], (w, e - m - scale_range))

        # applying scaled part to original img
        if d == 0:
            temp = cv2.hconcat([firstB,secondB])
            img[0:h, s:e] = temp
        else:
            temp = cv2.vconcat([firstB,secondB])
            img[s:e, 0:w] = temp
    
    return img
            


# result
######################################################################################
distOfLines = 80 # randome scaling 기준이 되는 범위의 크기(클수록 원본 훼손 증가)
WorH = 0 # scaling 방향(width or height)
######################################################################################

scaledImg = randomScale(scale_img, distOfLines, WorH)
"""
# original img
print(ori_img.shape)
cv2.imshow("img", ori_img)
# scaled img
print(scaledImg.shape)
cv2.imshow("f", scaledImg)
cv2.waitKey()
"""
######################################################################################


# getting testImgs depends on distoflines 

for i in range(20, 180, 20):
    test = ori_img.copy()
    test = randomScale(test, i, 1)
    cv2.imwrite(f"data/cat_h{i}.jpg", test)



