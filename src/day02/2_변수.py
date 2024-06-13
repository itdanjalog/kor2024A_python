'''
    변수 : 변하는 수       , 데이터 를 1개 저장할수 있는 공간/상자
    상수 : 변하지 않는 수   , 데이터 를 1개 저장할수 있는 공간/상자
        - 저장 : 해당하는 데이터를 반복적으로 사용할때

    변수 만드는 방법 / 준비물
        1. 변수명
        2. = 대입         : 오른쪽 값을 왼쪽에 대입/저장
        3. 저장할 값
    변수의 값을 꺼내기/호출
        변수명
    변수의 값을 수정/변경
'''
# 변수의 선언 과 초기화 ( 초기화 : 처음에 값을 변수에 넣어주는 행위 )
과일상자 = "바나나"    # 변수명 : 과일상자 , 값 : 바나나
# 변수의 들어있는 값 호출
과일상자
# 변수의 들어있는 값 호출해서 출력해
print( 과일상자 )
# 변수의 들어있는 값 수정
과일상자 = "딸기"
# 확인 출력
print( 과일상자 )

# * 사용자 로 부터 입력 받은 문자열을 변수에 저장
입력 = input( "문자열 : " )
print( 입력 )
print( 입력 ) # 변수에 저장된 값은 반복적으로 호출이 가능하다.
print( 입력 )

# 'strValue' 변수에 첫번째 입력받은 문자열 저장 하고
# 다시 두번째 입력받은 문자열을 'strValue' 변수의 값으로 수정
strValue = input( "첫번째 문자열 : ")
print( strValue )

strValue = input( "두번째 문자열 : ")
print( strValue )

# 'strValue2' 변수에 첫번째 입력받은 문자열 저장 하고
# 다시 두번째 입력받은 문자열을 'strValue2' 변수의 값 과 연결
strValue2 = input("[2]첫번째 문자열 : ")
print( strValue2 )
strValue2 = strValue2 + input("[2]두번째 문자열 : ")
print( strValue2 )

# 'intValue' 변수에 첫번째 입력받은 정수형 저장하고
# 'floatValue' 변수에 두번째 입력받은 실수형 저장하고
# 두 변수를 더하기 한 결과를 'sum' 변수에 저장하고 출력하시오.
intValue = int( input("[1]정수 : ") )
floatValue = float( input("[2]실수 : ") )
sum = intValue + floatValue
print( sum )

# 산술연산자
print( 3 + 3 )      # 더하기 6
print( 3 - 2 )      # 빼기 1
print( 3 * 2 )      # 곱하기 6
print( 10 / 3 )     # 나누기 3.3333~
print( 10 // 3 )    # 몫 3
print( 10 % 3 )     # 나머지 1
print( 10 ** 3)     # 제곱 1000
# 연결연산자
print( "3" + "3" )  # 연결 "33"






