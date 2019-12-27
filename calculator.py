
class User_Input:
    #Get user input and returns it
    def menuOptions(self):
        print("This is a calculator built in python")
        print("Only numbers and valid operands such as: ")
        print("+ - * /")
        print("are allowed as inputs")
        print("To exit out of the calculator type: exit")
        print("==============================================================")
        print("==============================================================")
        print("==============================================================")
        self.arrangeData()

    def getInput(self):
        userData = input()
        print("This is the user data: ",userData)
        return userData


    def arrangeData(self):
        #retrieve user input. Loop through string. 
        #Numbers and Operands get allocated in own containers
        #returns containers
        data = self.getInput()
        dataContainers = Data_Storage()
        if(data == "exit"):
            return print("You have exited the calculator")
        for i in data:
            if(ord(i) >= 48 and ord(i) <= 57):
                dataContainers.numStorage.append(i)
            elif(ord(i) == 42 or ord(i) == 43 or ord(i) == 45 or ord(i) == 47):     
                dataContainers.operandStorage.append(i)    
            else:
                return print("invalid input")
        
        operations = Do_Math()
        while(len(dataContainers.numStorage) > 1):
            operations.convertStrings(dataContainers)
        
        if(len(dataContainers.numStorage) == 1):
            self.arrangeData()



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


class Data_Storage:
    #containers for numbers and operands
    numStorage = []
    operandStorage = []


def main():
    userData = User_Input()
    userData.menuOptions()
    
  
if __name__ == "__main__":
  main()