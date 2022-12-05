
import common
    
# data=common.get_data_from_site(year=2022,day=2)
rounds=common.get_inputs_from_site(year=2022,day=2)
split_rounds=[(y[0],y[1]) for y in [x.split(" ") for x in rounds]]
print(len(rounds))
print(len(split_rounds))

# A X : rock
# B Y : paper
# C Z : scisor

def score_round_V1(round):
    adversary=round[0]
    your=round[1]
    score=0

    if your=="X":
        score+=1
    if your=="Y":
        score+=2
    if your=="Z":
        score+=3

    if (your=="X" and adversary=="A") or (your=="Y" and adversary=="B") or (your=="Z" and adversary=="C"):
        #draw
        score+=3
    elif  (your=="X" and adversary=="C") or (your=="Y" and adversary=="A") or (your=="Z" and adversary=="B"):
        #victory
        score+=6
    # print(score)
    return score

# A : rock 1
# B : paper 2
# C : scisor 3

# X : loss
# Y : draw
# Z : win

def calc_value_draw(adversary):
    if adversary=="A":
        return 1
    if adversary=="B":
        return 2
    if adversary=="C":
        return 3

def calc_value_win(adversary):
    if adversary=="A":
        return 2
    if adversary=="B":
        return 3
    if adversary=="C":
        return 1

def calc_value_loss(adversary):
    if adversary=="A":
        return 3
    if adversary=="B":
        return 1
    if adversary=="C":
        return 2

def score_round_V2(round):
    
    adversary=round[0]
    your=round[1]
    score=0
    if your=="X":
        score+=calc_value_loss(adversary)
    if your=="Y":
        score+=3
        score+=calc_value_draw(adversary)
    if your=="Z":
        score+=6
        score+=calc_value_win(adversary)
   # print(round,score)
    return score

test_input=[('A', 'Y'),('B','X'),('C', 'Z')]

print(sum([score_round_V1(i) for i in test_input]))
print(sum([score_round_V1(i) for i in split_rounds]))
print(sum([score_round_V2(i) for i in test_input]))
print(sum([score_round_V2(i) for i in split_rounds]))