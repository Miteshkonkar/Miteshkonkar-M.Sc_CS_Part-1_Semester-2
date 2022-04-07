# Converting Left Linear Grammer to Right Linear Grammer



def get_transitions(rules):

    my_dict = res = dict()
    ld = r = str()

    for i in rules:
        if i[0] not in my_dict:
            my_dict[i[0]] = []
        try:
            my_dict[i[0]].append([i[1][1], i[1][0]])
        except IndexError:
            continue
        print(my_dict)
    
    for sub in my_dict:
        for rule in my_dict[sub]:
            if isinstance(rule, list):
                if sub not in res:
                    res[sub] = []
                res[sub].append(ld.join([str(ele) for ele in rule]))
    
    print("Left Linear grammer is:")
    for item in res:
        for rhs in res[item]:
            if isinstance(rhs, str):
                print(r, item, "->", rhs)


if __name__ == "__main__":
    rule_count = int(input("Enter rule count>\t"))
    rules = []

    for i in range(rule_count):
        rules.append(input("Enter right linear grammer" + str(i + 1) + ">\t"))
    
    rules = [i.split("->") for i in rules]
    get_transitions(rules)