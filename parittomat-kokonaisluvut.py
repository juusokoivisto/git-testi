def main():
    parittomat = []
    i = 0
    while len(parittomat) < 29:
        i += 1
        if i % 2 != 0:
            parittomat.append(i)

    print(parittomat)

if __name__ == "__main__":
    main()