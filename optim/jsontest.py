import json
from pulp import *

from pojo.Processors import Processors
from pojo.Videocard import Videocard
from pojo.RAM import RAM
from pojo.Storage import Storage
from pojo.PowerSupply import PowerSupply
from pojo.Motherboard import Motherboard

data = []
with open("C:\\Users\\Roman\\Desktop\\jsontestpy.txt", "r") as read_file:
    data = json.load(read_file)

videocardsList = []
for videocard in data['videocardsList']:
    videocardsList.append(
        Videocard(videocard['name'], videocard['graphicsCoreFrequency'], videocard['videoMemory_Size'],
                  videocard['memoryBusCapacity'], videocard['videoMemoryOperatingFrequency'], videocard['powerUsage'],
                  videocard['price']))

print(len(videocardsList))

motherboardList = []
for board in data['motherboardList']:
    motherboardList.append(
        Motherboard(board['name'], board['formFactor'], board['ramSlots'], board['price']))

print(len(motherboardList))

powerSupplyList = []
for power in data['powerSupplyList']:
    powerSupplyList.append(
        PowerSupply(power['name'], power['power'], power['price']))

print(len(powerSupplyList))

processorsList = []
for proc in data['processorsList']:
    processorsList.append(Processors(proc['name'], proc['clockFrequency'],
                                     proc['capacity'], proc['cacheMemory'],
                                     proc['core'], proc['price'], proc['powerUsage']))

print(len(processorsList))

ramList = []
for ram in data['ramList']:
    ramList.append(
        RAM(ram['name'], ram['type'], ram['price'], ram['size'], ram['frequency']))
    print(ram['name'] + " " + str(ram['size']))

print(len(ramList))

storageList = []
for stor in data['storageList']:
    storageList.append(
        Storage(stor['name'], stor['powerUsage'], stor['price'], stor['type'], stor['size']))

print(len(storageList))

# ********************************
# Оптимізація
# ********************************

# Створення загального списку з деталями
megalist = processorsList + videocardsList + motherboardList + ramList + storageList + powerSupplyList

# Створення словника зі змінними моделі
dictionary = dict()

# Лічильники для іменування набору деталей
countProc = 0
countVideo = 0
countPlata = 0
coutRAM = 0
coutnDisk = 0
countBlock = 0

dictionaryVariableAndDeatilInfo = dict()

# Цилк іменує спеціальним чином змінні моделі та ініціалізує їх засобами бібліотеки для оптимізації
for i in range(len(megalist)):
    currentVaribleName = megalist[i].TYPE_DETAIL
    if currentVaribleName == "Processors":
        dictionary[currentVaribleName + str(countProc)] = pulp.LpVariable(currentVaribleName + str(countProc),
                                                                          lowBound=0, upBound=1)
        print(currentVaribleName + str(countProc))
        dictionaryVariableAndDeatilInfo[currentVaribleName + str(countProc)] = megalist[i]
        countProc += 1
    elif currentVaribleName == "Videocard":
        dictionary[currentVaribleName + str(countVideo)] = pulp.LpVariable(currentVaribleName + str(countVideo),
                                                                           lowBound=0, upBound=1)
        print(currentVaribleName + str(countVideo) + ": " + str(megalist[i]))
        dictionaryVariableAndDeatilInfo[currentVaribleName + str(countVideo)] = megalist[i]
        countVideo += 1
    elif currentVaribleName == "Motherboard":
        dictionary[currentVaribleName + str(countPlata)] = pulp.LpVariable(currentVaribleName + str(countPlata),
                                                                           lowBound=0, upBound=1)
        print(currentVaribleName + str(countPlata))
        dictionaryVariableAndDeatilInfo[currentVaribleName + str(countPlata)] = megalist[i]
        countPlata += 1
    elif currentVaribleName == "RAM":
        dictionary[currentVaribleName + str(coutRAM)] = pulp.LpVariable(currentVaribleName + str(coutRAM), lowBound=0)
        print(currentVaribleName + str(coutRAM))
        dictionaryVariableAndDeatilInfo[currentVaribleName + str(coutRAM)] = megalist[i]
        coutRAM += 1
    elif currentVaribleName == "Disk":
        dictionary[currentVaribleName + str(coutnDisk)] = pulp.LpVariable(currentVaribleName + str(coutnDisk),
                                                                          lowBound=0, upBound=1)
        print(currentVaribleName + str(coutnDisk))
        dictionaryVariableAndDeatilInfo[currentVaribleName + str(coutnDisk)] = megalist[i]
        coutnDisk += 1
    elif currentVaribleName == "Block":
        dictionary[currentVaribleName + str(countBlock)] = pulp.LpVariable(currentVaribleName + str(countBlock),
                                                                           lowBound=0, upBound=1)
        print(currentVaribleName + str(countProc))
        dictionaryVariableAndDeatilInfo[currentVaribleName + str(countBlock)] = megalist[i]
        countBlock += 1

# Створення списку з іменами всіх змінних
variableNameList = []
for i in dictionary.keys():
    variableNameList.append(i)

print("variableNameList " + str(len(variableNameList)))
print("variableNameList " + str(len(variableNameList)))
print("megalist " + str(len(megalist)))

# Вираження математичної моделі в коді:
# Функція мети
problem = pulp.LpProblem('Оптимізація', pulp.LpMinimize)
problem += lpSum(dictionary[variableNameList[j]] * megalist[j].price for j in range(len(megalist))), "Функция цели"

# Обеження кількості деталей в ПК
problem += lpSum(dictionary.get("Processors" + str(j)) for j in range(len(processorsList))) == 1
problem += lpSum(dictionary.get("RAM" + str(j)) for j in range(len(ramList))) == 1
problem += lpSum(dictionary.get("Plata" + str(j)) for j in range(len(motherboardList))) == 1
problem += lpSum(dictionary.get("Videocard" + str(j)) for j in range(len(videocardsList))) == 1
problem += lpSum(dictionary.get("Disk" + str(j)) for j in range(len(storageList))) == 1
problem += lpSum(dictionary.get("Block" + str(j)) for j in range(len(powerSupplyList))) == 1

# Користувацькі обмеження

# Розмір оперативної пам'яті
problem += lpSum(dictionary.get("RAM" + str(j)) * int(dictionaryVariableAndDeatilInfo.get("RAM" + str(j)).size) for j in
                 range(len(ramList))) >= 4.0, "2"

# Тактова частота процесора
problem += lpSum(dictionary.get("Processors" + str(j)) * int(
    dictionaryVariableAndDeatilInfo.get("Processors" + str(j)).clock_frequency) for j in
                 range(len(processorsList))) >= 2

# Блок живлення
problem += 1.2*(
        lpSum(dictionary.get("Processors" + str(j)) * int(dictionaryVariableAndDeatilInfo.get("Processors" + str(j)).power_usage) for j in range(len(processorsList)))
                +
                lpSum(dictionary.get("Videocard" + str(j)) * int(dictionaryVariableAndDeatilInfo.get("Videocard" + str(j)).powerUsage) for j in range(len(videocardsList)))
                ) \
           <= \
           lpSum(dictionary.get("Block" + str(j)) * int(dictionaryVariableAndDeatilInfo.get("Block" + str(j)).power) for j in range(len(powerSupplyList)))

problem.solve()

print("Результат:")
for variable in problem.variables():
    if variable.varValue == 1:
        print(dictionaryVariableAndDeatilInfo[variable.name])
        print(variable.name + " " + str(variable.varValue))

print("Прибыль:")
print(value(problem.objective))
print(problem.name)
