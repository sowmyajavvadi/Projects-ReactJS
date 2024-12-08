# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,

# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

list=[2200,2350,2600,2130,2190]
# 1. In Feb, how many dollars you spent extra compare to January?
print("how many dollars you spent extra compare to January:-", list[1]-list[0])

# 2. Find out your total expense in first quarter (first three months) of the year.
print("total expense in first quarter ", list[0]+list[1]+list[2])

# 3. Find out if you spent exactly 2000 dollars in any month
for i in range(len(list)):
    if list[i]== 2000:
        print("spent exactly 2000",i)
        break
    else:
        print("spent not exactly 2000")
        break

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
list.append(1980)
print("Add this item to our monthly expense list",list)

# 5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this
print("got a refund of 200$",list[3]-200)