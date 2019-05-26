from pojo.Processors import Processors
from pojo.Videocard import Videocard
from pojo.RAM import RAM
from pojo.Storage import Storage
from pojo.PowerSupply import PowerSupply
from pojo.Motherboard import Motherboard


class DetailParser:

    def __init__(self, data):
        self.data = data

    # Need data['videocardsList']
    def parsVideocard(self):
        videocardsList = []
        for videocard in self.data['videocardsList']:
            videocardsList.append(
                Videocard(videocard['name'], videocard['graphicsCoreFrequency'], videocard['videoMemory_Size'],
                          videocard['memoryBusCapacity'], videocard['videoMemoryOperatingFrequency'],
                          videocard['powerUsage'],
                          videocard['price']))
        return videocardsList

    # Need data['motherboardList']
    def parsMotherBoard(self):
        motherboardList = []
        for board in self.data['motherboardList']:
            motherboardList.append(
                Motherboard(board['name'], board['formFactor'], board['ramSlots'], board['price']))
        return motherboardList

    # Need data['motherboardList']
    def parsPowerSupply(self):
        powerSupplyList = []
        for power in self.data['powerSupplyList']:
            powerSupplyList.append(
                PowerSupply(power['name'], power['power'], power['price']))
        return powerSupplyList

    def parsProcessor(self):
        processorsList = []
        for proc in self.data['processorsList']:
            processorsList.append(Processors(proc['name'], proc['clockFrequency'],
                                             proc['capacity'], proc['cacheMemory'],
                                             proc['core'], proc['price'], proc['powerUsage']))
        return processorsList

    def parsRam(self):
        ramList = []
        for ram in self.data['ramList']:
            ramList.append(
                RAM(ram['name'], ram['type'], ram['price'], ram['size'], ram['frequency']))
        return ramList

    def parsStorage(self):
        storageList = []
        for stor in self.data['storageList']:
            storageList.append(Storage(stor['name'], stor['powerUsage'], stor['price'], stor['type'], stor['size']))
        return storageList
