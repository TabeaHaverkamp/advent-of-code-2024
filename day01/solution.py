
with open('input.txt', 'r') as file:
    lines = [line.strip().split("   ") for line in file]
    lines1 = [int(l[0]) for l in lines]
    lines2 = [int(l[1]) for l in lines]
        

def distance(lines1, lines2):
    lines1= sorted(lines1) 
    lines2 = sorted(lines2)
    print(lines1)
    print(lines2)
    dist = 0
    for idx, _ in enumerate(lines1):
        a = abs(lines1[idx]-lines2[idx])
        dist += a
    print('---')
    print(dist)

distance(lines1, lines2)

def similarity(lines1, lines2):
    sim = 0
    for i in lines1:
        cnt =lines2.count(i)
        sim += i *cnt
    print('----')
    print(sim)
        
similarity(lines1, lines2)