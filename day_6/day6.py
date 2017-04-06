def main():
    t = int(input())
    strings = [input() for x in range(t)]

    for s in strings:
        e = [s[x] for x in range(len(s)) if x % 2 == 0]
        e = "".join(e)
        o = [s[x] for x in range(len(s)) if x % 2 != 0]
        o = "".join(o)
        print("%s %s"%(e, o))

if __name__ == '__main__':
    main()
