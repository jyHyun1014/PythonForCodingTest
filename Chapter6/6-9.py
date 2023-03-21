# 정렬 라이브러리에서 key를 활용한 소스코드

array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)     # key 값으로 정렬 기준인 함수가 들어가야 함
print(result)