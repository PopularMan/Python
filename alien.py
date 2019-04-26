#coding=utf-8
aliens=[]
for alien_number in range(30):
    new_alien = {'color':'green','point':5,'speed':'slow'}
    aliens.append(new_alien)

print('creae success')
for alien in aliens[:5]:
    print(alien)
print("...")

print("一共创建个了"+str(len(aliens)))
