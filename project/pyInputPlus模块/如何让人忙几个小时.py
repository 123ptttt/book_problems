import pyinputplus as pyip

while True:
    prompt = "Want to know how to keep person work for hours:\n"
    response = pyip.inputYesNo(prompt)
    if response == "no":
        break
print("Thankyou, wish a nice day")