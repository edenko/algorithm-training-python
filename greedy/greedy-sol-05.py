# 그리디 - 단속카메라 v3

routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]

routes.sort(key=lambda x: x[1])
point = -30001
count = 0

for item in routes:
    if (point < item[0]):
        count += 1
        point = item[1]
    
print(count)
