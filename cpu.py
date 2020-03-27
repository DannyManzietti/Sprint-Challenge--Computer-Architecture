import sys


HLT = 0b00000001
LDI = 0b10000010
PRN = 0b01000111
ADD = 0b10100000
SUB = 0b10100001
MUL = 0b10100010
DIV = 0b10100011
AND = 0b10101000
CMP = 0b10100111
DEC = 0b01100110
INC = 0b01100101
MOD = 0b10100100
NOT = 0b01101001
OR = 0b10101010
SHL = 0b10101100
SHR = 0b10101101
XOR = 0b10101011
PUSH = 0b01000101
POP = 0b01000110
CALL = 0b01010000
RET = 0b00010001
ST = 0b10000100
JMP = 0b01010100
JEQ = 0b01010101
JGE = 0b01011010
JGT = 0b01010111
JLE = 0b01011001
JLT = 0b01011000
JNE = 0b01010110
LD = 0b10000011
NOP = 0b00000000
PRA = 0b01001000
INT = 0b01010010
IRET = 0b00010011


class CPU:
    def __init__(self):
        # memory
        self.ram = [0] * 256
        # reg
        self.reg = [0] * 8
        # reset stack pointer at R7
        self.reg[7] = 0xF4
        # internal registers:
        # program counter
        self.pc = 0
        # flag
        self.fl = 0
        # branch table
        self.branchtable = {
            HLT: self.HLT,
            LDI: self.LDI,
            PRN: self.PRN,
            ADD: self.alu,
            SUB: self.alu,
            MUL: self.alu,
            DIV: self.alu,
            AND: self.alu,
            CMP: self.alu,
            DEC: self.alu,
            INC: self.alu,
            MOD: self.alu,
            NOT: self.alu,
            OR: self.alu,
            SHL: self.alu,
            SHR: self.alu,
            XOR: self.alu,
            PUSH: self.PUSH,
            POP: self.POP,
            CALL: self.CALL,
            RET: self.RET,
            ST: self.ST,
            JMP: self.JMP,
            JEQ: self.JEQ,
            JGE: self.JGE,
            JGT: self.JGT,
            JLE: self.JLE,
            JLT: self.JLT,
            JNE: self.JNE,
            LD: self.LD,
            NOP: self.NOP,
            PRA: self.PRA,
            INT: self.INT,
            IRET: self.IRET,
        }

    def load(self):
        # load program into memory

        # check for filename arg
        if len(sys.argv) != 2:
            print("ERROR: include filename")
            sys.exit(1)

            address = 0
