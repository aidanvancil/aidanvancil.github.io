# -*- coding: utf-8 -*-
"""
@author: aidan
"""

def parse_values(lines):
    temp_num = ""
    temp_name = ""
    temp_ranking = {"Names":[], "Marks":[]}
    for line in lines:
        for i in line:
            if i == ' ' or i == '\n':
                continue
            if ord(i) <= 57 and ord(i) >= 48:
                temp_num += i
            elif i.isalpha():
                temp_name += i
        temp_ranking["Names"].append(temp_name)
        temp_ranking["Marks"].append(temp_num)
        temp_name = ""
        temp_num = ""
    return temp_ranking
    
def assign_ranks(ranking):
    counter = 0
    past_marking = 0
    master_ranks = []
    sub_str = ""
    while len(ranking["Marks"]) > 0:
        marking = max(ranking["Marks"])
        indexing = ranking["Marks"].index(marking)
        if marking != past_marking:
            counter += 1
        sub_str = str(counter) + '\t' + ranking["Names"][indexing] + '\t\t' + ranking["Marks"][indexing] + '\n'
        master_ranks.append(sub_str)
        ranking["Marks"].pop(indexing)
        ranking["Names"].pop(indexing)
        past_marking = marking
    return master_ranks

def open_file(textfile: str) -> list:
    file = open(textfile, "r") 
    lines = file.readlines()
    file.close()
    ranking = parse_values(lines)
    master_ranks = assign_ranks(ranking)
    print(master_ranks)
    buffer = ""
    for i in master_ranks:
        buffer += i
    print(buffer)
    return master_ranks

            

    
    
    
open_file("StudentData.txt")
