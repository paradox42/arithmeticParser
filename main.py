inputArr = []
outputArr = []


def readFile():
    global inputArr
    f = open("./input", "r")
    for line in f:
        inputArr.append(line)
    f.close()


def validate(line):
    i = 0
    operators = {"+", "-", "*", "/"}
    operants = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
    validationMsg = "Valid input"
    parenCounter = 0
    length = len(line)
    while i < length:
        if i == 0:
            if line[i] == '0' and line[i + 1] not in operators and line[i+1] != ')':
                validationMsg = (
                    "Invalid starting of input, first input contains multiple 0's"
                )
                break
            if line[i] in operators or line[i] == ")":
                validationMsg = "Invalid starting of input, first input must be a number, open parentheses or a single 0"
                break
            if line[i] == '(':
                parenCounter += 1
        elif i == length - 1:
            if line[i] in operators:
                validationMsg = "Invalid end of input, end of input cannot be a operator"
            elif line[i] == ')':
                parenCounter -= 1
        else:
            if line[i] in operators and line[i+1] in operators:
                validationMsg = "Too many operators"
                break
            if line[i] == '0' and line[i + 1] not in operators and line[i+1] != ')':
                validationMsg = "Invalid input of 0, too many 0's"
                break
            if line[i] == '(' and line[i+1] == ')':
                validationMsg = "Invalid oepn/close parentheses, there must a expression in parentheses"
                break
            if line[i] == '(':
                parenCounter += 1
            elif line[i] == ')':
                parenCounter -= 1
                if parenCounter < 0:
                    validationMsg = "Too many close parentheses"
        i += 1
    if parenCounter != 0:
        validationMsg = "Open parentheses does not match closed parentheses"
    return validationMsg


if __name__ == "__main__":
    readFile()
    for line in inputArr:
        outputArr.append(validate(line))
    for msg in outputArr:
        print(outputArr)