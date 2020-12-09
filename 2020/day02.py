import common

class password_rule():
    def __init__(self,input,rule_type):
       self.parse_input(input)
       self.rule_type=rule_type

    def parse_input(self,input):
        temp=input.split(" ")
        min_max=temp[0].split("-")
        self.min=int(min_max[0])
        self.max=int(min_max[1])
        self.value=str(temp[1].strip())
    
    def is_valid(self,password):
        if self.rule_type==0:
            count=password.count(self.value)
            if self.min <= count <= self.max:
                return True
            return False
        elif self.rule_type==1:
            if password[self.min -1] == self.value and password[self.max -1] == self.value:
                return False
            if password[self.min -1] == self.value or password[self.max -1] == self.value:
                return True
            return False
        else:
            raise ValueError

    def __str__(self) -> str:
        if self.rule_type==0:
            return f"the value {self.value} must be seen at least {self.min} and at most {self.max} times"
        elif self.rule_type==1:
            return f"the value {self.value} must be seen at least in position {self.min} or in position {self.max} (position starting at 1)"

class password():
    def __init__(self,input,rule_type):
        self.rule_type=rule_type
        self.parse_input(input)

    @property
    def is_valid(self):
        return self.password_rule.is_valid(self.password)
    
    def parse_input(self,input):
        inputs=input.split(":")
        rules=str(inputs[0]).strip()
        self.password_rule=password_rule(rules,self.rule_type)
        self.password=str(inputs[1].strip())
    
    def __str__(self) -> str:
        return f"the password {self.password} posess the following rule [{self.password_rule}] - The password validity check is {self.is_valid}"

def parse_input_to_password(list_input,rule_type=0):
    return [password(i,rule_type) for i in list_input]

def count_valid_password(list_password):
    nb=0
    for p in list_password:
        if p.is_valid:
            nb+=1
        #print(p)
    print(f"There is {nb} valid password (so there is {len(list_password)-nb} invalid password)")
    return nb

def test():
    input=["1-3 a: abcde","1-3 b: cdefg","2-9 c: ccccccccc"]
    print(input)
    list_password=parse_input_to_password(input)
    [print(p) for p in list_password]
    nb=count_valid_password(list_password)
    assert nb==2
    list_password=parse_input_to_password(input,1)
    nb=count_valid_password(list_password)
    assert nb==1
    [print(p) for p in list_password]

def main():
    inputs=common.get_input_from_file("day02.txt")    
    list_password=parse_input_to_password(inputs)
    nb=count_valid_password(list_password)
    assert nb==528
    list_password=parse_input_to_password(inputs,1)
    nb=count_valid_password(list_password)

test()
main()


