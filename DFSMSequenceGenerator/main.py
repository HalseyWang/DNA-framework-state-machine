import random
import sys
import textwrap


def main():
    if invalidarguments():
        return

    dnaDict = genseq(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
    dnaList = ToList(dnaDict)
    numseqf(dnaDict, "SN_seq.txt")
    seqf(dnaList, "seq.txt")
    filterseq("seq.txt", "SCR_sequence.csv")


def filterseq(IFPath, OFPath):
    pattern = ["TTTT",
             "AAAA",
             "CCCC",
             "GGGG",
             "GCGCGC",
             "CGCGCG",
             "ATATATA",
             "TATATAT",
             "GAGAGAG",
             "AGAGAGA",
             "GTGTGTG",
             "TGTGTGT",
             "CACACAC",
             "ACACACA",
             "CTCTCTC",
             "TCTCTCT,"
             "TGGATCCA",
             "ACCTAGGT",
             "GTTCGAAC",
             "CAAGCTTG",
             "GGGGGCCCCC",
             "CCCCCGGGGG",
             "AAAAATTTTT",
             "TTTTTAAAAA",
             "AATTGCAATT",
             "GGCCATGGCC",
             ]
    with open(IFPath, "r", encoding="utf-8") as f:
        with open(OFPath, 'w', encoding='UTF-8') as filterf:
            for line in f.readlines():
                if not isinarray(pattern, line):
                    filterf.write(line)


def ToList(Dict):
    dnaList = list(dict.values(Dict))
    return dnaList


def invalidarguments():
    if len(sys.argv) != 4:
        print("Invalid argument length: <seqNumber> <seqLengthStart> <seqLengthEnd>")
        return True

    try:
        int(sys.argv[1])
        int(sys.argv[2])
        int(sys.argv[3])
    except ValueError:
        print("Invalid argument type: <int> <int> <int>")
        return True

    return False


def numseqf(dict, fpath):
    with open(fpath, "w") as f:
        for key, vlue in dict.items():
            f.write(key)
            f.write('\n')
            f.write('\n'.join(textwrap.wrap(vlue, 300)))
            f.write('\n')


def seqf(data, fpath):
    f = open(fpath, "w")
    for line in data:
        f.write(line + '\n')
    f.close()


def genseq(seq, lenstart, lenend):
    dnaDict = {

    }
    for i in range(seq):
        dnaseq = ""
        for _ in range(random.randint(lenstart, lenend)):
            dnaseq += gendna(random.randint(0, 3))
        dnanum = str(i + 1) + " "
        dnaDict[dnanum] = dnaseq
    return dnaDict


def isinarray(array, line):
    for item in array:
        if item in line:
            return True
    return False


def gendna(base):
    return {
        0: 'A',
        1: 'C',
        2: 'G',
        3: 'T'
    }[base]


if __name__ == "__main__":
    main()
