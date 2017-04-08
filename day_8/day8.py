def main():
    n = int(input())

    phone_book = {}

    inputs = [str(input()) for entry in range(n)]
    # inputs = ["rob 18181818", "tan 834874", "sop 3743847384"]

    for name in inputs:
        print("AQUI: %s"%name)
        pares = name.split(" ")
        phone_book[pares[0]] = pares[1]

    queries = []

    while True:

        # A simple hack to make test pass on HackerRank console
        try:
            query = input()
        except EOFError:
            break

        if query == "":
            break
        queries.append(query)

    if queries:
        for query in queries:
            if query in phone_book.keys():
                print("%s=%s"%(query, phone_book[query]))
            else:
                print("Not found")

if __name__ == '__main__':
    main()
