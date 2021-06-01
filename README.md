# Random-Scale
New data augmentation(2021.04)

![image](https://user-images.githubusercontent.com/59173164/113481576-474b6380-94d5-11eb-8a56-994d64705477.png)

줄의 간격은 두 줄 사이에 포함되는 pixel의 개수(dist).
scale 방향은 width or height.
각 line이 밀릴 수 있는 범위는 다음 두 가지 경우를 배제하도록 산정.
1. 원본과 거의 유사할 수 있는 범위
2. 원본과 너무 달라져 알아보기 힘들 정도의 범위
→ 최소(line 간격 / 4) ~ 최대(line 간격 / 2) ... (try1)

# result
![image](https://user-images.githubusercontent.com/59173164/113481700-0011a280-94d6-11eb-9f18-41248babb013.png)




# 학습 결과
1. cifar-10 image Test Err(%) by Random Scaling prob (dist : 8)


|------|100%|75%|50%|
|------|---|---|---|
|ResNet110|7.14|6.48|5.51|

2. cifar-10 image Test Err(%) 


||Baseline|+RS|+cutout|+cutmix|
|------|---|---|---|---|
|ResNet20|8.20|7.62|7.39|7.26|
|ResNet44|7.92|6.23|6.90|6.99|
|ResNet110|6.72|5.51|5.58|5.60|

3. cifar-100 image Test Err(%) 


||Baseline|+RS|+cutout|+cutmix|+RS+cutmix|
|------|---|---|---|---|---|
|ResNet44|31.06|28.73|28.82|27.6|26.45|

4. cifar-10 graph
![image](https://user-images.githubusercontent.com/59173164/120281444-ea610380-c2f3-11eb-8fdc-6bed53998da8.png)

5. cifar-100 graph
![image](https://user-images.githubusercontent.com/59173164/120281459-ee8d2100-c2f3-11eb-90b3-40edff587e19.png)
