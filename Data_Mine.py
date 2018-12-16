import secrets, sys, time, os, Clear, WordCore

gene_pool = ["A", "T", "C", "G"]
length_range = 0
temp_gene = ''
sequence = []
sequence2 = []
run_num = 0
global_gene_pool = []
global_gene_pool_desc = []

def gene_length():
    global length_range
    length_range = secrets.choice(range(8, 64)) #pairs of 2

def gene_selection():
    global gene_pool
    global temp_gene
    global sequence
    global sequence2
    rand = secrets.randbelow(len(gene_pool))
    if str(temp_gene) == "G":
        sequence2.append("C")
        temp_gene = ''
    elif str(temp_gene) == "C":
        sequence2.append("G")
        temp_gene = ''
    elif str(temp_gene) == "A":
        sequence2.append("T")
        temp_gene = ''
    elif str(temp_gene) == "T":
        sequence2.append("A")
        temp_gene = ''
    else:
        temp_gene = gene_pool[rand]
        sequence.append(str(gene_pool[rand]))

def spinning_cursor():
    while True:
        for cursor in 'ATGC':
            yield cursor

def cursor():
    spinner = spinning_cursor()
    for _ in range(5):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')

def gene_check2():
    gene_lib = ["ATAAT", "GACCAGA", "AT", "AG"]
    gene_dict = ["Caxic", "Guanadine", "Feriox", "Durrix"]
    tempc = 0
    seq = ''
    seq2 = ''
    for x in range(len(sequence)):
        seq += sequence[x]
        seq += sequence2[x]
    for i in range(0, len(gene_lib)):
        if str(gene_lib[i]) in str(seq):
            print("Match | " + str(gene_lib[i]) + " | " + str(gene_dict[i]) + " | in primary sequence")
            tempc += 1
            time.sleep(0.5)
        else:
            print("No Match | " + str(gene_lib[i]) + " | " + str(gene_dict[i]) + " | in primary sequence")
            time.sleep(0.5)
    tempc = 0
    for u in range(0, len(gene_lib)):
        if str(gene_lib[u]) in str(seq2):
            print("Match | " + str(gene_lib[u]) + " | " + str(gene_dict[u]) + " | in secondary sequence")
            tempc += 1
            time.sleep(0.5)
        else:
            print("No Match | " + str(gene_lib[u]) + " | " + str(gene_dict[i]) + " | in secondary sequence")
            time.sleep(0.5)

def gene_mix():
    global length_range
    print("Euclid\n")
    print("Kepler\n")
    print("Khanid\n")
    print("Qasmer\n")
    strand_complexity = str(input("What is your preferred complexity: "))
    if strand_complexity == "Euclid":
        length_range = secrets.choice(range(8, 16))
        print("Selection: Euclid")
    elif strand_complexity == "Kepler":
        length_range = secrets.choice(range(16, 32))
        print("Selection: Kepler")
    elif strand_complexity == "Khanid":
        length_range = secrets.choice(range(32, 64))
        print("Selection: Khanid")
    elif strand_complexity == "Qasmer":
        length_range = secrets.choice(range(64, 128))
    else:
        Clear.clear()
        gene_mix()
     
def test_run():
    val = 0
    gene_mix()
    for q in range(length_range * 2):
        gene_selection()
    #sequence.pop()
    print(sequence)
    print(sequence2)
    #if len(sequence) != len(sequence2):
    #    print("Error in length")
        #return
    for w in range(0, len(sequence2)):
        for x in range(1):
            cursor()
        if val == 0:
            print(sequence[w], end='')
            val = 1
        elif val == 1:
            print(sequence2[w-1], end='')
            val = 0
        else:
            print("Err")
            break
        global run_num
        if run_num == 0:
            print("-^-^-", end='')
            run_num += 1
        else:
            run_num = 0
            print("")
            print(" |   | ")
    print(" ^   ^ ")
    print("* * * *")
    gene_check2()

test_run()

#update to give DNA or to make a library of singular points, such as random A/T/G/C Variance