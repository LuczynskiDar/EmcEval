

#Dictionary reference
# monitor = {
#     # "start": "to:start",
#     "start": "ms:-> on",
#     "stop": "End:",
#     "marker_off": "to:gen:att",
#     "generate": "to:start",
#     "frq_marker": "to:gen:frq"
# }


class FrequencyFinder:
    def __init__(self, generator: dict):
        self.frequency = False
        self.status = False
        self.generator = generator
        self.value = int

    def get_frequency_from_generator(self, content: str, value: int):
        if content in self.generator["frq_marker"]:
            self.refresh()
            self.frequency = True
            self.value = value
            return None
        elif content in self.generator["generate"]:
            if self.frequency:
                self.status = True
                return self.value
            else:
                return None
        elif content in self.generator["marker_off"]:
            if self.frequency and self.status:
                return self._clean()
            else:
                return None
        else:
            if self.status:
                return self.value
            else:
                return None

    def _clean(self):
        temp = self.value
        self.frequency = None
        self.status = False
        self.value = None
        return temp

    def refresh(self):
        self.frequency = None
        self.status = False
        self.value = None

    def _get_and_clean_value(self):
        temp = self.value
        self.value = None
        return temp

# Test use

# ff = FrequencyFinder(monitor)
#
# for t in  test_list:
#     print(t[0])
#     print(ff.get_frequency_from_generator(t[0], t[1]))
#     print(ff.frequency)
#     print(ff.value)
#     print(ff.status)

# test_list = \
#     [["initiate", 0],
#      ["to:on", 0],
#      ["to:gen:frq", 150000],
#      ["to:on", 0],
#      ["to:meas:channel", 1],
#      ["to:meas:frq", 150000],
#      # ["to:meas:trig", 0],
#      # ["from:rm,513;", 0],
#      # ["to:gen:att", 375],
#      # ["to:meas:trig", 0],
#      # ["from:rm,760;", 0],
#      # ["to:gen:att", 265],
#      # ["to:meas:trig", 0],
#      # ["from:rm,863;", 0],
#      # ["to:gen:att", 225],
#      # ["to:meas:trig", 0],
#      # ["from:rm,908;", 0],
#      # ["to:meas:trig", 0],
#      # ["from:rm,924;", 0],
#      # ["to:gen:att", 200],
#      ["to:meas:trig", 0],
#      ["from:rm,935;", 0],
#      ["to:gen:mod:prm:am", 80],
#      ["to:gen:mod:frq:am", 1000],
#      ["to:gen:time", 20],
#      ["to:start", 0],
#      ["from:rr,00;", 0],
#      ["to:gen:att", 260],
#      ["to:gen:mod:prm:am", 0],
#      ["to:gen:frq", 151500],
#      ["to:meas:frq", 151500],
#      ["to:gen:time", 20],
#      ["to:start", 0],
#      ["from:rr,00;", 0],
#      ["to:gen:att", 260],
#      ["to:gen:time", 20], ]
