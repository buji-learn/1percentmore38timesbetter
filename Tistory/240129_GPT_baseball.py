import random

def generate_secret_number(n):
    """1부터 9까지 서로 다른 임의의 숫자로 이루어진 비밀 숫자 생성"""
    return random.sample(range(1, 10), n)

def check_guess(secret, guess, n):
    """비밀 숫자와 추측한 숫자를 비교하여 스트라이크와 볼 계산"""
    strikes, balls = 0, 0
    for i in range(n):
        if guess[i] == secret[i]:
            strikes += 1
        elif guess[i] in secret:
            balls += 1
    return strikes, balls

def play_number_baseball():
    """숫자 야구 게임 실행"""
    print("숫자 야구 게임을 시작합니다!")
    n = 4
    secret_number = generate_secret_number(n)
    attempts = 0

    while True:
        user_input = input(str(n) + "자리 숫자를 입력하세요 (1부터 9까지의 서로 다른 숫자): ")
        
        try:
            user_guess = [int(x) for x in user_input]
        except ValueError:
            print("올바른 형식의 숫자를 입력하세요.")
            continue

        if len(user_guess) != n or len(set(user_guess)) != n or any(x < 1 or x > 9 for x in user_guess):
            print("1부터 9까지의 서로 다른 " + str(n) + "자리 숫자를 입력하세요.")
            continue

        attempts += 1
        strikes, balls = check_guess(secret_number, user_guess, n)

        print(f"결과: {strikes} 스트라이크, {balls} 볼")

        if strikes == n:
            print(f"축하합니다! "+ str(n) + "번 만에 비밀 숫자를 맞추셨습니다.")
            break

if __name__ == "__main__":
    play_number_baseball()