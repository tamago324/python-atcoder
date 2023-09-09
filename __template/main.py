import sys

# region


class _Reader:
    # String
    def readString(self) -> str:
        return input()

    def readListString(self) -> list[str]:
        return self.readString().split()

    def readNLinesString(self, n: int) -> list[str]:
        return [self.readString() for _ in range(n)]

    def readGridString(self, n: int) -> list[list[str]]:
        return [list(self.readString()) for _ in range(n)]

    # Int
    def readInt(self) -> int:
        return int(self.readString())

    def readListInt(self) -> list[int]:
        return [int(x) for x in self.readListString()]

    def readNLinesInt(self, n: int) -> list[int]:
        return [int(self.readString()) for _ in range(n)]

    def readGridInt(self, n: int) -> list[list[int]]:
        return [self.readListInt() for _ in range(n)]

    def readColumnsInt(self, m: int, n: int = 2) -> list[list[int]]:
        result = [list() for _ in range(n)]
        for _ in range(m):
            row = [int(x) for x in self.readListString()]
            for i in range(n):
                result[i].append(row[i])
        return result


# endregion


def main(rd: _Reader):
    pass


# region

if __name__ == "__main__":
    if "--debug" in sys.argv:
        sample_number = sys.argv[sys.argv.index("--debug") + 1]
        input_file_path = f"./tests/sample-{sample_number}.in"

        # 標準入力をファイルから読み込む
        sys.stdin = open(input_file_path, "r")

    main(_Reader())

# endregion