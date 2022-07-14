from unittest import result


with open('alexa_top_10k.txt', 'r') as r:
    results = set()
    for line in r:
            results.add(line.strip("\n").split(",")[1].removeprefix("www.").split(".")[0])
    print(len(results))