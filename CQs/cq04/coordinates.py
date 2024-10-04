"""cq04 - coordinates."""

__author__ = "730744691"


def get_coords(xs: str, ys: str) -> None:
    y_idx: int = 0
    x_idx: int = 0
    while x_idx < len(xs):
        while y_idx < len(ys):
            print("(" + xs[x_idx] + "," + ys[y_idx] + ")")
            y_idx = y_idx + 1
        x_idx = x_idx + 1
        y_idx = 0


if __name__ == "__main__":
    print(get_coords("1234", "123"))
