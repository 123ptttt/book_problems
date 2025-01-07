import pyinputplus as pyip
import random, time

numberqustions = 10
correctAnswer = 0
for question in range(numberqustions):
    number1 = random.randint(0, 9)
    number2 = random.randint(0, 9)

    prompt = '#%s: %s x %s = ' % (question, number1, number2)

    try:
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (number1 * number2)],
                                blockRegexes=[('.*', 'Incorrect')],
                                timeout=8, limit=3)
    except pyip.TimeoutException:
        print("out of time")
    except pyip.RetryLimitException:
        print("out of tries!!!")
    else:
        print("correct!")
        correctAnswer += 1
    time.sleep(1)
