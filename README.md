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
1. resNet(20, 44, ...)

진행중...
