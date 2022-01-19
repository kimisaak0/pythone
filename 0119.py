# 예외처리

# try:
#     print("나누기 전용 계산기입니다.")
#     list = []
#     list.append(int(input("첫 번째 숫자를 입력하세요 : ")))
#     list.append(int(input("두 번째 숫자를 입력하세요 : ")))
#     list.append(list[0]/list[1])
#     print("{0}/{1} = {2}".format(list[0],list[1], int(list[2])))
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err :
#     print(err)
# except Exception as arr:
#     print("예상하지 못한 에러가 발생하였습니다.")
#     print(arr)

#에러 만들기

# try:
#     print("한자리 수 나누기 전용 계산기입니다.")
#     list = []
#     list.append(int(input("첫 번째 숫자를 입력하세요 : ")))
#     list.append(int(input("두 번째 숫자를 입력하세요 : ")))
#     if list[0] >= 10 or list[1] >= 10:
#         raise ValueError
#     list.append(list[0]/list[1])
#     print("{0}/{1} = {2}".format(list[0],list[1], int(list[2])))
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err :
#     print(err)
# except Exception as arr:
#     print("예상하지 못한 에러가 발생하였습니다.")
#     print(arr)

#사용자 정의 에러 만들기
class BigNumberErr(Exception) :
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

try:
    print("한자리 수 나누기 전용 계산기입니다.")
    list = []
    list.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    list.append(int(input("두 번째 숫자를 입력하세요 : ")))
    if list[0] >= 10 or list[1] >= 10:
        raise BigNumberErr("입력값 : {0}, {1}".format(list[0], list[1]))
    list.append(list[0]/list[1])
    print("{0}/{1} = {2}".format(list[0],list[1], int(list[2])))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err :
    print(err)
except BigNumberErr as err:
    print("에러가 발생했습니다.")
    print(err)
except Exception as err:
    print("예상하지 못한 에러가 발생하였습니다.")
    print(err)
#finally 
finally:
    print("Thank you")