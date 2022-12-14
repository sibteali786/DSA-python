expenses = [
    2200,
    2350,
    2600,
    2130,
    2190
]

# 1. In Feb, how many dollars you spent extra compare to January?

extraDollar = expenses[1]- expenses[0]
print(extraDollar)

# 2. Find out your total expense in first quarter (first three months) of the year.
total = 0
for x in range(0,3):
    total +=expenses[x]
print(total)

# 3. Find out if you spent exactly 2000 dollars in any month
# My version
for i in expenses:
    if i == 2000:
        print("Yes")

# better version
print("Did i spent 2000$ in any month ?",2000 in expenses)

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list

expenses.append(1980)


# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

expenses[3] = expenses[3] - 200
print(expenses)


# Task No 2
heros=['spider man','thor','hulk','iron man','captain america']

# 1. Length of the list
print(len(heros))
# 2. Add 'black panther' at the end of this list
heros.append("black panther")
print(heros)
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
heros.pop()
heros.insert(3,"black panther")
print(heros)
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
heros[1:3] = ["Doctor Strange"]
print(heros)
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros.sort()
print(heros)

