class Motherboard():
    TYPE_DETAIL = "Motherboard"

    def __init__(self, name, form_factor, ram_slots, price):
        self.name = name
        self.form_factor = form_factor
        self.ram_slots = ram_slots
        self.price = price

    def __str__(self):
        return "\"motherboard\": " \
               "{\"name\": \"%s\", " \
               "\"form_factor\": \"%s\", " \
               "\"ram_slots\": %s, " \
               "\"price\": %s" \
               " }" \
               % (self.name, self.ram_slots,
                  self.ram_slots, self.price
                  )
