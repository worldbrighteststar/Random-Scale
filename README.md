# Random-Scale
New data augmentation : Random Scaling

 기존의 이미지 데이터 증강 기법들은 데이터에 포함된 객체 모양 자체를 변형시키지는 않는다. 이미지 전체를 뒤집거나, 이미지의 특정 구역을 잘라 내거나, 특정 픽셀에 노이즈를 발생시키는 등 객체의 원본 모양을 유지하면서 이미지에 변화를 주는 방법으로 데이터 증강 효과를 가져왔다. 따라서 본 연구는 객체를 구성하는 2차원 요소들을 적당히 변형시키는 것이 모델 학습에 어떤 영향을 미치는지 파악하는 것을 목표로 하였으며, 이미지에 ‘Partially’, ‘Randomly’ Scale을 적용하여 원본 객체의 모양을 다양하게 변형시킬 수 있는 새로운 데이터 증강 기법, Random Scaling을 고안한다. 제안된 방법은 ResNet-110 모델에서 CIFAR10 classification 기준 5.51%의 test error를 기록하였고, 이는 기존의 typical data augmentation을 적용한 방법보다 1.21% 정도 높은 성능이다.

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


||100%|75%|50%|
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
