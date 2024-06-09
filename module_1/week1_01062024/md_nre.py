def md_nre(y = 50, y_hat = 49.5, n = 2, p = 1):
    print((y**(1/n) - y_hat**(1/n))**p)

if __name__ == "__main__":
    md_nre()