
from pulp import *


class Optimizer:
    # Списки, що необхідні для роботи
    megalist = []
    dictionaryVariableAndDeatilInfo = dict()
    dictionary = dict()
    variableNameList = []


    def __init__(self, videocardsList, motherboardList, powerSupplyList, processorsList, ramList, storageList):
        self.videocardsList = videocardsList
        self.motherboardList = motherboardList
        self.powerSupplyList = powerSupplyList
        self.processorsList = processorsList
        self.ramList = ramList
        self.storageList = storageList

        self.megalist = processorsList + videocardsList + motherboardList + ramList + storageList + powerSupplyList

    def initializeDictionarys(self):
        # Лічильники для іменування набору деталей
        countProc = 0
        countVideo = 0
        countPlata = 0
        coutRAM = 0
        coutnDisk = 0
        countBlock = 0

        # Цилк іменує спеціальним чином змінні моделі та ініціалізує їх засобами бібліотеки для оптимізації
        for i in range(len(self.megalist)):
            currentVaribleName = self.megalist[i].TYPE_DETAIL
            if currentVaribleName == "Processors":
                self.dictionary[currentVaribleName + str(countProc)] = pulp.LpVariable(
                    currentVaribleName + str(countProc),
                    lowBound=0, upBound=1)
                print(currentVaribleName + str(countProc))
                self.dictionaryVariableAndDeatilInfo[currentVaribleName + str(countProc)] = self.megalist[i]
                countProc += 1
            elif currentVaribleName == "Videocard":
                self.dictionary[currentVaribleName + str(countVideo)] = pulp.LpVariable(
                    currentVaribleName + str(countVideo),
                    lowBound=0, upBound=1)
                print(currentVaribleName + str(countVideo) + ": " + str(self.megalist[i]))
                self.dictionaryVariableAndDeatilInfo[currentVaribleName + str(countVideo)] = self.megalist[i]
                countVideo += 1
            elif currentVaribleName == "Motherboard":
                self.dictionary[currentVaribleName + str(countPlata)] = pulp.LpVariable(
                    currentVaribleName + str(countPlata),
                    lowBound=0, upBound=1)
                print(currentVaribleName + str(countPlata))
                self.dictionaryVariableAndDeatilInfo[currentVaribleName + str(countPlata)] = self.megalist[i]
                countPlata += 1
            elif currentVaribleName == "RAM":
                self.dictionary[currentVaribleName + str(coutRAM)] = pulp.LpVariable(currentVaribleName + str(coutRAM),
                                                                                     lowBound=0)
                print(currentVaribleName + str(coutRAM))
                self.dictionaryVariableAndDeatilInfo[currentVaribleName + str(coutRAM)] = self.megalist[i]
                coutRAM += 1
            elif currentVaribleName == "Disk":
                self.dictionary[currentVaribleName + str(coutnDisk)] = pulp.LpVariable(
                    currentVaribleName + str(coutnDisk),
                    lowBound=0, upBound=1)
                print(currentVaribleName + str(coutnDisk))
                self.dictionaryVariableAndDeatilInfo[currentVaribleName + str(coutnDisk)] = self.megalist[i]
                coutnDisk += 1
            elif currentVaribleName == "Block":
                self.dictionary[currentVaribleName + str(countBlock)] = pulp.LpVariable(
                    currentVaribleName + str(countBlock),
                    lowBound=0, upBound=1)
                print(currentVaribleName + str(countProc))
                self.dictionaryVariableAndDeatilInfo[currentVaribleName + str(countBlock)] = self.megalist[i]
                countBlock += 1

        for i in self.dictionary.keys():
            self.variableNameList.append(i)

    def optimize(self):
        # Вираження математичної моделі в коді:
        # Функція мети
        problem = pulp.LpProblem('Оптимізація', pulp.LpMinimize)
        problem += lpSum(
            self.dictionary[self.variableNameList[j]] * self.megalist[j].price for j in
            range(len(self.megalist))), "Функция цели"

        # Обеження кількості деталей в ПК
        problem += lpSum(self.dictionary.get("Processors" + str(j)) for j in range(len(self.processorsList))) == 1
        problem += lpSum(self.dictionary.get("RAM" + str(j)) for j in range(len(self.ramList))) == 1
        problem += lpSum(self.dictionary.get("Plata" + str(j)) for j in range(len(self.motherboardList))) == 1
        problem += lpSum(self.dictionary.get("Videocard" + str(j)) for j in range(len(self.videocardsList))) == 1
        problem += lpSum(self.dictionary.get("Disk" + str(j)) for j in range(len(self.storageList))) == 1
        problem += lpSum(self.dictionary.get("Block" + str(j)) for j in range(len(self.powerSupplyList))) == 1

        # Користувацькі обмеження

        # Розмір оперативної пам'яті
        problem += lpSum(
            self.dictionary.get("RAM" + str(j)) * int(self.dictionaryVariableAndDeatilInfo.get("RAM" + str(j)).size) for j in
            range(len(self.ramList))) >= 4.0, "2"

        # Тактова частота процесора
        problem += lpSum(self.dictionary.get("Processors" + str(j)) * int(
            self.dictionaryVariableAndDeatilInfo.get("Processors" + str(j)).clock_frequency) for j in
                         range(len(self.processorsList))) >= 2

        # Блок живлення: потужність повинна перевищувати сумарне споживання деталей
        problem += 1.2 * (
                lpSum(self.dictionary.get("Processors" + str(j)) * int(
                    self.dictionaryVariableAndDeatilInfo.get("Processors" + str(j)).power_usage) for j in
                      range(len(self.processorsList)))
                +
                lpSum(self.dictionary.get("Videocard" + str(j)) * int(
                    self.dictionaryVariableAndDeatilInfo.get("Videocard" + str(j)).powerUsage) for j in
                      range(len(self.videocardsList)))
        ) \
                   <= \
                   lpSum(self.dictionary.get("Block" + str(j)) * int(
                       self.dictionaryVariableAndDeatilInfo.get("Block" + str(j)).power) for j in
                         range(len(self.powerSupplyList)))

        problem.solve()

        print("Результат:")
        for variable in problem.variables():
            if variable.varValue == 1:
                print(self.dictionaryVariableAndDeatilInfo[variable.name])
                print(variable.name + " " + str(variable.varValue))

        print("Прибыль:")
        print(value(problem.objective))
        print(problem.name)

        return problem
