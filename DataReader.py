import re
import csv
import os.path


class Commons:
    def __init__(self, filename: str):
        self.start_flag = bool()
        self.data_path = r'.\Data\\'
        self.type_txt = r'.txt'
        self.filename = filename

        # Parameters csv_write related
        self.type_csv = r'.csv'
        self.file_path = self._do_file_path
        self.csv_file_path = self._do_csv_file_path

        # Parameters related to split_string
        # self.line = str()

        # Parameters related to time_adapter
        self.start = int()
        self.stop = int()
        self.my_list = list()

        # Table of contents
        self.rows = list()

    @property
    def _do_file_path(self) -> str:
        return self.data_path + self.filename + self.type_txt

    @property
    def _do_csv_file_path(self) -> str:
        return self.data_path + self.filename + self.type_csv

    @staticmethod
    def csv_write(self):
        if not os.path.isfile(
                self.csv_file_path
        ):
            f = open(
                self.csv_file_path,
                'w'
            )
            with f:
                writer = csv.writer(f)
                for row in self.rows:
                    writer.writerow(row)

    @staticmethod
    def _time_adapter(start_iterator: int, stop_iterator: int, line: list):
        new_list = []
        for time in range(start_iterator, stop_iterator):
            new = [str(time)]
            new.extend(line)
            new_list.append(new)
        return new_list

    def _accumulate_generator_time(self, line: list, start_iterator: int):
        new_list = []
        if self.start_flag:
            stop_iterator = int(line[0]) + start_iterator  # include last item
            new_list.append(
                self._time_adapter(start_iterator, stop_iterator, line)
            )
        else:
            pass
        return new_list

    @staticmethod
    def _split_string(line: str):
        return re.findall(r'\S+', line)


class GeneratorLog(Commons):
    def __init__(self, filename: str):
        super(GeneratorLog, self).__init__(filename)
        self.filename = filename
        self.file_path = super(GeneratorLog, self)._do_file_path
        self.csv_file_path = super(GeneratorLog, self)._do_csv_file_path
        self.start_flag = False
        self.place_holder = "0"
        # Monitoring file substitutions and contents check dictionaries
        self.substitutions = {
            " ms": " ",
            ":-> ": " to:",
            ":  <- ": " from:",
            "\n": "",
        }

        self.monitor = {

            "start": "ms:-> on",
            "stop": "End:",
            "marker_off": "to:gen:att",
            "generate": "to:start",
            "frq_marker": "to:gen:frq"
        }

        # first, initial line
        self.initial_line = [["0", "0", "initiate", "0", "0"]]
        # header
        self.header = [["gen_time_ms", "time_accu", "command", "value", "monitor_id"]]

    def csv_write(self):
        super(GeneratorLog, self).csv_write(self)

    def read_generator_log(self):
        try:
            with open(self.file_path, mode='r', encoding='utf-8') as file:
                content_list = []
                start_iterator = None
                content_flag = False
                # Counter is used to create an unique line ID
                counter = 0
                for line in file:

                    if line == '\n':
                        content_flag = True
                        continue

                    if line.startswith('-'):
                        continue

                    if line.startswith(self.monitor["stop"]):
                        continue
                    if content_flag:
                        line_data_list = self._split_string(
                            self._substitute_in_generator_log(line.lower())
                        )

                        if len(line_data_list) < 3:
                            line_data_list.append(self.place_holder)

                        if self.monitor["start"] in line \
                                and not self.start_flag:
                            content_list.extend(self.initial_line)
                            self.start_flag = True

                        if len(content_list) > 0:
                            start_iterator = int(content_list[-1][0]) + 1

                        if self.start_flag:
                            counter += 1
                            line_data_list.extend([str(counter)])
                            some_list = self._accumulate_generator_time(line_data_list, start_iterator)
                            if len(content_list) == 0:
                                content_list.append(some_list)
                            else:
                                content_list.extend(some_list[0])
                self.rows = self.header
                self.rows.extend(content_list)
                self.start_flag = False
                return self.rows
        except FileNotFoundError:
            print(f'File not found')
        except PermissionError:
            print("Permission denied")
        except IndexError:
            print("Index Error")

    def _substitute_in_generator_log(self, line: str):
        regex = re.compile("(%s)" % "|".join(map(re.escape, self.substitutions.keys())))
        return regex.sub(
            lambda mo: self.substitutions[mo.string[mo.start():mo.end()]], line)


class ActToolLog(Commons):
    def __init__(self, filename: str):
        super(ActToolLog, self).__init__(filename)
        self.filename = filename
        self.file_path = super(ActToolLog, self)._do_file_path
        self.csv_file_path = super(ActToolLog, self)._do_csv_file_path
        self.start_flag = False
        self.act_tool = {
            "start": "time",
            "stop": "*"
        }
        self.header = ['act_time_ms']
        self.header_ending = ['act_tool_id']

    def csv_write(self):
        super(ActToolLog, self).csv_write(self)

    def read_act_tool_log(self):

        try:
            with open(self.file_path, mode='r', encoding='utf-8') as file:
                content_list = []
                counter = 0
                for line in file:
                    if line.startswith(self.act_tool["stop"]):
                        continue
                    if line.startswith(self.act_tool["start"]):
                        self.header.extend(
                            self._split_string(line)[:3]
                        )
                        self.header.extend(self.header_ending)
                        content_list.append(self.header)
                        self.start_flag = True
                        continue
                    if self.start_flag:
                        counter += 1
                        row = self._split_string(line.lower())[:3]
                        row.extend([counter])

                        # from s to ms
                        stop_iterator = float(row[0]) * 1000
                        stop_iterator = int(stop_iterator)
                        if stop_iterator < 1:
                            content_list.extend(
                                self._time_adapter(stop_iterator, stop_iterator + 1, row)
                            )

                        else:
                            start_iterator = int(content_list[-1][0])
                            content_list.extend(
                                self._time_adapter(start_iterator + 1, stop_iterator + 1, row)
                            )
                self.rows = content_list
                self.start_flag = False
                return self.rows

        except FileNotFoundError:
            print("File do not exist")
        except PermissionError:
            print("Permission denied")



# Test use

# DATA_PATH = r'.\Data\\'
# ACT_TOOL_LOG = r'Test_results'
# GENERATOR_LOG = r'Monitor'
# FILE_TYPE = r'.txt'


# # FILENAME = r'.\Data\Test_results.txt'
# FILENAME = DATA_PATH + ACT_TOOL_LOG + FILE_TYPE
# # FILEGEN = r'.\Data\Monitor.txt'
# FILEGEN = DATA_PATH + GENERATOR_LOG + FILE_TYPE
#

# uu = readfile(FILENAME)
#
# print(len(uu))
#
# for r in uu:
#     print([u for u in r])

# aa = ActToolLog("Test_results")
# bb = aa.read_act_tool_log()
#
# print(len(bb))
#
# for r in bb:
#     print([u for u in r])
#
# aa.csv_write()



rr = GeneratorLog("Monitor_20181114_1348_4T_PS")
qaaa = rr.read_generator_log()
# rr.csv_write()
#
# print(len(qaaa))
#
# for t in qaaa:
#     print([u for u in t])
#
# rr.csv_write()
