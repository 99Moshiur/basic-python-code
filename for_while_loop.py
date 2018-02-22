# Now this code for loop:

number = [1,2,3,4,5,6]
for item in number:
    print(item)

# For loop with string:
string = ["Redoy","Abdul Hai","Omor FAruk Orofe Hacker","unknown name"]
for item in string:
    print(item)
    #End for loop


#Start while loop:
# this like run and this current run will be increased Until then is 100 And when is == 100 give me return false
run = True
current_run = 1
while run:
    if current_run == 100:
        run = False
    else:
        print(current_run)
        current_run += 1
