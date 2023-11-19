def string_concat(n):
    s = ""
    for _ in range(n):
        s += "test"
    return s


if __name__ == "__main__":
    string_concat(100000000)
