import time

def play_the_game(list_of_number,number_of_round=2020):
    dict_indice={}
    rounds=1
    for n in list_of_number:
        dict_indice[n]=list()
        dict_indice[n].append(rounds)    
        rounds+=1
    last_spoken=list_of_number[-1]
    while rounds <= number_of_round:
        last_spoken_number=last_spoken
        indices=dict_indice.get(last_spoken_number,-1)
        if indices!=-1:
            indices=indices[-2:]
            if len(indices)>0:
                spoken=indices[-1]-indices[0]
            else:
                spoken=0
            if len(indices)>=2:
                dict_indice[last_spoken_number]=indices            
        else:
            dict_indice[last_spoken_number]=list()
            spoken=0
        
       # print(f"round n°{rounds} - number {last_spoken_number} - {spoken=}")
        if not spoken in dict_indice:
            dict_indice[spoken]=list()
        dict_indice[spoken].append(rounds)
        last_spoken=spoken
        rounds+=1
    return last_spoken

def prepare_the_game(input,number_of_round=2020):
    list_of_number=[int(x) for x in input.split(",")]
    print(list_of_number)
    return play_the_game(list_of_number,number_of_round)

import time

start= time.time()
assert 436 == prepare_the_game("0,3,6")
assert 1 == prepare_the_game("1,3,2")
assert 10 == prepare_the_game("2,1,3")
assert 27 == prepare_the_game("1,2,3")
assert 78 == prepare_the_game("2,3,1")
assert 438 == prepare_the_game("3,2,1")
assert 1836 == prepare_the_game("3,1,2")
end= time.time()
print(f"tests took {end-start}sec to complete")


start= time.time()
assert 175594 == prepare_the_game("0,3,6",30000000)
assert 2578 == prepare_the_game("1,3,2",30000000)
assert 3544142 == prepare_the_game("2,1,3",30000000)
assert 261214 == prepare_the_game("1,2,3",30000000)
assert 6895259 == prepare_the_game("2,3,1",30000000)
assert 18 == prepare_the_game("3,2,1",30000000)
assert 362 == prepare_the_game("3,1,2",30000000)
end= time.time()
print(f"tests took {end-start}sec to complete")

input="1,20,8,12,0,14"
part1= prepare_the_game(input,False)
print(part1)
assert part1==492
part2= prepare_the_game(input,False,30000000)
print(part2)