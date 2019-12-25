
from typing import List, NamedTuple, Tuple, Iterable, Set, Dict, Callable
from enum import Enum
import itertools
from collections import deque, defaultdict
import logging
import copy


program = [3,62,1001,62,11,10,109,2221,105,1,0,703,635,744,781,1191,913,1024,1451,1125,1928,1703,2190,1220,1575,944,1769,1996,672,1352,1800,983,1965,1321,1160,2027,812,571,1249,2157,1061,2126,1414,1868,1484,1835,884,1635,1604,2097,1383,604,1517,1670,1096,2062,1897,1546,853,1280,1734,0,0,0,0,0,0,0,0,0,0,0,0,3,64,1008,64,-1,62,1006,62,88,1006,61,170,1105,1,73,3,65,20101,0,64,1,20101,0,66,2,21102,105,1,0,1106,0,436,1201,1,-1,64,1007,64,0,62,1005,62,73,7,64,67,62,1006,62,73,1002,64,2,133,1,133,68,133,102,1,0,62,1001,133,1,140,8,0,65,63,2,63,62,62,1005,62,73,1002,64,2,161,1,161,68,161,1101,1,0,0,1001,161,1,169,101,0,65,0,1102,1,1,61,1102,1,0,63,7,63,67,62,1006,62,203,1002,63,2,194,1,68,194,194,1006,0,73,1001,63,1,63,1106,0,178,21102,1,210,0,106,0,69,1202,1,1,70,1101,0,0,63,7,63,71,62,1006,62,250,1002,63,2,234,1,72,234,234,4,0,101,1,234,240,4,0,4,70,1001,63,1,63,1106,0,218,1105,1,73,109,4,21102,1,0,-3,21101,0,0,-2,20207,-2,67,-1,1206,-1,293,1202,-2,2,283,101,1,283,283,1,68,283,283,22001,0,-3,-3,21201,-2,1,-2,1106,0,263,21201,-3,0,-3,109,-4,2106,0,0,109,4,21101,0,1,-3,21101,0,0,-2,20207,-2,67,-1,1206,-1,342,1202,-2,2,332,101,1,332,332,1,68,332,332,22002,0,-3,-3,21201,-2,1,-2,1106,0,312,21202,-3,1,-3,109,-4,2106,0,0,109,1,101,1,68,359,20102,1,0,1,101,3,68,366,21001,0,0,2,21101,376,0,0,1105,1,436,21202,1,1,0,109,-1,2106,0,0,1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576,2097152,4194304,8388608,16777216,33554432,67108864,134217728,268435456,536870912,1073741824,2147483648,4294967296,8589934592,17179869184,34359738368,68719476736,137438953472,274877906944,549755813888,1099511627776,2199023255552,4398046511104,8796093022208,17592186044416,35184372088832,70368744177664,140737488355328,281474976710656,562949953421312,1125899906842624,109,8,21202,-6,10,-5,22207,-7,-5,-5,1205,-5,521,21102,1,0,-4,21101,0,0,-3,21102,51,1,-2,21201,-2,-1,-2,1201,-2,385,470,21002,0,1,-1,21202,-3,2,-3,22207,-7,-1,-5,1205,-5,496,21201,-3,1,-3,22102,-1,-1,-5,22201,-7,-5,-7,22207,-3,-6,-5,1205,-5,515,22102,-1,-6,-5,22201,-3,-5,-3,22201,-1,-4,-4,1205,-2,461,1105,1,547,21101,-1,0,-4,21202,-6,-1,-6,21207,-7,0,-5,1205,-5,547,22201,-7,-6,-7,21201,-4,1,-4,1105,1,529,22102,1,-4,-7,109,-8,2105,1,0,109,1,101,1,68,563,21001,0,0,0,109,-1,2106,0,0,1102,1,20593,66,1101,2,0,67,1102,598,1,68,1102,302,1,69,1102,1,1,71,1102,602,1,72,1105,1,73,0,0,0,0,2,268791,1101,85361,0,66,1102,1,1,67,1101,631,0,68,1102,1,556,69,1101,0,1,71,1102,1,633,72,1106,0,73,1,1151,49,80363,1102,1,99277,66,1101,0,4,67,1102,662,1,68,1101,302,0,69,1102,1,1,71,1102,670,1,72,1106,0,73,0,0,0,0,0,0,0,0,48,166638,1101,92297,0,66,1102,1,1,67,1101,0,699,68,1102,556,1,69,1101,0,1,71,1101,0,701,72,1105,1,73,1,117,36,311061,1101,0,90173,66,1101,0,1,67,1101,730,0,68,1101,556,0,69,1102,1,6,71,1102,1,732,72,1106,0,73,1,28429,42,65381,29,27793,29,55586,8,89783,8,179566,8,269349,1102,89597,1,66,1101,0,4,67,1101,0,771,68,1102,302,1,69,1102,1,1,71,1101,779,0,72,1106,0,73,0,0,0,0,0,0,0,0,42,130762,1101,61283,0,66,1102,1,1,67,1101,808,0,68,1101,556,0,69,1102,1,1,71,1101,810,0,72,1106,0,73,1,32,26,20593,1102,41081,1,66,1101,0,1,67,1102,839,1,68,1101,556,0,69,1101,0,6,71,1102,1,841,72,1106,0,73,1,1,49,160726,36,103687,7,101902,31,193852,44,126194,19,146613,1102,1,31177,66,1101,0,1,67,1101,880,0,68,1102,1,556,69,1101,0,1,71,1101,882,0,72,1106,0,73,1,-16,49,241089,1102,1,51071,66,1102,1,1,67,1101,911,0,68,1101,0,556,69,1101,0,0,71,1102,1,913,72,1105,1,73,1,1137,1101,96763,0,66,1101,0,1,67,1101,0,940,68,1102,1,556,69,1101,1,0,71,1101,0,942,72,1105,1,73,1,349,19,48871,1102,101267,1,66,1102,1,1,67,1101,0,971,68,1101,0,556,69,1102,5,1,71,1102,973,1,72,1105,1,73,1,2,20,175948,31,48463,2,89597,48,27773,48,55546,1101,0,43987,66,1101,6,0,67,1101,1010,0,68,1102,302,1,69,1101,0,1,71,1102,1022,1,72,1106,0,73,0,0,0,0,0,0,0,0,0,0,0,0,9,2998,1101,0,33359,66,1102,4,1,67,1102,1,1051,68,1101,253,0,69,1102,1,1,71,1101,0,1059,72,1105,1,73,0,0,0,0,0,0,0,0,26,41186,1102,27793,1,66,1101,3,0,67,1102,1088,1,68,1101,0,302,69,1101,0,1,71,1102,1,1094,72,1106,0,73,0,0,0,0,0,0,9,5996,1101,16693,0,66,1101,1,0,67,1102,1123,1,68,1102,556,1,69,1102,0,1,71,1101,1125,0,72,1105,1,73,1,1553,1101,89783,0,66,1102,3,1,67,1101,1152,0,68,1102,1,302,69,1101,0,1,71,1102,1158,1,72,1106,0,73,0,0,0,0,0,0,9,4497,1102,100493,1,66,1101,1,0,67,1102,1187,1,68,1101,0,556,69,1101,1,0,71,1102,1189,1,72,1106,0,73,1,3,31,96926,1102,1,95569,66,1101,1,0,67,1101,1218,0,68,1101,556,0,69,1101,0,0,71,1101,0,1220,72,1105,1,73,1,1638,1102,13477,1,66,1101,0,1,67,1102,1247,1,68,1101,0,556,69,1101,0,0,71,1102,1249,1,72,1106,0,73,1,1295,1102,1,21893,66,1101,0,1,67,1101,0,1276,68,1101,0,556,69,1101,0,1,71,1101,0,1278,72,1105,1,73,1,10007,7,50951,1102,27773,1,66,1101,6,0,67,1101,1307,0,68,1101,0,302,69,1101,0,1,71,1101,0,1319,72,1106,0,73,0,0,0,0,0,0,0,0,0,0,0,0,34,103706,1101,73883,0,66,1101,0,1,67,1101,0,1348,68,1101,0,556,69,1102,1,1,71,1101,0,1350,72,1105,1,73,1,4441,44,63097,1102,103967,1,66,1102,1,1,67,1101,1379,0,68,1102,556,1,69,1102,1,1,71,1102,1381,1,72,1105,1,73,1,359,36,207374,1102,71353,1,66,1101,0,1,67,1101,1410,0,68,1102,556,1,69,1102,1,1,71,1102,1,1412,72,1106,0,73,1,256,20,263922,1102,1,48463,66,1101,0,4,67,1101,1441,0,68,1101,302,0,69,1101,0,1,71,1102,1449,1,72,1105,1,73,0,0,0,0,0,0,0,0,6,33359,1101,50951,0,66,1101,0,2,67,1102,1478,1,68,1101,302,0,69,1102,1,1,71,1102,1482,1,72,1105,1,73,0,0,0,0,31,145389,1102,35591,1,66,1101,1,0,67,1102,1,1511,68,1101,556,0,69,1102,1,2,71,1102,1513,1,72,1105,1,73,1,7,20,131961,2,358388,1102,1,42491,66,1102,1,1,67,1102,1,1544,68,1101,556,0,69,1101,0,0,71,1102,1,1546,72,1106,0,73,1,1462,1102,1,15073,66,1101,0,1,67,1101,0,1573,68,1101,0,556,69,1101,0,0,71,1101,0,1575,72,1105,1,73,1,1971,1102,17891,1,66,1102,1,1,67,1101,1602,0,68,1101,0,556,69,1101,0,0,71,1102,1604,1,72,1105,1,73,1,1581,1102,1,18089,66,1102,1,1,67,1102,1,1631,68,1102,1,556,69,1101,1,0,71,1102,1633,1,72,1106,0,73,1,1319,20,219935,1101,0,103687,66,1102,1,3,67,1102,1662,1,68,1101,0,302,69,1102,1,1,71,1102,1668,1,72,1105,1,73,0,0,0,0,0,0,6,133436,1101,65381,0,66,1102,1,2,67,1102,1,1697,68,1101,302,0,69,1102,1,1,71,1102,1701,1,72,1105,1,73,0,0,0,0,9,1499,1102,1,97499,66,1101,0,1,67,1102,1,1730,68,1101,0,556,69,1102,1,1,71,1101,1732,0,72,1106,0,73,1,125,1,198554,1102,80363,1,66,1101,0,3,67,1102,1,1761,68,1102,302,1,69,1102,1,1,71,1101,1767,0,72,1105,1,73,0,0,0,0,0,0,6,66718,1101,6661,0,66,1102,1,1,67,1101,0,1796,68,1102,556,1,69,1102,1,1,71,1101,0,1798,72,1106,0,73,1,160,48,138865,1102,48871,1,66,1101,3,0,67,1101,0,1827,68,1101,302,0,69,1102,1,1,71,1101,0,1833,72,1105,1,73,0,0,0,0,0,0,29,83379,1101,0,51853,66,1101,2,0,67,1102,1,1862,68,1101,0,351,69,1101,0,1,71,1101,0,1866,72,1106,0,73,0,0,0,0,255,90173,1102,1,9283,66,1101,0,1,67,1102,1895,1,68,1102,1,556,69,1101,0,0,71,1101,1897,0,72,1106,0,73,1,1671,1101,0,57163,66,1102,1,1,67,1101,1924,0,68,1101,0,556,69,1101,0,1,71,1101,0,1926,72,1106,0,73,1,-168,19,97742,1102,1,1499,66,1101,0,4,67,1102,1,1955,68,1102,1,253,69,1101,0,1,71,1102,1,1963,72,1106,0,73,0,0,0,0,0,0,0,0,34,51853,1102,1,90469,66,1102,1,1,67,1101,1992,0,68,1101,0,556,69,1101,1,0,71,1101,0,1994,72,1106,0,73,1,30,44,189291,1102,277,1,66,1101,1,0,67,1101,2023,0,68,1101,0,556,69,1102,1,1,71,1102,1,2025,72,1106,0,73,1,971,20,43987,1102,78497,1,66,1101,1,0,67,1102,1,2054,68,1101,0,556,69,1101,0,3,71,1102,2056,1,72,1106,0,73,1,5,1,99277,1,297831,48,83319,1102,63097,1,66,1101,0,3,67,1101,2089,0,68,1102,1,302,69,1102,1,1,71,1102,1,2095,72,1105,1,73,0,0,0,0,0,0,6,100077,1101,0,26371,66,1101,1,0,67,1102,1,2124,68,1101,0,556,69,1101,0,0,71,1102,1,2126,72,1105,1,73,1,1351,1102,3557,1,66,1102,1,1,67,1101,2153,0,68,1102,1,556,69,1101,1,0,71,1102,1,2155,72,1106,0,73,1,19,2,179194,1102,52561,1,66,1102,1,1,67,1102,1,2184,68,1101,556,0,69,1101,0,2,71,1101,0,2186,72,1106,0,73,1,10,1,397108,48,111092,1102,1,9181,66,1101,1,0,67,1102,2217,1,68,1101,556,0,69,1102,1,1,71,1101,0,2219,72,1105,1,73,1,-349,20,87974]

logging.basicConfig(level=logging.INFO)


class Opcode(Enum):
    ADD = 1
    MULTIPLY = 2
    STORE_INPUT = 3
    SEND_TO_OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    ADJUST_RELATIVE_BASE = 9

    END_PROGRAM = 99


Modes = List[int]
Program = List[int]


class EndProgram(Exception): pass


def parse_opcode(opcode: int, num_modes: int = 3) -> Tuple[Opcode, Modes]:
    # logging.debug(f"parsing {opcode}")

    opcode_part = opcode % 100

    modes: List[int] = []
    opcode = opcode // 100

    for _ in range(num_modes):
        modes.append(opcode % 10)
        opcode = opcode // 10

    return Opcode(opcode_part), modes


class IntcodeComputer:
    def __init__(self, program: List[int], get_input: Callable[[], int]) -> None:
        self.program = defaultdict(int)
        self.program.update({i: value for i, value in enumerate(program)})
        self.get_input = get_input
        self.pos = 0
        self.relative_base = 0
        self.minus_ones = 0

    def save(self):
        return [
            copy.deepcopy(self.program),
            self.get_input,
            self.pos,
            self.relative_base
        ]

    @staticmethod
    def load(program, get_input, pos, relative_base):
        computer = IntcodeComputer([], get_input)
        computer.program = program
        computer.pos = pos
        computer.relative_base = relative_base
        return computer

    def _get_value(self, pos: int, mode: int) -> int:
        if mode == 0:
            # pointer mode
            # logging.debug(f"pos: {pos}, mode: {mode}, value: {self.program[self.program[pos]]}")
            return self.program[self.program[pos]]
        elif mode == 1:
            # immediate mode
            # logging.debug(f"pos: {pos}, mode: {mode}, value: {self.program[pos]}")
            return self.program[pos]
        elif mode == 2:
            # relative mode
            # logging.debug(f"pos: {pos}, mode: {mode}, value: {self.program[self.program[pos] + self.relative_base]}")
            return self.program[self.program[pos] + self.relative_base]
        else:
            raise ValueError(f"unknown mode: {mode}")

    def _loc(self, pos: int, mode: int) -> int:
        if mode == 0:
            # pointer mode
            # logging.debug(f"pos: {pos}, mode: {mode}, value: {self.program[pos]}")
            return self.program[pos]
        elif mode == 2:
            # relative mode
            # logging.debug(f"pos: {pos}, mode: {mode}, value: {self.program[pos] + self.relative_base}")
            return self.program[pos] + self.relative_base

    def go(self) -> int:

        while True:
            # logging.debug(f"program: {self.program}")
            # logging.debug(f"pos: {self.pos}, inputs: {self.inputs}, relative_base: {self.relative_base}")

            opcode, modes = parse_opcode(self.program[self.pos])

            # logging.debug(f"opcode: {opcode}, modes: {modes}")

            if opcode == Opcode.END_PROGRAM:
                raise EndProgram

            elif opcode == Opcode.ADD:
                value1 = self._get_value(self.pos + 1, modes[0])
                value2 = self._get_value(self.pos + 2, modes[1])
                loc = self._loc(self.pos + 3, modes[2])

                # logging.debug(f"value1: {value1}, value2: {value2}, loc: {loc}")

                self.program[loc] = value1 + value2
                self.pos += 4

            elif opcode == Opcode.MULTIPLY:
                value1 = self._get_value(self.pos + 1, modes[0])
                value2 = self._get_value(self.pos + 2, modes[1])
                loc = self._loc(self.pos + 3, modes[2])

                # logging.debug(f"value1: {value1}, value2: {value2}, loc: {loc}")

                self.program[loc] = value1 * value2
                self.pos += 4

            elif opcode == Opcode.STORE_INPUT:
                # Get input and store at location
                loc = self._loc(self.pos + 1, modes[0])
                input_value = self.get_input()

                self.program[loc] = input_value
                self.pos += 2
                
                if input_value == -1:
                    self.minus_ones += 1

                if self.minus_ones >= 10:
                    self.minus_ones = 0
                    raise NoInput

            elif opcode == Opcode.SEND_TO_OUTPUT:
                # Get output from location
                value = self._get_value(self.pos + 1, modes[0])
                self.pos += 2
                # logging.debug(f"output: {value}")

                ####
                ####

                return value

            elif opcode == Opcode.JUMP_IF_TRUE:
                # jump if true
                value1 = self._get_value(self.pos + 1, modes[0])
                value2 = self._get_value(self.pos + 2, modes[1])

                # logging.debug(f"value1: {value1}, value2: {value2}")

                if value1 != 0:
                    self.pos = value2
                else:
                    self.pos += 3

            elif opcode == Opcode.JUMP_IF_FALSE:
                value1 = self._get_value(self.pos + 1, modes[0])
                value2 = self._get_value(self.pos + 2, modes[1])

                # logging.debug(f"value1: {value1}, value2: {value2}")

                if value1 == 0:
                    self.pos = value2
                else:
                    self.pos += 3

            elif opcode == Opcode.LESS_THAN:
                value1 = self._get_value(self.pos + 1, modes[0])
                value2 = self._get_value(self.pos + 2, modes[1])
                loc = self._loc(self.pos + 3, modes[2])

                # logging.debug(f"value1: {value1}, value2: {value2}, loc: {loc}")

                if value1 < value2:
                    self.program[loc] = 1
                else:
                    self.program[loc] = 0
                self.pos += 4

            elif opcode == Opcode.EQUALS:
                value1 = self._get_value(self.pos + 1, modes[0])
                value2 = self._get_value(self.pos + 2, modes[1])
                loc = self._loc(self.pos + 3, modes[2])

                # logging.debug(f"value1: {value1}, value2: {value2}, loc: {loc}")

                if value1 == value2:
                    self.program[loc] = 1
                else:
                    self.program[loc] = 0
                self.pos += 4

            elif opcode == Opcode.ADJUST_RELATIVE_BASE:
                value = self._get_value(self.pos + 1, modes[0])

                # logging.debug(f"value: {value}")

                self.relative_base += value
                self.pos += 2

            else:
                raise ValueError(f"invalid opcode: {opcode}")

N = 50
queues = [deque() for _ in range(N)]
output_queues = [deque() for _ in range(N)]

class NoInput(Exception): pass


def get_input(q: deque, i: int):
    started = False

    def _get_input():
        nonlocal started

        if not started:
            started = True
            #print("q", i, i)
            return i
        elif q:
            #print("q", i, q[0])
            return q.popleft()
        else:
            #print("q", i, -1)
            return -1
    return _get_input

computers = [IntcodeComputer(program, get_input(q, i)) 
             for i, q in enumerate(queues)]

nat = None
idles = set()
delivered = set()

while True:
    if len(idles) == 50:
        queues[0].extend(nat)
        x, y = nat
        if y in delivered:
            print("y", y)
            break
        delivered.add(y)
        idles.clear()

    for i, (computer, output_q) in enumerate(zip(computers, output_queues)):
        print("i", i)
        try:
            output_q.append(computer.go())
            idles.clear()
        except NoInput:
            idles.add(i)
        print(output_q)

        if len(output_q) == 3:
            address = output_q.popleft()
            x = output_q.popleft()
            y = output_q.popleft()

            print(address, x, y)

            if address == 255:
                nat = (x, y)
            else:
                queues[address].append(x)
                queues[address].append(y)

