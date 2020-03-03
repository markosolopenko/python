import pyinputplus as pyip
import random, time
def my_own_multiplication_quiz():
    number_of_questions = 10
    correct_answers = 0
    for question in range(1,number_of_questions + 1):
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        prompt = f'#{question}: {num1} x {num2} = '
        try:
            pyip.inputStr(prompt, allowRegexes=[f'^{num1 * num2}$'],
                          blockRegexes=[('.*', 'Incorrect!')],
                          timeout=8, limit=3)
        except pyip.TimeoutException:
            print('Out of time!')
        except pyip.RetryLimitException:
            print('Out of tries!')
        else:
            print('Correct!')
            correct_answers += 1
        time.sleep(1)
    print(f'Score: {correct_answers} {number_of_questions}')

if __name__ == "__main__":
    my_own_multiplication_quiz()