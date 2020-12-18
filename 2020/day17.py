import copy
from collections import OrderedDict

class Part1():
    def check_availability(self,x,y,z,cubes):
        list_cube={}
        for z_pos in [-1,0,1]:
            for x_pos in [-1,0,1]:
                    for y_pos in [-1,0,1]:
                        if not (x_pos==0 and y_pos==0 and z_pos==0):
                            xx=x+x_pos
                            yy=y+y_pos
                            zz=z+z_pos
                                                
                            try :                            
                                list_cube[(zz,yy,xx)]=cubes[zz][yy][xx]
                            except:
                                pass
        result= len([x for x in list_cube.values() if x=="#"])
        return result

    def new_plan(self,cubes):
        line_dict={}
        for y in cubes[0].keys():
            col_dict={}
            for x in cubes[0][0].keys():
                col_dict[x]='.'
            line_dict[y]=col_dict
        return line_dict
                
    def extend_neighboor(self,cubes):
        result_cube=copy.deepcopy(cubes)
        for z,plan in cubes.items():        
            for z_pos in [-1,0,1]:
                for y,line in plan.items():
                    for y_pos in [-1,0,1]:
                        for x,val in line.items():
                            for x_pos in [-1,0,1]:   
                                if not (x_pos==0 and y_pos==0 and z_pos==0):             
                                    xx=x+x_pos
                                    yy=y+y_pos
                                    zz=z+z_pos
                                    try:
                                        result_cube[zz]
                                    except:
                                        result_cube[zz]=self.new_plan(result_cube)
                                        
                                    try:
                                        result_cube[zz][yy]
                                    except:
                                        for _,pp in result_cube.items():
                                            col_dict={}
                                            for xxx in result_cube[0][0].keys():
                                                col_dict[xxx]='.'
                                            for zzz in result_cube.keys():
                                                result_cube[zzz][yy]=col_dict                                    
                                    
                                    try:
                                        result_cube[zz][yy][xx]
                                    except:                                
                                        for _,pp in result_cube.items():
                                            for ll in pp.values():
                                                ll[xx]='.'
        
        final_dict={}
        for z,plan in OrderedDict(sorted(result_cube.items())).items():   
            final_dict[z]={}
            for y,line in OrderedDict(sorted(plan.items())).items():            
                final_dict[z][y]={}
                for x,v in  OrderedDict(sorted(line.items())).items():                
                    final_dict[z][y][x]=v
        return final_dict

    def display(self,cubes):
        for z,plan in cubes.items():    
            print(f"for {z=}")     
            for y,line in plan.items():
                count=0
                for x,v in line.items():
                    count+=1
                    end=""
                    if count==len(line):
                        end="\n"
                    print(v, end =end)

    def boot_cube(self,cubes):
        
        result_cube=copy.deepcopy(cubes)
        
        print(f"==== INIT =====")
        self.display(cubes)
        for steps in range(1,7):
            cubes = self.extend_neighboor(cubes)
            print(f"==== round {steps} =====")
            result_cube=copy.deepcopy(cubes)
            active_side_cube=copy.deepcopy(cubes)
            for z,plan in cubes.items():   
                for y,line in plan.items():
                    for x,v in line.items():
                        new_v=v
                        availability = self.check_availability(x,y,z,cubes)
                        active_side_cube[z][y][x]=min(9,availability)
                        if v=="#":                        
                            if not availability in [2,3]:
                                #print(f"disabling cube at {z=}{y=}{x=}")
                                new_v="."
                        elif v==".":
                            if  availability ==3:
                                #print(f"enabling cube at {z=}{y=}{x=}")
                                new_v="#"
                        result_cube[z][y][x]=new_v          
            #display(active_side_cube)
            # display(result_cube)
            cubes=copy.deepcopy(result_cube)
        
        return cubes

    def answer(self,cubes):
        ans_part1=0
        for z in cubes.values():
            for y in z.values():
                for x in y.values():
                    if x=="#":
                        ans_part1+=1
        return ans_part1

    def parse_to_cube(self,inputs):
        
        cubes={}
        line_dict={}
        for x,line in enumerate(inputs.splitlines()):
            col_dict={}
            for y,v in enumerate(line):
                col_dict[y]=v
            line_dict[x]=col_dict
        cubes[0]=line_dict
        return cubes
class Part2():
    def check_availability(self,x,y,z,w,cubes):
        list_cube={}
        for w_pos in [-1,0,1]:
            for z_pos in [-1,0,1]:
                for x_pos in [-1,0,1]:
                        for y_pos in [-1,0,1]:
                            if not (x_pos==0 and y_pos==0 and z_pos==0 and w_pos==0):
                                xx=x+x_pos
                                yy=y+y_pos
                                zz=z+z_pos
                                ww=w+w_pos                
                                try :                            
                                    list_cube[(ww,zz,yy,xx)]=cubes[ww][zz][yy][xx]
                                except:
                                    pass
        result= len([x for x in list_cube.values() if x=="#"])
        return result

    def new_dim(self,cubes):
        plan_dict={}
        for z in cubes[0].keys():
            plan_dict[z]=self.new_plan(cubes)
        return plan_dict

    def new_plan(self,cubes):
        line_dict={}
        for y in cubes[0][0].keys():            
            line_dict[y]=self.new_line(cubes)
        return line_dict

    def new_line(self,cubes):
        col_dict={}
        for x in cubes[0][0][0].keys():
            col_dict[x]='.'
        return col_dict

    def extend_neighboor(self,cubes):
        result_cube=copy.deepcopy(cubes)
        for w,dim in cubes.items():
            for w_pos in [0,-1,1]:
                for z,plan in dim.items():        
                    for z_pos in [0,-1,1]:
                        for y,line in plan.items():
                            for y_pos in [0,-1,1]:
                                for x,val in line.items():
                                    for x_pos in [0,-1,1]:   
                                        if not (x_pos==0 and y_pos==0 and z_pos==0 and w_pos ==0):             
                                            xx=x+x_pos
                                            yy=y+y_pos
                                            zz=z+z_pos
                                            ww=w+w_pos    
                                            try:
                                                result_cube[ww] 
                                            except:
                                                result_cube[ww]=self.new_dim(result_cube)

                                            try:
                                                result_cube[ww][zz]
                                            except:
                                                result_cube[ww][zz]=self.new_plan(result_cube)
                                                
                                            try:
                                                result_cube[ww][zz][yy]
                                            except:
                                                result_cube[ww][zz][yy]=self.new_line(result_cube)

                                            try:
                                                result_cube[ww][zz][yy][xx]
                                            except:    
                                                # inesert enw value on each line              
                                                for www in result_cube.values():
                                                    for zzz in www.values():
                                                        for yyy in zzz.values():
                                                                yyy[xx]='.'
        
        final_dict={}
        for w,dim in OrderedDict(sorted(result_cube.items())).items():   
            final_dict[w]={}
            for z,plan in OrderedDict(sorted(dim.items())).items():   
                final_dict[w][z]={}
                for y,line in OrderedDict(sorted(plan.items())).items():            
                    final_dict[w][z][y]={}
                    for x,v in  OrderedDict(sorted(line.items())).items():                
                        final_dict[w][z][y][x]=v
        return final_dict

    def display(self,cubes):
        for w,dim in cubes.items():     
            for z,plan in dim.items():    
                print(f"for {z=},for {w=}")     
                for y,line in plan.items():
                    count=0
                    for x,v in line.items():
                        count+=1
                        end=""
                        if count==len(line):
                            end="\n"
                        print(v, end =end)

    def boot_cube(self,cubes):
               
        print(f"==== INIT =====")
        cubes = self.extend_neighboor(cubes)
        self.display(cubes)
        for steps in range(1,7):
            print(f"==== round {steps} =====")
            result_cube={}
            active_side_cube={}
            
            for w,dim in cubes.items():  
                result_cube[w]={}
                active_side_cube[w]={}
                for z,plan in dim.items():   
                    result_cube[w][z]={}
                    active_side_cube[w][z]={}
                    for y,line in plan.items():
                        result_cube[w][z][y]={}
                        active_side_cube[w][z][y]={}
                        for x,v in line.items():
                            new_v=v
                            availability = self.check_availability(x,y,z,w,cubes)
                            active_side_cube[w][z][y][x]=0
                            if v=="#":                        
                                if not availability in [2,3]:
                                    #print(f"disabling cube at {z=}{y=}{x=}")
                                    new_v="."
                                else:
                                    active_side_cube[w][z][y][x]=availability
                            elif v==".":
                                if  availability ==3:                                    
                                    active_side_cube[w][z][y][x]=availability
                                    #print(f"enabling cube at {z=}{y=}{x=}")
                                    new_v="#"
                            result_cube[w][z][y][x]=new_v    
            cubes=result_cube
            print(self.answer(cubes))        
            #self.display(cubes)    
            #self.display(active_side_cube) 
            cubes = self.extend_neighboor(cubes)
        
        return cubes

    def answer(self,cubes):
        ans=0
        for w in cubes.values():
            for z in w.values():
                for y in z.values():
                    for x in y.values():
                        if x=="#":
                            ans+=1
        return ans

    def parse_to_cube(self,inputs):
        dim={}
        cubes={}
        line_dict={}
        for x,line in enumerate(inputs.splitlines()):
            col_dict={}
            for y,v in enumerate(line):
                col_dict[y]=v
            line_dict[x]=col_dict
        cubes[0]=line_dict
        dim[0]=cubes
        return dim

def test():
    inputs=""".#.
..#
###"""
    part1=Part1()
    cubes=part1.parse_to_cube(inputs)
    cubes = part1.boot_cube(cubes)
    # part1.display(cubes)
    assert 112 == part1.answer(cubes)

    part2=Part2()
    cubes=part2.parse_to_cube(inputs)
    cubes = part2.boot_cube(cubes)
    # part2.display(cubes)
    assert 848 == part2.answer(cubes)


def main():
    inputs="""#.##....
.#.#.##.
###.....
....##.#
#....###
.#.#.#..
.##...##
#..#.###"""
    part1=Part1()
    cubes=part1.parse_to_cube(inputs)
    cubes = part1.boot_cube(cubes)
    # part1.display(cubes)
    print(part1.answer(cubes))
    
    part2=Part2()
    cubes=part2.parse_to_cube(inputs)
    cubes = part2.boot_cube(cubes)
    # part2.display(cubes)
    print(part2.answer(cubes))

test()
main()