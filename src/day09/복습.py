# 딕셔너리 복습
    # data = { key : [ { key : [ ] } , { key : [ ] } , { key : [ ] } ] }
    # key : [ { key : [ ] } , { key : [ ] } , { key : [ ] } ]
    # { key : [ ] } , { key : [ ] } , { key : [ ] }
    # [ ]
data = {
  "squadName": "Super hero squad",
  "homeTown": "Metro City",
  "formed": 2016,
  "secretBase": "Super tower",
  "active": "true",
  "members": [
    {
      "name": "Molecule Man",
      "age": 29,
      "secretIdentity": "Dan Jukes",
      "powers": ["Radiation resistance", "Turning tiny", "Radiation blast"]
    },
    {
      "name": "Madame Upper",
      "age": 39,
      "secretIdentity": "Jane Wils",
      "powers": [
        "Million tonne punch",
        "Damage resistance",
        "Superhuman reflexes"
      ]
    },
    {
      "name": "Eternal Flame",
      "age": 10000,
      "secretIdentity": "Unknown",
      "powers": [
        "Immortality",
        "Heat Immunity",
        "Inferno",
        "Teleportation",
        "Interdimensional travel"
      ]
    }
  ]
}
# [풀이 ]
# 상자/딕셔너리/리스트 하나씩 오픈 하기
    # 1. 딕셔너리 전체구역
print( data )
    # 2. 딕셔너리 내 각 key를 이용한 value 호출
print( data['active'] , data['formed'] , data['squadName'] , data['homeTown'] , data['secretBase'] , data['members'] )
    # 3. members 리스트
print( data['members'][0] , data['members'][1] , data['members'][2] )

print( data['members'][0]['name'] )   # 4. 첫번째 멤버의 이름 호출
print( data['members'][0]['age'] )   # 4. 첫번째 멤버의 나이 호출
print( data['members'][0]['powers'])
    # 5.
print( data['members'][0]['powers'][0] )

#############
# [결과]
print( f'squadName : {data['squadName']}')
print( f'homeTown : {data['homeTown']}')
print( f'formed : {data['formed']}')
print( f'secretBase : {data['secretBase']}')
print('members')
print( f'{ "name":<20}{"age":<20}{"secretIdentity":<20}{"powers":<20}')
for member in data['members'] :
    name = member['name']
    age = member['age']
    secretIdentity = member['secretIdentity']
    powers = member['powers']
    print( f'{ name:<20}{ age:<20}{ secretIdentity:<20}{ " / ".join( powers ) }')
# ' ' 문자열 안에서 문자열 표현할때 '  " "  '
# " " 문자열 안에서 문자열 표현할때 "  ' '  "
# f'문자열{ 연산/변수/값/함수호출 }문자열문자열{ 연산/변수/값/함수호출 }문자열' : 문자열포매팅
    # 정렬 :   { 값:<칸수 }  : 칸수 만큼 데이터 채운후 왼쪽 정렬
    # 정렬 :   { 값:>칸수 }  : 칸수 만큼 데이터 채운후 오른쪽 정렬
    # 정렬 :   { 값:^칸수 }  : 칸수 만큼 데이터 채운후 가운데 정렬
# '문자열'.join( 리스트 ) : 리스트내 각 요소들 사이사이에 해당 문자열이 삽입된 전체문자열를 반환




