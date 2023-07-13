def main():
    pattern = filst("input.txt")
    print(pattern)
    filterseq("no_library-screening_seq.txt", "library-screening_seq", pattern)


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


def filst(fpath):
    with open(fpath, "r", encoding="utf-8") as f:
        text = f.read()
#        print(text)
#        text = text.replace("TTTT", "").replace("AAAA", "")
        data = split_lines(text)
        return data


if __name__ == "__main__":
    main()
