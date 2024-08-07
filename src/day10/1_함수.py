'''
    - 생활속 함수??
        ( 매개변수 )                        ( 리턴 )
        입력          --->  기능 수행  ---> 출력
        돈,제품 선택   --->    자판기   ---> 잔돈 , 제품
        1000,콜라선택 --->    자판기    ---> 200 , 콜라

    함수 : 일정한 동작을 수행하는 코드들
        -   어떤 일/동작을 수행 하는 명령/코드 들을 하나로 묶어서
            이름을 부여 하고 필요할 때마다 함수 사용/호출
        - 용어
            매개 변수 : 함수 안으로 들어 오는 값 , 인자 값 , 인수
            리턴 값 : 함수가 종료 되면서 호출 했던곳 으로 반환 되는 값
            정의 : 특정 코드를 선언 하거나 만드는 행위
        - 특징
            1. 재사용성 2.매개변수에 따른 서로 다른 결과물 3.메모리 효율성이 좋다.
'''
# 함수 정의
def 자판기( 돈 , 제품번호 ) :
    if 제품번호 == 1 and 돈 >= 800 :
        return '콜라' # 함수 밖으로 반환되는 값
    elif 제품번호 == 2 and 돈 >= 700 :
        return '사이다'
    elif 제품번호 == 3 and 돈 >= 600 :
        return '환타'
# 함수 실행/호출
받은제품 = 자판기( 1000 , 1 )
print( 받은제품 )

# 언제 사용 하면 좋을까?
# [1] 재사용성 : 규모가 큰 프로 젝트 내에서 매우 중요한 역할 , 유지보수
    # 반복문 : 특정 조건에 따라 작성된 위치에서 반복되는 코드
    # 함수 : 코드를 한번 정의/만들기 하고 어떠한 위치에서도 함수 호출해서 코드 실행
for i in range( 0 , 3 ) :   #
    print('python')

def py( ) :
    print('python')
py()
py()
py()

# [2] 매개변수에 따른 결과물
def _plus( x , y ) :
    return x + y
print( _plus( 3 , 5 ) )
print( _plus( 5 ,10 ) )

# [3] 메모리 효율성 이 좋다. 함수 종료될때 함수내{ } 모든 변수/메모리 들은 다 사라 진다.
def _subtract( x , y ) :
    result = x - y      # 함수 실행될때 선언 되었던 result 변수는 어떻게 되었을까???
    return result
print( _subtract( 5 , 3 ) )
print( _subtract( 10 , 5 ) )
print(" -------------------------  ")


# [ 경우에 따라 함수 활용 ]
# [1] 매개변수를 지정해서 호출
def _sum( a , b ) :
    print( f' a : { a }  b : { b }')
    return a + b
print( _sum( 3 , 5 ) )      # 3 데이터를 a매개변수에 대입 , 5 데이터를 b매개변수에 대입
print( _sum( 5 , 3 ) )      # 인자값 순서가 매개변수의 정의 순서대로 대입된다.
print( _sum( b=5 , a=3 ) )  # 매개변수 지정 . 매개변수명=인자값
print( _sum( a = 3 , b = 5) )

# [2] 매개변수 다수일때 또는 매개변수 개수가 일정하지 않을때/모를때 , *매개변수명
    # ( )튜플 타입으로 매개변수를 받는다.
def _sum2( *다수의매개변수 ) :
    print( 다수의매개변수 )

_sum2( 1,3,5,7,9)
_sum2( 1 , 5 )

# [실습1] "1,123,123" 천단위 쉼표가 있는 문자열 을 매개변수 로 받았을때 ,쉼표가 제거된 정수를 반환 하는 함수 정의 하기
    # 파이썬 아닌 외부(엑셀,웹의자료 등등) 로부터 금액을 가져왔는데 ,천단위쉼표(문자열) 가 있으면 연산이 불가능
    # 연산을 하기위해 문자열타입금액을-->숫자타입금액으로
def intConvert( str ) :
    # 1. 쉼표 제거
    newStr = str.replace( ',' , '' )    # 문자열.replace( 기존문자 , 새로운문자 ) 기존문자를 새로운문자로 치환/교체 된 문자열 반환
    print( newStr )
    # 2. 정수로 타입 변환
    intStr = int( newStr )              # int(문자열) : 해당 문자열을 정수타입으로 반환 해주는 함수
    print( intStr )
    # 3. 리턴 값
    return intStr
result = intConvert( "1,123,123" )
print( f'result1 : { result }')
result = intConvert( "456,789" )
print( f'result2 : { result }')

# [실습2] [ 1 , 3 , 5 , 7] 리스트 를 매개변수로 받았을때 리스트 내 모든 요소 들의 총합계 를 반환 하는 함수 정의 하기
def listTotalSum( list ) :
    # 1. 매개변수 확인
    print( list )
    # 2. 리스트를 반복해서 총합계 구하기
    sum = 0
    for value in list : # 리스트내 모든 요소를 하나씩 반복변수에 대입 반복
        # print( value )  # 리스트내 모든 요소가 하나씩 호출 / 출력
        sum += value
    # 3. sum 총합계 변수를 반환 하자.
    return sum
result = listTotalSum( [ 1 , 3 , 5 , 7 ] )
print( f'result3 : { result }')




















