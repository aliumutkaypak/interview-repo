import json
file=open('data/sat.json')
data=json.load(file)
info=data['data']
schoolnumber=len(info)
noinformation=0;
temp=(float(info[0][11])+float(info[0][12])+float(info[0][13]))/4
diftemp=abs(float(info[0][11])-float(info[0][12]))
mathematicsmean=0
for i in range(schoolnumber):
    if info[i][10]==None:
        noinformation+=1
        continue
    mathematicsmean+=float(info[i][11])
    mean=(float(info[i][11])+float(info[i][12])+float(info[i][13]))/4
    if mean >=temp:
        temp=mean
        index=i
    if abs(float(info[i][11])-float(info[i][12]))>=diftemp:
        difindex=i;
mathematicsmean=mathematicsmean/schoolnumber
print('The number of schools is {}'.format(schoolnumber))
print('The number of schools which have no associated testing information is {}'.format(noinformation))
print('{} have the best overall scores'.format(info[index][9]))
print('{} have the most divergent scores between mathematics and critical reading'.format(info[difindex][9]))
print('Mathematics avarage score in the whole schools is {}'.format(mathematicsmean))
file.close()

