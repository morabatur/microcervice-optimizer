class Processors():
    TYPE_DETAIL = "Processors"

    def __init__(self, name, clock_frequency, capacity, cache_memory, core, price, power_usage):
        self.name = name
        self.clock_frequency = clock_frequency
        self.capacity = capacity
        self.cache_memory = cache_memory
        self.core = core
        self.price = price
        self.power_usage = power_usage

    def __str__(self):
        return "\"processor\": " \
               "{\"name\": \"%s\", " \
               "\"clock_frequency\": %s, " \
               "\"capacity\": %s, " \
               "\"cache_memory\": %s, " \
               "\"core\": %s, " \
               "\"price\": %s, " \
               "\"power_usage\": %s" \
               " }" \
               % (self.name, self.clock_frequency,
                  self.capacity,
                  self.cache_memory,
                  self.core,
                  self.price,
                  self.power_usage
                  )
