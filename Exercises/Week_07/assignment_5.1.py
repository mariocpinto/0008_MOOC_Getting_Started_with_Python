# Write a program that reads a list of numbers until "done" is entered.
# Once done is entered, print count, total and avergae of numbers.
# If the user enters anything other than a number, 
#       print an error message and skip to the next number.

# Initialize count & sum
count = 0
sum = 0

while True :
    input_num = input('Enter a number: ')
    
    if input_num == 'done' :
        break
        
    try:
        num = float(input_num)
        
    except:
        print('Invalid Input')
        continue
        
    count = count + 1
    sum = sum + num
    
print('Count = ',count)
print('Total = ',sum)

if count != 0 :
    print('Average = ',sum/count)
else:
    print('Average = 0')

