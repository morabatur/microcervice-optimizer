class Storage():
    TYPE_DETAIL = "Disk"

    def __init__(self, name, power_usage, price, size, types):
        self.name = name
        self.power_usage = power_usage
        self.price = price
        self.size = size
        self.types = types

    def __str__(self):
        return "\"storage\": " \
               "{\"name\": \"%s\", " \
               "\"power_usage\": %s, " \
               "\"price\": %s, " \
               "\"types\": \"%s\", " \
               "\"size\": %s" \
               " }" \
               % (self.name, self.power_usage,
                  self.price,
                  self.size,
                  self.types,
                  )
