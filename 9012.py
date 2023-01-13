T = int(input()) #입력은 T개의 테스트 데이터

for i in range(T): #총 T번 반복
    stack = [] #빈 stack 생성
    PS = input() #괄호들을 input으로 입력받음

    for check in PS:
        if check == '(': #만약 ( 이 나오면 그대로 stack에 append
            stack.append('(')
        elif check == ')': #만약 ) 이 나오면
            if stack: #stack 검사해서 비어있지 않으면
                stack.pop() #pop()을 해줌
            else: #stack 검사해서 비어있다면
                print("NO") #NO를 출력해줌
                break #그리고 break!
    else: #elif문에서 break로 끊기지 않고 여기까지 왔을 때
        if not stack: #stack이 비어있으면 모든 ()가 짝이 맞은 경우이므로
                print("YES") #YES 출력해줌
        else: #elif문에서 break로 끊기지 않았더라도 stack이 비어있지 않으면 모든 ()가 짝이 맞지 않은 경우이므로
                print("NO") #NO를 출력해줌
