
class movieTheater(object):
    def __init__(self, name, time, money):
        self.name = name
        self.time = time
        self.money = money

    def showTime(self):
        print(self.time)

    def earnMoney(self, newMoney):
        self.meney = self.money + newMoney


class Seat(object): #Seat 클래스는 좌석 예매 기능을 좀 더 쉽게 하기 위해 구현, 시간대별 좌석 구분을 위해 구현: seat(double array)
    def __init__(self, seat):
        self.seat = seat

    def showSeat(self):
    #좌석 예매 기능에서 좌석을 미리 보여줘야 하므로 구현해야 하는 부분
    #좌석은 이중 배열로 구성, 배열에 저장된 값이 0이면 열은 A, B, C, D, E로 행은 1, 2, 3, 4, 5로 출력
    #저장된 값이 1이면 이미 예약이 된 좌석이므로 예약 불가능하다는 의미의 'X'로 출력

        print("X는 예매가 완료된 좌석입니다.")
        for i in range(5):
            for j in range(5):
                if self.seat[i][j] == 0:
                    if i == 0:
                        print('A'+ str(j+1) , end=' ')
                    if i == 1:
                        print('B'+ str(j+1), end=' ')
                    if i == 2:
                        print('C'+ str(j+1), end=' ')
                    if i == 3:
                        print('D'+ str(j+1) , end=' ')
                    if i == 4:
                        print('E'+ str(j+1) , end=' ')
                elif self.seat[i][j] == 1:
                    print("X  ",end="")
            print("\n")

    def reserveSeat(self):  # 실제 좌석 예매를 진행하는 함수, 표의 수와 표의 종류를 구분할 수 있음. 함수의 반환 값은 money로, 표의 종류를 인자로 받을 때 수익을 함께 계산하여 반환함으로써 조금 더 간단한 수익 계산 진행 가능
        flag = 1  # 모든 좌석이 예매된 경우 더 이상 예매를 할 수 불가하도록 설정하기 위한 장치
        for i in range(5):
            for j in range(5):
                flag = self.seat[i][j] * flag
        if flag == 1:
            print("모든 좌석이 예매되었습니다.")
            return 0
        n = int(input("예약할 표의 수를 입력하세요\n"))
        if n < 0 or n > 25:  # 예외 처리 부분, 예를 들어 인원이 음수이거나 영화관 좌석 수보다 많은 수를 예매하려 할 때, 예외가 발생하지 않을 때까지 재귀 호출되고 그 때의 money가 반환
            print("음수와 25보다 큰 수는 입력하지 마세요. 다시 예매를 진행하세요.")
            money = self.reserveSeat()
            return money
        junior = int(input("어린이는 몇 명입니까?\n"))
        if junior < 0 or junior > n:  # 예외 처리 부분, 어린이 수가 n보다 많거나 음수인 경우 예외가 생기지 않을 때까지 재귀 호출되고 그 때의 money가 반환
            print("인원이 맞지 않습니다. 음수는 입력하지 마세요. 다시 예매를 진행하세요.")
            money = self.reserveSeat()
            return money
        senior = int(input("청소년은 몇명입니까?\n"))
        if senior < 0 or senior > n:  # 예외 처리 부분, 청소년 수가 n보다 많거나 음수인 경우 예외가 생기지 않을 때 까지 재귀 호출되고 그 때의 money가 반환
            print("인원이 맞지 않습니다. 음수는 입력하지 마세요. 다시 예매를 진행하세요.")
            money = self.reserveSeat()
            return money
        adult = n - junior - senior
        if adult < 0:  # 예외 처리 부, 예를 들어 예매할 표의 수가 4일 때 어린이가 5명, 청소년이 8명 입력된 경우 함수가 재귀적으로 실행. 예외가 생기지 않을 때까지 재귀 호출되고 그 때의 money가 반환
            print("인원이 맞지 않습니다. 다시 예매를 진행하세요.")
            money = self.reserveSeat()
            return money
        else:
            for k in range(n):
                i = int(input("예약할 좌석의 열(1, 2, 3, 4, 5)를 입력하세요. 1열은 A를 의미합니다.\n"))
                j = int(input("예약할 좌석의 행(1, 2, 3, 4, 5)을 입력하세요\n"))
                if self.seat[i - 1][ j - 1] == 1:  # 예외 처리 부분, 이미 예약된 좌석에 예매를 시도한 경우 함수가 재귀 실행. 예외가 생기지 않을 때까지 재귀 호출되고 그 때의 money가 반환
                    print("이미 예매된 좌석입니다. 다시 예매를 진행하세요.")
                    money = self.reserveSeat()
                    return money
                else:
                    self.seat[i - 1][j - 1] = 1
        print("예매가 완료되었습니다.")
        money = junior * 5000 + senior * 8000 + adult * 10000
        return money


#영화관(1, 2, 3)별로 클래스의 초기화를 진행하며, 시간대별로 좌석 클래스도 초기화. 처음에는 모두 빈 좌석이므로 0으로 배열 초기화
movie1 = movieTheater("검은사제들",'9:00     12:00     15:00     18:00', 0)
movie1_time1 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
movie1_time2 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
movie1_time3 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
movie1_time4 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])

movie2 = movieTheater("내부자들", '10:15     13:30     16:45     20:00', 0)
movie2_time1 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
movie2_time2 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
movie2_time3 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
movie2_time4 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])

movie3 = movieTheater("마션", '7:30     10:00     15:00', 0)
movie3_time1 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
movie3_time2 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
movie3_time3 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])

TRUE = 1
FALSE = 0
BOOL = TRUE  # 메뉴 반복 실행을 위한 flag
benefit = 0  # 수익 계산시 사용

while TRUE:
    print("1. 영화 예매")
    print("2. 영화 시간표 확인")
    print("3. 영화 좌석 확인")
    print("4. 총 수입 보기")
    print("5. 시스템 종료")
    choiceMenu = str(input("실행할 것을 선택하세요\n"))  # 위 4가지 기능 중 어떤 기능을 실행해야 하는지 판단하는 flag

    if choiceMenu == '1':  # 좌석 예매 기능
        print("1. " + movie1.name)
        print("2. " + movie2.name)
        print("3. " + movie3.name)
        choiceMovie = str(input("몇 번째 영화를 보시겠습니까\n"))  # 영화 종류 선택
        if choiceMovie == '1':
            movie1.showTime()
            choiceTime = str(input("영화의 상영 순서를 선택해주세요\n"))  # 상영 시간 선택
            if choiceTime == '1':
                movie1_time1.showSeat()  # 좌석을 보여주고 예매 진행, 예매에서 얻은 수익을 영화관 클래스의 money에 추가
                benefit = movie1_time1.reserveSeat()
                movie1.earnMoney(benefit)
            elif choiceTime == '2':
                movie1_time2.showSeat()
                benefit = movie1_time2.reserveSeat()
                movie1.earnMoney(benefit)
            elif choiceTime == '3':
                movie1_time3.showSeat()
                benefit = movie1_time3.reserveSeat()
                movie1.earnMoney(benefit)
            elif choiceTime == '4':
                movie1_time4.showSeat()
                benefit = movie1_time4.reserveSeat()
                movie1.earnMoney(benefit)
            else:
                print("해당 시간은 존재하지 않습니다. 1에서 4사이의 시간을 입력해주세요. 프로그램을 다시 시작합니다.")
        elif choiceMovie == '2':
            movie2.showTime()
            choiceTime = str(input("영화의 상영 순서를 선택해주세요\n"))
            if choiceTime == '1':
                movie2_time1.showSeat()
                benefit = movie2_time1.reserveSeat()
                movie2.earnMoney(benefit)
            elif choiceTime == '2':
                movie2_time2.showSeat()
                benefit = movie2_time2.reserveSeat()
                movie2.earnMoney(benefit)
            elif choiceTime == '3':
                movie2_time3.showSeat()
                benefit = movie2_time3.reserveSeat()
                movie2.earnMoney(benefit)
            elif choiceTime == '4':
                movie2_time4.showSeat()
                benefit = movie2_time4.reserveSeat()
                movie2.earnMoney(benefit)
            else:
                print("해당 시간은 존재하지 않습니다. 1에서 4사이의 시간을 입력해주세요. 프로그램을 다시 시작합니다.")
        elif choiceMovie == '3':
            movie3.showTime()
            choiceTime = str(input("영화의 상영 순서를 선택해주세요\n"))
            if choiceTime == '1':
                movie3_time1.showSeat()
                benefit = movie3_time1.reserveSeat()
                movie3.earnMoney(benefit)
            elif choiceTime == '2':
                movie3_time2.showSeat()
                benefit = movie3_time2.reserveSeat()
                movie3.earnMoney(benefit)
            elif choiceTime == '3':
                movie3_time3.showSeat()
                benefit = movie3_time3.reserveSeat()
                movie3.earnMoney(benefit)
            else:
                print("해당 시간은 존재하지 않습니다. 1에서 3사이의 시간을 입력해주세요. 프로그램을 다시 시작합니다.")
        else:
            print("없는 영화입니다. 1에서 3사이의 정수를 입력해주세요. 프로그램을 다시 시작합니다.")

    elif choiceMenu == '2':
        print(movie1.time+'\n'+movie2.time+'\n'+movie3.time)
    elif choiceMenu == '3':
        print(movie1_time1.showSeat())
    elif choiceMenu == '4':
        print("아직 구현하지 않았어요!!")
    elif choiceMenu == '5':
        print('감사합니다 다음에도 찾아주세요!')
        break
    else:
        print("1에서 5까지의 정수만 입력해주세요")

