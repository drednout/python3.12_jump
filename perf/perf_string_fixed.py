def string_concat_fast(n):
    s_list = []
    for _ in range(n):
        s_list.append("test")
    return "".join(s_list)


if __name__ == "__main__":
    string_concat_fast(100000000)
