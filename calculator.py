import do_math

class User_Input:
    #Get user input and returns it
    def menuOptions(self):
        print("==============================================================")
        print("==============================================================")
        print("==============================================================")
        print("==============================================================")
        print("This is a calculator built in python")
        print("Only numbers and valid operands such as: ")
        print("+ - * /")
        print("are allowed as inputs")
        print("To clear current input type: clear")
        print("To exit out of the calculator type: exit")
        print("==============================================================")
        print("==============================================================")
        print("==============================================================")
        self.arrangeData()

    def getInput(self):
        #Grab User Input and saves it to var userData
        userData = input()
        print("This is the user data: ",userData)
        return userData


    def arrangeData(self):
        #retrieve user input. Loop through string. 
        #Numbers and Operands get allocated in own containers
        #returns containers
        data = self.getInput()
        dataContainers = Data_Storage()
        num = ""
        
        if(data == "exit"):
            print("You have exited the calculator")
            return
        if(data == "clear"):
            dataContainers.clearAllInputsFromAllLists(dataContainers.numStorage, dataContainers.operandStorage)
            self.arrangeData()
        for i in data:
            while(i.isnumeric()):
                num += i
                i + 1
                print("this is i: ", i, "and this is the num var: ", num)
            dataContainers.numStorage.append(num)
            num = ""    
            # if(ord(i) >= 48 and ord(i) <= 57):
            #     dataContainers.numStorage.append(i)
            if(ord(i) == 42 or ord(i) == 43 or ord(i) == 45 or ord(i) == 47):     
                dataContainers.operandStorage.append(i) 
            else:
                print("Invalid Input")
                dataContainers.clearAllInputsFromAllLists(dataContainers.numStorage, dataContainers.operandStorage)
                self.arrangeData()
        
        operations = Do_Math()
        while(len(dataContainers.numStorage) > 1):
            operations.orderOfOperations(dataContainers)
            # operations.convertStrings(dataContainers)
        
        #Recursive state
        if(len(dataContainers.numStorage) <= 1 and len(dataContainers.operandStorage) == 0):
            self.arrangeData()
        else:
            return print("Error: Invalid Input")    



class Do_Math:
    #Grab input from containers and do math
    def orderOfOperations(self, containers):
        result = None
        num1 = None
        num2 = None
        numIndex = None
        operand = None


        for i in containers.operandStorage:
            print("this is the i in the orderOfOperations container: ", i, "Indicie is: ", containers.operandStorage.index(i))
            if(i == "/" or i == "*"):
               numIndex = containers.operandStorage.index(i) 
               operand = i
               num1 = containers.numStorage[numIndex]
               num2 = containers.numStorage[numIndex + 1]
               result = self.doMath(num1, num2, operand)
               print("this is the result in the order ofOperations: ", result, "this is num1 and num2: ", num1, " ", num2)
               print("this is the num container: ", containers.numStorage)
               self.removeInputsFromList(containers, numIndex)
               containers.numStorage.insert(numIndex,result)

        
        for i in containers.operandStorage:
            print("this is the i in the orderOfOperations container: ", i, "Indicie is: ", containers.operandStorage.index(i))
            if(i == "+" or i == "-"):
                numIndex = containers.operandStorage.index(i)
                operand = i
                print("this is the containers: ", containers.operandStorage, "num container: ", containers.numStorage)
                num1 = containers.numStorage[numIndex]
                num2 = containers.numStorage[numIndex + 1]
                result = self.doMath(num1, num2, operand)
                print("this is the result in the order ofOperations: ", result, "this is num1 and num2: ", num1, " ", num2)
                print("this is the num container: ", containers.numStorage)
                self.removeInputsFromList(containers, numIndex)
                containers.numStorage.insert(numIndex,result)

        print("current input: ", result, " Current num storage: ", containers.numStorage)
     
    def convertStrings(self, containers):
        numStorage = containers.numStorage
        operandStorage = containers.operandStorage
        firstNum = float(numStorage[0])
        secondNum = float(numStorage[1])
        operand = operandStorage[0]
        result = None

        result = self.doMath(firstNum, secondNum, operand)
        self.removeInputsFromList(numStorage, operandStorage)
        if(result != "Cannot Divide By Zero"):
            numStorage.insert(0,result)
        print("current input: ", result)


    def doMath(self, firstNum, secondNum, operand):
        result = None
        firstNumConvert = float(firstNum)
        secondNumConvert = float(secondNum)
        
        if(operand == "+"):
            result = firstNumConvert + secondNumConvert
        elif(operand == "-"):
            result = firstNumConvert - secondNumConvert
        elif(operand == "/"):
            if(secondNum == 0):
                result = "Cannot Divide By Zero"
            else:    
                result = firstNumConvert / secondNumConvert
        elif(operand == "*"):
            result = firstNumConvert * secondNumConvert
        else:
            return "Invalid Operand"
                   
        return result

    # def divideByZero(self, operand, secondNum):
    #     if(operand == "/" and secondNum == 0):
    #         result = "invalid"

    def removeInputsFromList(self, containers, numIndex):
        print("this is the num index start: ", numIndex)
        print("this is the stop at: ", numIndex + 2)
        del containers.numStorage[numIndex : numIndex + 2]
        containers.operandStorage.pop(numIndex)
        print("this is the operand contianer: ", containers.operandStorage)

class Data_Storage:
    #containers for numbers and operands
    #added the dev branch
    numStorage = []
    operandStorage = []

    def clearAllInputsFromAllLists(self, numStorage, operandStorage):
        numStorage.clear()
        operandStorage.clear()


def main():
    userData = User_Input()
    userData.menuOptions()
    
  
if __name__ == "__main__":
  main()