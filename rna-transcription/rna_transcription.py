
# * `G` -> `C`
# * `C` -> `G`
# * `T` -> `A`
# * `A` -> `U`

def to_rna( dna_strand ):

    result = " "

    string = list( dna_strand )
    
    for c in string:
        if c == "G":
            result += "C" 

        if c == "C":
            result += "G" 

        if c == "T":
            result += "A" 

        if c == "A":
            result += "U"

    return result.strip()

