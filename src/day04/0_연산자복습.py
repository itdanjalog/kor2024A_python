# 문제1 : 하나의 정수형으로 정수를 입력받아 입력받은 값이 7의 배수 이면 'O' 아니면 'X' 출력 하시오.
#[풀이]
value1 = int( input('[문제1] 정수 : ') ) # 1.입력받고 -> 정수형으로 변환 -> 변수에 저장
result1 = value1 %  7 == 0              # 2. 산술연산자 , 7배수의 찾기   (  배수찾기 : 값 % 배수 == 0 )
print( 'O' if result1 else 'X' )        # 3. 삼항연산자

# 문제4 : 하나의 정수형으로 정수를 입력받아 입력받은 값이 11의 배수 이거나 짝수 이면 'O' 아니면 'X' 출력 하시오.
#[풀이]
value4 = int( input('[문제4] 정수 : ') )
result4 = value4 % 11 == 0 or value4 % 2 == 0     #  논리연산자 , 짝수 찾기 : 값 % 2 == 0
print( 'O' if result4 else 'X' )
# print( 'O' if value4 % 11 == 0 or value4 % 2 == 0 else 'X' )

# 문제7 : 두개의 실수형으로 입력받아 앞 실수의 값이 뒤의 값의 몇% 인지 출력하시오.
#     예) 54.5   84.3 실수 2개입력시 결과는   64.2%
# [풀이]
value7_1 = float( input('[문제7] 실수1 : ') )
value7_2 = float( input('[문제7] 실수2 : ') )
result7 = value7_1 / value7_2
print( '결과 : ' , result7 )
print( '결과 : ' , result7 * 100 )
print( '결과 : ' , int( result7 * 100 ) )
print( '결과 : ' , result7 * 1000 )           # 646.5005931198102
print( '결과 : ' , int( result7 * 1000 ) )    # 646
print( '결과 : ' , int( result7 * 1000 )/10 ) # 64.6

#문제13 : 정수형으로 나이를 입력받아 나이가 10세이상이면 학생 , 20세이상이면 성인 , 40세이상이면 중년 으로 출력하기
value13 = int( input('[문제13] 나이 : ') )
result13 = '중년' if value13 >= 40 else '성인' if value13 >=20 else '학생' if value13 >=10 else ''
print( result13 )
