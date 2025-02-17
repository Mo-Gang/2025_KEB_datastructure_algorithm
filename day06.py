# v1.4 의 v0.7 guess number 예제를 자동화하고 로그파일(guess.txt)을 남기도록 코드를 수정하시오.
# 단, 해당 프로그램이 로그시간을 갖도록 한다.
# 범위는 1~100. 찬스는 7번.
# 힌트: with open('guess.txt', 'w') as fp:
            #fp.write()  # :쓰기함수

# #원래 코드
# import random
#
# answer = random.randint(1, 100)
# chance = 7
#
# while chance != 0:
#     guess = int(input("Input guess number : "))
#     if guess == answer:
#         print(f'You win. Answer is {answer}')
#         break
#     elif guess > answer:
#         chance = chance - 1
#         print(f'{guess} is bigger. Chance left : {chance}')
#     else:
#         chance = chance - 1
#         print(f'{guess} is lower. Chance left : {chance}')
# else:
#     print(f'You lost. Answer is {answer}')


# # 수정한 코드
import random

def guess_number(low, high, answer, chance) -> int:
    mid =  (low+high) // 2
    print(f'Guess number is {mid}')
    fp.write(f'Guess number is {mid}\n')
    while chance != 0:
        if mid == answer:
            print(f'You win. Answer is {answer}')
            fp.write(f'You win. Answer is {answer}\n')
            return
        elif mid > answer:
            chance = chance - 1
            print(f'{mid} is bigger. Chance left : {chance}')
            fp.write(f'{mid} is bigger. Chance left : {chance}\n')
            return guess_number(low, mid-1, answer, chance)
        else:
            chance = chance - 1
            print(f'{mid} is lower. Chance left : {chance}')
            fp.write(f'{mid} is lower. Chance left : {chance}\n')
            return guess_number(mid+1, high, answer, chance)
    else:
        print(f'You lost. Answer is {answer}')
        fp.write(f'You lost. Answer is {answer}')


if __name__ == "__main__":
    low = 1
    high = 100
    chance = 7
    answer = random.randint(low, high)
    with open('guess.txt', 'w') as fp:
        guess_number(low, high, answer, chance)