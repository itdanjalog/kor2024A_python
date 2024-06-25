# [문제2] 두 개의 정수를 입력받아서, 두 수 사이의 모든 정수를 출력하는 프로그램을 작성하세요. (단, 입력받은 두 수도 포함)
# [ 풀이 ]
시작값 = int( input('[문제2] 시작값 : ') )      # 3
끝값 = int( input('[문제3] 끝값 : ') )         # 6

# 반복문 사용 하지 않았을떄
print( 3 )
print( 4 )
print( 5 )
print( 6 )
# 반복문 사용 했을때
for 반복변수 in range( 시작값 , 끝값+1 , 1 ) :
    print( 반복변수 )

#[문제4] 2~9단 에서 3단을 제외한 구구단을 구현하시오.
    # 반복되는 구역 :  print( " 2 X ")
    # 패턴 구역 : 1 부터 9 까지 1씩 증가 반복 => 반복변수 in range
print( " 2 X 1 = 2 ")
print( " 2 X 2 = 4 ")
print( " 2 X 3 = 6 ")
print( " 2 X 4 = 8 ")
print( " 2 X 5 = 10 ")
print( " 2 X 6 = 12 ")
print( " 2 X 7 = 14 ")
print( " 2 X 8 = 16 ")
print( " 2 X 9 = 18 ")

for 곱 in range( 1 , 10 , 1 ) :
    print( "2 X",곱,"=" , 2*곱 )

for 단 in range( 2 , 10 , 1 ) :
    print( 단 ,'X 1 = ', 단*1)

# 단 안에 곱이 포함 인지?? 곱 안에 단이 포함 인지??? --> for 중첩
for 단 in range( 2 , 10 , 1 ) :
    for 곱 in range(1, 10, 1):
        print( 단,"X",곱,"=", 단 * 곱)

for 단 in range( 2 , 10 , 1 ) :
    if 단 == 3 : continue
    for 곱 in range(1, 10, 1):
        print( 단,"X",곱,"=", 단 * 곱)






