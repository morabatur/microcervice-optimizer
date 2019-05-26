class Videocard():
    TYPE_DETAIL = "Videocard"

    def __init__(self, name, graphicsCoreFrequency, videoMemory_Size,
                 memoryBusCapacity, videoMemoryOperatingFrequency, powerUsage, price):
        self.name = name
        self.graphicsCoreFrequency = graphicsCoreFrequency
        self.videoMemory_Size = videoMemory_Size
        self.memoryBusCapacity = memoryBusCapacity
        self.videoMemoryOperatingFrequency = videoMemoryOperatingFrequency
        self.powerUsage = powerUsage
        self.price = price

    def __str__(self):
        return "\"videocard\": " \
               "{\"name\": \"%s\", " \
               "\"graphicsCoreFrequency\": %s, " \
               "\"videoMemory_Size\": %s, " \
               "\"memoryBusCapacity\": %s, " \
               "\"videoMemoryOperatingFrequency\": %s, " \
               "\"powerUsage\": %s, " \
               "\"price\": %s" \
               " }" \
               % (self.name, self.graphicsCoreFrequency,
                  self.videoMemory_Size,
                  self.memoryBusCapacity,
                  self.videoMemoryOperatingFrequency,
                  self.powerUsage,
                  self.price)
