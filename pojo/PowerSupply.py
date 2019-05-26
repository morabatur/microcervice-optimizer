class PowerSupply():
    TYPE_DETAIL = "Block"

    def __init__(self, name, power, price):
        self.name = name
        self.power = power
        self.price = price

    def __str__(self):
        return "\"power_supply\": " \
               "{\"name\": \"%s\"," \
               "\"power\": %s, " \
               "\"price\": %s" \
               " }" \
               % (self.name, self.power,
                  self.price
                  )
