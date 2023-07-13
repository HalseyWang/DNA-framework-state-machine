darry = ["TTTT",
         "AAAA",
         "CCCC",
         "GGGG",
         "GCGCGC",
         "CGCGCG",
         "ATATAT",
         "TATATA",
         "GAGAGA",
         "GTGTGT",
         "AGAGAG",
         "TGTGTG",
         "CACACA",
         "ACACAC",
         "CTCTCT",
         "TCTCTC"
         ]


def isinarray(array, line):
    for item in array:
        if item in line:
            return True
    return False


with open("sequence.txt", "r", encoding="utf-8") as f:
    with open("filter.txt", 'w', encoding='UTF-8') as g:
        for line in f.readlines():
            if not isinarray(darry, line):
                g.write(line)
