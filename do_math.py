class Do_Math:
    #Grab input from containers and do math
    def convertStrings(self, containers):
        numStorage = containers.numStorage
        operandStorage = containers.operandStorage
        firstNum = float(numStorage[0])
        secondNum = float(numStorage[1])
        operand = operandStorage[0]
        result = None

        result = self.doMath(firstNum, secondNum, operand)
        self.removeInputsFromList(numStorage, operandStorage)
        numStorage.insert(0,result)
        print("this is the result: ", result)


    def doMath(self, firstNum, secondNum, operand):
        result = None

        if(operand == "+"):
            result = firstNum + secondNum
        elif(operand == "-"):
            result = firstNum - secondNum
        elif(operand == "/"):
            result = firstNum / secondNum
        elif(operand == "*"):
            result = firstNum * secondNum
        else:
            return "Invalid Operand"
                   
        return result

    def removeInputsFromList(self, numContainer, operandContainer):
        del numContainer[0:2]
        del operandContainer[0:1]

