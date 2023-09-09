import sys

# region


class _Reader:
    # String
    def read_string(self) -> str:
        return input()

    def read_list_string(self) -> list[str]:
        return self.read_string().split()

    def read_n_lines_string(self, n: int) -> list[str]:
        return [self.read_string() for _ in range(n)]

    def read_grid_string(self, n: int) -> list[list[str]]:
        return [list(self.read_string()) for _ in range(n)]

    # Int
    def read_int(self) -> int:
        return int(self.read_string())

    def read_list_int(self) -> list[int]:
        return [int(x) for x in self.read_list_string()]

    def read_n_lines_int(self, n: int) -> list[int]:
        return [int(self.read_string()) for _ in range(n)]

    def read_grid_int(self, n: int) -> list[list[int]]:
        return [self.read_list_int() for _ in range(n)]

    def read_columns_int(self, m: int, n: int = 2) -> list[list[int]]:
        result = [list() for _ in range(n)]
        for _ in range(m):
            row = [int(x) for x in self.read_list_string()]
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
