def read_fasta(fp):
    name, seq = None, []
    for line in fp:
        line = line.rstrip()
        if line.startswith(">"):
            if name: yield (name, ''.join(seq))
            name, seq = line, []
        else:
            seq.append(line)
    if name: yield (name, ''.join(seq))

def fasta_array(file_name):
    array = []
    with open(file_name) as fp:
        for name, seq in read_fasta(fp):
            array.append([name, seq])
    return array

def fp_divide(x, y):
    return float(x) / float(y)

def unique(l):
    return list(set(l))

def most_common_element(l):
    table = {}
    unique_elements = unique(l)
    for k in range(0,len(unique_elements)):
        table[unique_elements[k]] = 0

    for i in range(0, len(l)):
        table[l[i]] += 1

    most_common = "N"
    max = 0
    for j in range(0, len(unique_elements)):
        if table[unique_elements[j]] > max:
            most_common = unique_elements[j]
            max = table[unique_elements[j]]

    return most_common

def insert_newlines(string, every=60):
    lines = []
    for i in range(0, len(string), every):
        lines.append(string[i:i+every])
    return '\n'.join(lines)

def begining_string_match(small, big):
    if len(small) > len(big):
        return False
    for i in range(0, len(small)):
        if small[i] != big[i]:
            return False
    return True

def percent_identity(small, big):
    total = 0
    for i in range(0, len(small)):
        if small[i] == big[i]:
            total += 1
    return fp_divide(total, len(small) - small.count("N") - big.count("N"))

def max_percent_identity(small, big):
    pi_list = []
    while len(big) >= len(small):
        pi_list.append(percent_identity(small, big))
        big = big[1:]
    return max(pi_list)