'''shopping_list =[]
shopping_list.append("яблоко")
shopping_list.append("молоко")
shopping_list.append("хлеб")
shopping_list.append("яйца")
shopping_list.append("соль")
print (shopping_list)
for item in shopping_list:
    print(item)

del shopping_list [1]
print (shopping_list)
shopping_list[0] = "банан"
print (shopping_list)
b =len(shopping_list)
print (b)'''
N= int(input())
k = int(input())-1
people = list(range(1,N+1))
while len(people) !=1:
    k = k% len(people)
    del people[k]
    k+=2
    print (people)
