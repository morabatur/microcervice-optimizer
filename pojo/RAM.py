class RAM():
    TYPE_DETAIL = "RAM"

    def __init__(self, name, types, price, size, frequency):
        self.name = name
        self.size = size
        self.price = price
        self.types = types
        self.frequency = frequency

    def __str__(self):
        return "\"ram\": " \
               "{\"name\": \"%s\", " \
               "\"types\": \"%s\", " \
               "\"price\": %s, " \
               "\"size\": %s, " \
               "\"frequency\": %s" \
               " }" \
               % (self.name, self.types,
                  self.price,
                  self.size,
                  self.frequency,
                  )