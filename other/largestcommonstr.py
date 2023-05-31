def lcs(x, y):
    m = [[0] * (1 + len(y)) for _ in range(1 + len(x))]
    longest, x_pos = 0, 0
    for x_idx in range(1, 1 + len(x)):
        for y_idx in range(1, 1 + len(y)):
            if x[x_idx - 1] == y[y_idx - 1]:
                m[x_idx][y_idx] = m[x_idx - 1][y_idx - 1] + 1
                if m[x_idx][y_idx] > longest:
                    longest = m[x_idx][y_idx]
                    x_pos = x_idx
            else:
                m[x_idx][y_idx] = 0
    print(x[x_pos - longest: x_pos])

if __name__ == "__main__":
    str1 = "Привет подписчикам канала Class Python"
    str2 = "Class Python - лучший канал о программировании"
    lcs(str1, str2)
