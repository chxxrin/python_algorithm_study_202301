letter = input().upper() #letter은 입력받은 문자열이며, 대소문자를 구분하지 않으므로 upper함수로 문자열을 모두 대문자로 변환
letter_list = list(set(letter)) #입력받은 문자열인 letter에서 중복값을 제거하고, 리스트로 변환
count_list = [] #새로운 리스트 생성. 여기에는 입력받은 문자열의 각 문자의 갯수를 저장

for i in letter_list:
    num = letter.count(i) #입력받은 문자열의 갯수를 순서대로 세서 num변수에 저장
    count_list.append(num) #갯수를 세고 저장한 num변수를 리스트에 차례대로 append

if count_list.count(max(count_list)) > 1: #만약 lst에서의 최댓값의 갯수가 1개 이상이면 ?를 출력
    print("?")
else: #그게 아니면 lst에서의 최댓값을 가지는 문자의 인덱스를 찾음
    max_index = count_list.index(max(count_list))
    print(letter_list[max_index])


# set() : 집합 자료형 set은자료형의 중복을 제거하기 위한 필터
# count(x) : list안에 x가 몇 개 있는지 조사해 그 개수를 돌려줌
# index(x) : list에 x값이 있으면 x의 위치값을 돌려줌
# max(lst) : lst라는 list안에서의 최댓값을 돌려줌
# append(x) : list에 x를 추가해줌
# list(x) : x를 list형식으로 변환해줌