'''
    딕셔너리
        - key-value 쌍으로 데이터를 저장하는 구조
        - { } 중괄호 사용 , 각각의 key와value는 :(콜론) 으로 구분한다.
        - 순서가 없는 자료형 이므로 인덱스가 없다. key를 사용한 값 조회/수정 할수있다.
        - key는 중복을 허용 하지 않고(식별용도) , value 중복을 허용
        - key는 주로 '문자열'이용한 이름 정의
        - value는 주로 모든 자료의 타입이 저장가능하다.
        - 선언
            변수 = { key : value , key : value , key : value }
            변수 = { key : [ ] , key : { } , key : { key : [ ] } }
                * 주로 { 딕셔너리 } 와 [ 리스트 ] 중첩으로 많이 사용됨.
        - 값 호출
            변수['key']       : key 문자일때
            변수[key]         : key 숫자일때
            변수.get('key')   : key 해당하는 값 호출
        - 값 수정
            변수['key'] = 새로운값  : 해당하는 key의 value 값 수정
        - 요소 삭제
            del 변수['key']   : 해당 key의 key와value 쌍의 요소를 제거
            변수.pop('key')   : 해당 key의 key와value 쌍의 요소를 제거
            변수.clear()      : 모든 key와value 쌍을 제거 , 전체 요소 삭제

'''

# 리스트는 인덱스를 이용한 요소들을 식별한다.
a = [ '바나나' , '컴퓨터' , '그릇' ]
# 1. 바나나 호출 --> '바나나' 의 인덱스번호 를 알아야 한다.
print( a[0] )
print( a[1] )
print( a[2] )
# 2.
a = { '과일' : '바나나' , '전자제품' : '컴퓨터' , '식기' : '그릇' }
print( a['과일'] )
print( a['전자제품'] )
print( a['식기'] )

# 1. 딕셔너리 선언
dic = { 'name' : 'kim' ,
        'phone' : '010-3333-3333' ,
        'birth' : '0627' }

print( dic )
# 2. value(값) 호출 , 변수명['key']
print( dic['name'] )
print( dic['phone'] )
print( dic['birth'])
# print( dic['age'] ) # 존재하지 않는 key 이므로 오류 발생
    # -
phones = {
    '010-0000-0000' : '유재석' ,
    '010-1111-1111' : '강호동' ,
    '010-2222-2222' : '신동엽'
}
print( phones['010-0000-0000'] )

#
print( phones.get('010-0000-0000') )

# 딕셔너리 value 값 수정
dic['name'] = '강호동'

# 딕셔너리 요소 삭제
del dic['name']
print( dic )

dic.pop('phone')
print( dic )
# 딕셔너리 전체 요소 삭제
dic.clear()
print( dic )

# 딕셔너리의 key:value 쌍/요소 추가
dic['age'] = 42
dic['이름'] = '유재석'
print( dic )

#[실습] 메뉴들을 저장하는 딕셔너리 만들기
    # 1. 제품명과 가격을 저장하는 딕셔너리 선언 하는 코드
        # 제품명이 아메리카노,밀크티,모카라떼 각 저장할 예정이고
        # 제품가격은 각각 5.8 , 6.3 , 6.3
menus = { '아메리카노' : 5.8 , '밀크티' : 6.3 , '모카라떼' : 6.3 }
print( menus )
    # 2. 자몽차를 5.5 가격 에 쌍을 추가 하는 코드 작성
menus['자몽차'] = 5.5
print( menus )
    # 3. 아메리카노의 가격을 4.2 로 수정 하는 코드 작성
menus['아메리카노'] = 4.2    # 동일한 key가 있으면 수정 , 없으면 새로운 쌍 추가
print( menus )
    # 4. 밀크티 를  삭제하는 코드 작성
del menus['밀크티']
print( menus )

# 순회
print( menus.keys() )           # 딕셔너리 내 모든 key를 객체로 반환
print( list( menus.keys() ) )   # 객체를 리스트 타입 으로 변환 ( py3.0이상 , py3.0미만 안해도된다. )

print( menus.values() )         # 딕셔너리 내 모든 value를 객체로 반환
print( list( menus.values() ) ) # 객체를 리스트 타입 으로 변환

# 반복문 이용한 딕셔너리 순회
# [1]
for element in menus :
    print( element )    # key 가 하나씩 출력
# [2]
for key , value in menus.items() :
    print( key , value )        # key 와 value 같이 출력
# [3]
for key in list( menus.keys() ) :
    print( key )
# [4]
for value in list( menus.values() ) :
    print( value )





















