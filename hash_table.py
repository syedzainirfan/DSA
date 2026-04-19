table= [[],[],[],[],[],[],[],[],[],[]]  # --> Create empty list

def get_value(value):  # --> convert name into ord number
    total=0 # --> for add the ord values in variable
    for x in value:
        total+=ord(x)
    return total%10

def assign_index(name): # --> After get number assign it in list index
    index=get_value(name)
    table[index].append(name)

def for_finding(name): # --> to check a name consist in list or not
    index=get_value(name)
    return table[index]==name

# objects
assign_index("zain")
assign_index("hassan")
assign_index("rafay")
assign_index("ali")
assign_index("mudassir")
assign_index("umer")
assign_index("fahad")
print(table)

