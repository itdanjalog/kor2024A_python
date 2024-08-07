'''
    문자열
        - 파이썬에는 문자열을 표현하는 4가지 방법 
        - " "(큰따옴표) , ' '(작은따옴표), """ """ , ''' ''' 로 감싼 형식 
        - 문자열은 불변성 성질을 가지기 때문에 변경이 불가능하다.
            - 새로운 문자열 생성하거나 문자열을 조작은 가능하다.
'''
a = "코딩도 헤매는 만큼 자기 땅이야"
print( a )
a = '코딩도 헤매는 만큼 자기 땅이야'
print( a )
a = """코딩도 헤매는 만큼 자기 땅이야"""
print( a )
a = '''코딩도 헤매는 만큼 자기 땅이야'''
print( a )

# 1. 문자열 안에 작은따옴표 포함
a = "코딩'도 헤매는 만큼 자기 땅이야"
print( a )
# 2. 문자열 안에 큰따옴표 포함
a = '코딩도 헤매는 만큼 "자기 땅이야"'
print( a )
# 3. 이스케이프 문자 이용한 큰따옴표 포함
a = "코딩\'도 헤매는 만큼 자기 땅이야"
print( a )
a = '코딩도 헤매는 만큼 \"자기 땅이야\"'
print( a )

# 여러 줄인 문자열 을 표현 할때
# 1. 이스케이프 문자
a = "코딩도\n 헤매는 만큼 자기 땅이야"
print( a )
# 2.  """ ''' 연속된 따옴표
a = """코딩도
 헤매는 만큼 자기 땅이야"""
print( a )
a = '''코딩도
 헤매는 만큼 자기 땅이야'''
print( a )


# 문자열 연산
# 1. 연결연산자
a = '코딩도'
b = ' 헤매는 만큼 자기 땅이야'
c = a + b # 문자열 끼리는 더하기 연산이 아닌 연결연산
print( c )
# 2. 문자열 곱하기
print( a * 3 )
print( '=' * 30 ) # * 수    만큼 문자열 반복
print( 'MENU')
print( '=' * 30 )
# 3. 문자열 길이 구하기 , 띄어쓰기 도 문자 1개로 취급
a = '코딩도 헤매는 만큼 자기 땅이야'
print( len( a ) )
# 인덱스 , 슬라이싱
a = '코딩도 헤매는 만큼 자기 땅이야'
# 인덱스 : 코[0] 딩[1] 도[2] [3] 헤[4]매[5]는[6] [7] 만[8]큼[9] [10] 자[11]기[12] [13] 땅[14] 이[15] 야[16]
# 인덱스 :  0 ~ 16   , 길이 : 17
print( a[0] )   # 0번째 인덱스 문자 1개
print( a[12] )  # 기
print( a[-1] )  # 야  ,  인덱스는 0있고 , -0 없음
print( a[0:4] ) # 코딩도  , 공백포함 0 ~ 3 인덱스
print( a[5:7] ) # 매는    , 5 ~ 6 인덱스
print( a[5:0] ) #
print( a[0:5] ) #
print( a[ : ] )

# 반복문 과 문자열
for char in a :
    print( char )   # 문자열내 문자 하나씩 출력

# [ 실습1 ]
    # '코딩도 헤매는 만큼 자기 땅이야' 에서 띄어 쓰기가 제거 된 새로운 문자열 생성 하시오.
a = '코딩도 헤매는 만큼 자기 땅이야' # 기존문자열
newStr = ''                      # 새로운문자열
for c in a :
    if c == ' ' :   # 만약에 반복변수의 문자가 공백/띄어쓰기 이면
        continue    # 반복 중단하고 다시 for문으로 이동
    newStr += c                 # 기존문자를 새로운문자 에 연결연산자
print( newStr )

# [ 실습2 ]
    # 아래 문자열내 제품명과 제품가격이 저장된 문자열 입니다.
    # 아래 와 같은 형식으로 출력하시오.
'''
    제품명    가격
    콜라 300
    사이다    400
    환타 500
'''
product = '콜라,300\사이다,400\환타,500'   # 기존 문자열
newStr = ''                             # 새로운 문자열
for c in product :                      # 기존 문자열 반복문 해서 문자 하나씩 순회
    # print( c )
    if c == ',' :                       # 해당 문자가 , 이면
        newStr += '\t'                      # 들여쓰기 \t 연결
        continue
    if c == '\\' :                      # 해당 문자가 \ 이면
        newStr += '\n'                      # 줄바꿈 \n 연결
        continue
    newStr += c                         # 아니면 연결
print( newStr )


































