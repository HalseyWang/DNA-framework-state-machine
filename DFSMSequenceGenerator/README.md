# DNA sequence generator for DFSM
Generation filter for random DNA sequences. The output is unfiltered TXT and filtered CSV formatted files containing sequences and their headers. These sequences are divided into a series of 300-character lines by specification. The title of the sequence can be customized. It can generate any number of fixed-length DNA sequences if you need it. The resulting sequences are used for programmable assembly of DFSM. It has been experimentally verified and is reliable.

## Input
>python main<span></span>.py \<seqnum> \<seqlengthstart> \<seqlengthend>

## Example
A small example of generating a random DNA sequence with a sequence length of 60.

### Example Input
>python main<span></span>.py 1 60 60

### Filter Pattern
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
             
### Example Output
#### unfiltered sequence
GAGAATCCTCCGCGTTCTTGGGGAAATTCTACATGTTCCCCCAGTTCGACAAGCGAGGGC

