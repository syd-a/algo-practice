def lcs(x, y):
    seq_dict = {}
    for i in range(1 + len(x)):
        key = (x[0:i], "")
        seq_dict[key] = ""
    for j in range(1 + len(y)):
        key = ("", y[0:j])
        seq_dict[key] = ""

    for i in range(1, 1 + len(x)):
        for j in range(1, 1 + len(y)):
            key_x = x[0:i]
            key_y = y[0:j]
            key = (key_x, key_y)
            end_key_x = key_x[-1]
            end_key_y = key_y[-1]

            val_discard_x = seq_dict[(x[0:(i - 1)], y[0:j])]
            val_discard_y = seq_dict[(x[0:i], y[0:(j - 1)])]
            val_match = end_key_x if (end_key_x == end_key_y) else ""
            val_diag = seq_dict[(x[0:(i - 1)], y[0:(j - 1)])] + val_match

            val = None
            if (len(val_discard_x) >= len(val_discard_y)) and ((len(val_discard_x)) >= len(val_diag)):
                val = val_discard_x
            elif (len(val_discard_y) >= len(val_discard_x)) and ((len(val_discard_y)) >= len(val_diag)):
                val = val_discard_y
            elif (len(val_diag) >= len(val_discard_x)) and (len(val_diag) >= len(val_discard_y)):
                val = val_diag
            seq_dict[key] = val

    return seq_dict[x, y]

if __name__ == "__main__":
    x = "AGGTAB"
    y = "GXTXAYB"
    common_subseq = lcs(x, y)
    expected_subseq = "GTAB"
    print(f"calculated: {common_subseq}")
    print(f"expected: {expected_subseq}")
