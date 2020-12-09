import common
import re
class passport():
    required_fields=["byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid"]
    optional_fields=["cid"]

    def __init__(self,inputs):
        self.append(inputs)

    def append(self,data):
        for input in data.split():
            key,value = input.split(":")
            self.__setattr__(key,value)

    def is_valid(self)->bool:
        for f in self.required_fields:
            if f not in self.__dict__.keys():
                return False
        return True
    
    def validate_rules(self)->bool:
        if not (1920<= int(self.byr) <=2002):
            return False
        if not (2010<= int(self.iyr) <=2020):
            return False
        if not (2020<= int(self.eyr) <=2030):
            return False
        if self.hgt[-2:]=="in":            
            if not (59<= int(self.hgt[:-2]) <=76):
                return False
        else:
            if not (150<= int(self.hgt[:-2]) <=193):
                return False
        if not re.match(r"#[a-f0-9]{6}$",self.hcl):
            return False
        if not self.ecl in ["amb","blu","brn","gry","grn","hzl","oth"]:
            return False
        if not len(self.pid) == 9:
            return False
        return True
        
def parse_input_into_passport(inputs):
    passports=[]
    index=0
    for line in inputs:
        if line=="\n" or line=="":
            index+=1
        else:
            if len(passports) == index :
                passports.insert(index,passport(line))
            else:
                passports[index].append(line)
    return passports

def validate_passports(passports):
    valid_passport=[p for p in passports if p.is_valid()]
    print(f"number of complete password : {len(valid_passport)}")
    valid_passport=[p for p in valid_passport if p.validate_rules()]
    print(f"number of valid password : {len(valid_passport)}")
    return len(valid_passport)
    


def test():
    inputs=["ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
            "byr:1937 iyr:2017 cid:147 hgt:183cm",
            "",
            "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
            "hcl:#cfa07d byr:1929",
            "",
            "hcl:#ae17e1 iyr:2013",
            "eyr:2024",
            "ecl:brn pid:760753108 byr:1931",
            "hgt:179cm",
            "",
            "hcl:#cfa07d eyr:2025 pid:166559648",
            "iyr:2011 ecl:brn hgt:59in"]

    passports=parse_input_into_passport(inputs)
    assert 2==validate_passports(passports)

def test2():
    inputs=["eyr:1972 cid:100",
            "hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926",
            "",
            "iyr:2019",
            "hcl:#602927 eyr:1967 hgt:170cm",
            "ecl:grn pid:012533040 byr:1946",
            "",
            "hcl:dab227 iyr:2012",
            "ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277",
            "",
            "hgt:59cm ecl:zzz",
            "eyr:2038 hcl:74454a iyr:2023",
            "pid:3556412378 byr:2007",
            "",
            "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980",
            "hcl:#623a2f",
            "",
            "eyr:2029 ecl:blu cid:129 byr:1989",
            "iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm",
            "",
            "hcl:#888785",
            "hgt:164cm byr:2001 iyr:2015 cid:88",
            "pid:545766238 ecl:hzl",
            "eyr:2022",
            "",
            "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"]
    passports=parse_input_into_passport(inputs)
    assert 4==validate_passports(passports)

def main():
    inputs=common.get_input_from_file("day04.txt")
    
    passports=parse_input_into_passport(inputs)
    assert 147==validate_passports(passports)

test()
test2()
main()