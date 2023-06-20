import json
from sys import argv

def read_txt(file):
    return [float(x) for x in file.read().split()]

def find_avg(num_list):
    return round(sum(num_list)/len(num_list),2)

result = dict()

with open("case_study/results/python.txt","r") as p, \
        open("case_study/results/c.txt","r") as c, \
        open("case_study/results/java.txt","r") as j:
    
    data_p = read_txt(p)
    avg_p = find_avg(data_p)
    result["python"] = {"val":data_p, 'avg': avg_p}

    data_c = read_txt(c)
    avg_c = find_avg(data_c)
    result["c"] = {"val":data_c, 'avg': avg_c}

    data_j = read_txt(j)
    avg_j = find_avg(data_j)
    result["java"] = {"val":data_j, 'avg': avg_j}


n = int(argv[1])
no_of_iter = int(argv[2])

print(
f'''
Test Details:
Matrix Size: {n} x {n}
Number of Iterations: {no_of_iter}\n
Average Runtime
Python: {avg_p}
C: {avg_c}
Java: {avg_j}
'''
)

with open('case_study/results/findings.json', 'w') as fp:
    json.dump(result, fp)