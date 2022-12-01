
import common
    
data=common.get_data_from_site(year=2022,day=1)
parsed=common.parse_data_by_groups(data,as_int=True)

sum_parsed=[sum(p) for p in parsed]
print(max(sum_parsed))

print(sum(sorted(sum_parsed,reverse=True)[:3]))