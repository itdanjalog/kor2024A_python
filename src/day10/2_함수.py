
# [3] 매개변수 다수일때 , 개수가 정해져 있지 않을때.
    # *매개변수명 : 튜플타입으로 모든 인자값들을 받는다.
def method1( *매개변수 ) :  # 여기서 는 받은 인자값 여러개를 하나의 자료(튜플) 로 받습니다.
    print( 매개변수 )

method1( 1 , 2 )        # 여기서는 인자값/자료 2개를 함수 매개변수로 전달
method1( 1 , 2 , 3 )    # 여기서는 인자값/자료 3개를 함수 매개변수로 전달

    # **매개변수명 : 딕셔너리 타입으로 모든 인자값들을 받는다.
def method2( **매개변수 ) :
    print( 매개변수 )

method2( a = 1 , b = 2 )
method2( num1 = 1 , num2 = 2 , num3 = 3 )

# [4] 함수의 리턴값
    # 리턴값이 가는곳 : 해당 함수를 호출했던 위치/곳
    # 리턴값은 항상 1개의 자료/데이터 만 가능하다.
def method3( x , y ) :
    더하기값 = x + y
    곱하기값 = x * y
    return 더하기값 , 곱하기값 # 자동으로 두개의 변수값을 튜플타입으로 반환된다.

result =  method3( 3 , 2 )
print( f'method3 : {result}')

# 아래와 같은 형식으로 return 2번 사용하면 2번째 return 의미가 없다.
def method4( x , y ) :
    return x+y
    return x*y  # 위에서 이미 함수가 리턴 했으므로 아래 리턴은 실행되지 않는다. 리턴이란? 함수종료인가요? 맞아요.
# 아래와 같은 형식으로 return 2번 사용했지만 흐름/제어에 따라 return코드가 무조건 실행되는 코드가 아니므로 가능하다.
def method5( x , y ) :
    if x >= 5 :
        return x + y
    else :
        return x * y

# [5] 함수 안에서 또는 함수 밖에서 선언된 변수들 효력 범위
value1 = 10 # 일반변수
def method6( value1 ) : # 매개변수
    return value1 + 1   # 10 + 1 => 11

print( method6( value1 ) )  # 변수명 코드로 작성하면 변수 호출    # method6( 10 ) => 11
print( value1 ) # 10

## 전역변수 : 함수 밖에서 선언된 변수는 함수 안에서 호출/사용이 가능 하다.
def method7( ) :
    print( value1 )
method7()

## 지역변수 : 함수 안에서 선언된 변수는 함수 밖에서 호출/사용이 불가능하다.
def method8( ) :
    value2 = 20
# print( value2 )

## global키워드 : 함수 안에서 선언된 변수를 함수 밖에서 사용/호출 하기 위해서 사용되는 키워드
    ## return 은 변수를 밖으로 반환하는게 아니라 변수가 가지는 또는 순수 값/자료 을 반환
value6 = 60
def method9( ) :
    value3 = 30
    global value7       # 글로벌 변수 선언
    value7 = 70         # 글로벌 변수의 값/자료 대입
    if 3 > 2 :
        value4 = 40
    else:
        value5 = 50
    print( value3 )
    print( value4 )
    #print( value5 )    # 실행 불가능 , 오류
    print( value6 )
    return value3       # 30 자료/값이 반환 
method9()
print( value6 )
print( value7 )


















