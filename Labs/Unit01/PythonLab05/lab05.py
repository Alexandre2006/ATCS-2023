def print_sum(number_path="data/numbers.txt"):
    with open(number_path, "r") as file:
        lines = file.readlines()
        sum = 0
        for line in lines:
            try:
                num = int(line)
                sum += num
            except ValueError:
                print("Invalid number: " + line)
        print("Sum: " + str(sum))

def calculate_costs(purchase_path="data/raw_purchases.txt", cost_path="data/costs.txt", out_path="costs_out.txt"):
    # Get purchases
    purchases = {}
    with open(purchase_path, "r") as purchaseFile:
        for line in purchaseFile.readlines():
            items = line.split(" ")
            number = int(items.pop(0))
            purchases[number] = map(lambda x:x.strip(), items)
            
    # Get item costs
    with open(cost_path, "r") as costFile:
        costs = {}
        for line in costFile.readlines():
            split_line = line.split(" ")
            cost = float(split_line.pop().strip())
            item = split_line.pop()
            costs[item] = cost
    
    # Calculate costs per number line
    totals = {}
    for i in purchases.keys():
        total = 0
        for item in purchases[i]:
            total += costs[item.strip()]
        totals[i] = total
    
    # Write to file
    with open(out_path, "w") as outFile:
        outFile.writelines(map(lambda key:str(key) + " " + str(totals[key]) + "\n", totals.keys()))

def rna_to_aa(rna_path="data/rna.txt", aa_path="data/codons.txt", out_path="rna_out.txt"):
    # Load RNA
    rna = ""
    with open(rna_path, "r") as rnaFile:
        rna = rnaFile.readline()
    
    # Load Codons
    rna_to_aa_map = {}
    with open(aa_path, "r") as aaFile:
        lines = aaFile.readlines()
        for line in lines:
            split_line = line.split(" ")
            value = split_line.pop(0)
            for key in split_line:
                rna_to_aa_map[key.strip()] = value
    
    # Convert to Amino Acids
    with open(out_path, "w") as outFile:     
        index = rna.index("AUG")
        while index < len(rna) and rna[index:index+3] != "UAG":
            try:
                outFile.write(rna_to_aa_map[rna[index:index+3]])
            except:
                pass
            index += 3

if __name__ == "__main__":
    while True:
        print("""
1. Print Sum
2. Calculate Costs
3. RNA to AA
Q. Quit
""")
        selection = input("Enter a selection: ")
        if selection == "1":
            print_sum()
        elif selection == "2":
            calculate_costs()
        elif selection == "3":
            rna_to_aa()
        elif selection.lower() == "q":
            break