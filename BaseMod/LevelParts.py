from RWESharp.Modify import LevelPart
import numpy as np


stack_pos = [1, 2, 11, 3, 4, 5, 6, 7, 9, 10, 12, 13, 19, 21, 20, 18]


class GeoLevelPart(LevelPart):
    def __init__(self, level):
        super().__init__("geo", level)
        self.blocks = np.zeros((*level.level_size.toTuple(), 3), np.uint8)
        self.stack = np.zeros((*level.level_size.toTuple(), 3), np.uint16)

        # loading level
        self.load_level()

    def load_level(self):
        dat = self.level.data["GE"]
        with np.nditer(self.blocks, flags=['multi_index'], op_flags=['writeonly']) as it:
            for x in it:
                x[...] = dat[it.multi_index[0]][it.multi_index[1]][it.multi_index[2]][0]
        with np.nditer(self.stack, flags=['multi_index'], op_flags=['writeonly']) as it:
            for x in it:
                x[...] = self.stack2byte(dat[it.multi_index[0]][it.multi_index[1]][it.multi_index[2]][1])

        #print("new")
        #print(np.asarray(dat, np.int8))

    @staticmethod
    def stack2byte(stack) -> np.int16:
        b = np.uint16()
        for i in stack:
            b |= 1 << stack_pos.index(i)
        return b

    @staticmethod
    def byte2stack(b) -> list:
        stack = []
        for i in range(16):
            if b & 1 << i > 0:
                stack.append(stack_pos[i])
        return stack
