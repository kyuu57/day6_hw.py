import turtle as t           # turtle 을 t로 한다.
t.shape("circle")            # t의 모양을 circle 로 한다.

t.up()                       # 그림을 그리지 않고 이동한다.
t.goto(-680,-150)            # t의 좌표를 (-680,-150)으로 이동한다.
t.down()                     # 그림을 그릴 준비를 한다.
t.seth(0)                    # circle 의 방향을 오른쪽으로 향하게 함.



def polygon(n, a):           # polygon 함수를 정의한다.
   for x in range(n):        # n번 반복한다.
        t.fd(a)              # 앞으로 a만큼 간다.
        t.lt(360/n)          # 왼쪽으로 360/n도 만큼 회전한다.
        
polygon(4,500)               # polygon 을 이용하여 한변이 500인 정사각형을 만든다.


t.up()                       # 그림을 그리지 않고 이동한다.
t.goto(-350,-50)
t.down()
polygon(4,100)
t.up()


import random                # random 모듈을 쓰겠다.
a=random.randint(1,360)      # 1부터 360까지의 수를 랜덤추출해서 a에 저장
t.speed(0)                   # 거북이를 최고 속도로 한다

t.goto(-430,100)             # 거북이를 중앙에 놓는다
t.setheading(a)              # 거북이가 바라보는 각도를 a도로 한다.
  
while True:                  # 무한반복
   a = t.xcor()              # x좌표를 a에 저장
   b = t.ycor()              # y좌표를 b에 저장
   ang=t.heading()           # 거북이가 바라보는 각도를 ang에 저장
   t.fd(2)                   # 앞으로 2만큼 이동한다
   
   if b < -150:              # 만약 y좌표가 -150보다 작다면
      t.seth(360-ang)        # 반사각 계산
      t.fd(5)                # 5씩 앞으로 이동한다
    
      
   if b > 350:               # 만약 y좌표가 350보다 크다면
      t.seth(360-ang)        # 반사각 계산
      t.fd(5)                # 5씩 앞으로 이동
  
      
   if a > -180:              # 만약 x좌표가 -180보다 작다면
      t.seth(180-ang)        # 반사각 계산
      t.fd(5)                # 5씩 앞으로 이동
      
      
   if a < -680:              # 만약 x좌표가 -680보다 크다면
      t.seth(180-ang)        # 반사각 계산
      t.fd(5)                # 5씩 앞으로 이동
    
      
   
   
