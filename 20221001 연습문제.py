print("안녕하세요?")

print("파이썬을 연습하고 있습니다.")

print("제 나이는", 4*6 ,"살입니다.")

print("감사합니다.")


# 화면에 여러 개의 값을 출력할 때는 쉼표(,) 사용.
# 다른 자료형에 +를 사용하면 error

# 터틀 그래픽으로 정삼각형 그리기

import turtle
t = turtle.Turtle()
t.shape("turtle") #없어도 실행 가능, 대신 커서모양이 삼각형이 됨.

t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.circle(100) #반지름이 100인 원이 그려
#육각형은 left(60)사용




