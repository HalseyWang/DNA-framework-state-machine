import random
import sys
import textwrap


def main():
    if invalidarguments():
        return

    dnaDict = genseq(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
    dnaList = ToList(dnaDict)
    pattern = flist("pattern.txt")
    numseqf(dnaDict, "SN_seq.txt")
    seqf(dnaList, "seq.txt")
    print(pattern)
    filterseq("seq.txt", "no_library-screening_seq.txt", pattern)


def isinarray(array, line):
    for item in array:
        if item in line:
            return True
    return False


def filterseq(IFPath, OFPath, darry):
    with open(IFPath, "r", encoding="utf-8") as f:
        with open(OFPath, 'w', encoding='UTF-8') as filterf:
            for line in f.readlines():
                if not isinarray(darry, line):
                    filterf.write(line)


def split_lines(datastr):
    return datastr.split('\n')


def flist(fpath):
    with open(fpath, "r", encoding="utf-8") as f:
        text = f.read()
#        print(text)
#        text = text.replace("TTTT", "").replace("AAAA", "")
        patternlist = split_lines(text)
        return patternlist


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


def gendna(base):
    return {
        0: 'A',
        1: 'C',
        2: 'G',
        3: 'T'
    }[base]


if __name__ == "__main__":
    main()
