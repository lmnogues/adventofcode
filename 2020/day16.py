import common
from collections import Counter

def is_value_valid(rules,value):
    for rule in rules.values():
        for rr in rule:
            if  rr[0] <= value <= rr[1]:
                return True
    return False

def return_list_valid_rules(rules,value):
    rule_names=set()
    for rulename,rule in rules.items():
        for rr in rule:
            if  rr[0] <= value <= rr[1]:
                rule_names.add(rulename)
    return list(rule_names)

def parse_rule(rules):
    list_rules=dict()
    for r in rules:
        rr=r.split(":")
        rule_name=rr[0].strip()
        rule_ranges=rr[1].split(" or ")
        list_rules[rule_name]=list()
        for rule_range in rule_ranges:
            min_range=int(rule_range.split("-")[0].strip())
            max_range=int(rule_range.split("-")[1].strip())
            list_rules[rule_name].append((min_range,max_range))
    return list_rules

def parse_input(inputs):
    group=inputs.split("\n\n")
    rules=group[0].splitlines()
    rules=parse_rule(rules)
    your_ticket=[int(x) for x in group[1].splitlines()[1].split(",")]
    nearby_tickets=group[2].splitlines()[1:]
    for i,t in enumerate(nearby_tickets):
        nearby_tickets[i]=[int(x) for x in t.split(",")]
    # print(rules,your_ticket,nearby_tickets)
    return rules,your_ticket,nearby_tickets

def calculate_error_rate(tickets,rules):
    total=0
    ticket_to_remove=list()
    for t in tickets:
        for v in t:
            if not is_value_valid(rules,v):
                total+=v
                ticket_to_remove.append(t)
    return total,ticket_to_remove

def assign_category(categorized_data):
    sorted_per_len = {k: v for k, v in sorted(categorized_data.items(), key=lambda item: len(item[1]))}
    for k,v in sorted_per_len.items():
        if len(v) ==1:
            print(v)
            for c in categorized_data.values():
                if len(c)>1 and v[0] in c:
                    c.remove(v[0])
    if any([len(v) for v in categorized_data.values() if len(v)> 1]):
        categorized_data=assign_category(categorized_data)
    return categorized_data

def categorize_data(rules,nearby_ticket,your_ticket):
    categorized_data={}
    for idx in range(len(your_ticket)):
        list_rules=list()
        for ticket in nearby_ticket:
            list_rules = list_rules + return_list_valid_rules(rules,ticket[idx])            
        counter=Counter(list_rules)
        rule = [x[0] for x in counter.items() if x[1]==len(nearby_ticket)]
        if len(rule)==1:
            rules.pop(rule[0])
        categorized_data[idx]=rule
    print(categorized_data)
    categorized_data_cleaned = assign_category(categorized_data)
    your_ticket_dict={}
    for i,v in enumerate(your_ticket):
        your_ticket_dict[categorized_data_cleaned[i][0]]=v
        print(f"{categorized_data_cleaned[i]} : {v}")
    return your_ticket_dict




def test():
    inputs="""class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""
    rules,your_ticket,nearby_ticket = parse_input(inputs)
    assert False == is_value_valid(rules,4)
    assert False == is_value_valid(rules,55)
    assert False == is_value_valid(rules,12)
    total,ticket_to_remove = calculate_error_rate(nearby_ticket,rules)
    assert 71 == total
    nearby_ticket = [item for item in nearby_ticket if item not in ticket_to_remove]

def test2():
    inputs="""class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9"""
    rules,your_ticket,nearby_ticket = parse_input(inputs)
    
    _ ,ticket_to_remove = calculate_error_rate(nearby_ticket,rules)
    
    nearby_ticket = [item for item in nearby_ticket if item not in ticket_to_remove]
    categorize_data(rules,nearby_ticket,your_ticket)


def main():
    inputs=common.get_data_from_file("day16.txt")
    rules,your_ticket,nearby_ticket = parse_input(inputs)
    calculate_error_rate(nearby_ticket,rules)
    total,ticket_to_remove = calculate_error_rate(nearby_ticket,rules)
    assert 29851 == total
    print(len(nearby_ticket))
    nearby_ticket = [item for item in nearby_ticket if item not in ticket_to_remove]
    print(len(nearby_ticket))
    yourt_cket = categorize_data(rules,nearby_ticket,your_ticket)
    result =1
    print(yourt_cket)
    for r,v in yourt_cket.items() :
        if r.startswith("departure"):
            result*=v
    print(result)


test()
test2()
main()