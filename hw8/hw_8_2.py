from tabulate import tabulate

data = '''id,name,segment,state,city
CG-12520,Claire Gute,Consumer,Kentucky,Henderson
DV-13045,Darrin Van Huff,Corporate,California,Los Angeles
SO-20335,Sean O'Donnell,Consumer,Florida,Fort Lauderdale
BH-11710,Brosina Hoffman,Consumer,California,Los Angeles
AA-10480,Andrew Allen,Consumer,North Carolina,Concord
IM-15070,Irene Maddox,Consumer,Washington,Seattle
HP-14815,Harold Pawlan,Home Office,Texas,Fort Worth
PK-19075,Pete Kriz,Consumer,Wisconsin,Madison
AG-10270,Alejandro Grove,Consumer,Utah,West Jordan
ZD-21925,Zuschuss Donatelli,Consumer,California,San Francisco
KB-16585,Ken Black,Corporate,Nebraska,Fremont
SF-20065,Sandra Flanagan,Consumer,Pennsylvania,Philadelphia
EB-13870,Emily Burns,Consumer,Utah,Orem
EH-13945,Eric Hoffmann,Consumer,California,Los Angeles
TB-21520,Tracy Blumstein,Consumer,Pennsylvania,Philadelphia
MA-17560,Matt Abelman,Home Office,Texas,Houston'''

lines = data.strip().split('\n')
# other variant:
# for line in lines:
#     row = line.split(",")
#     print(f"{row[0]: >7} {row[1]: >20} {row[2]: >15} {row[3]: >17} {row[4]: >17}")
rows = [line.split(',') for line in lines]

print(tabulate(rows))
