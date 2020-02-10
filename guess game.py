import random 
wrong = ['ap_le', 'bal_', 'c_t', '_og', 'ele_hant','fis_', 'g_at', 'h_use', 'icebe_g', 'jac_al',
    'ki_g', 'l_ama', 'mo_key', 'nu_se', '_ctopus',
    'pi_', 'qu_en', 'ro_ot', 'sn_ke', 
    'unic_rn', 'vam_ire', 'x-_ay', 'y_k',
    'ze_ra']
correct = ['apple','ball','cat','dog','elephant','fish','goat','house','iceberg','jackel','king','llama','monkey','nurse','octopus','pie','queen','robot','snake','unicorn','vampire','x-ray','yak','zebra']
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
word = random.choice(wrong)
rn = random.choice(letters)
i = 0
while True:
    new = word.replace("_",rn)
    if new in correct:
        break
    rn = random.choice(letters)
a = []

guess = ""
i = 0
print("The word is : " + word)
print("You have to guess the missing letter")
print("You have 3 tries ")
start = ""
start = input("Write Start to begin the game: ")
start = start.lower()
while start != 'start':
    start = input("Write Start to begin the game: ")
    start = start.lower()
if start == "start" :
    while i <= 2:
        print("The word is " + word)
        guess = input("Please Enter the missing letter Here: ")
        if guess == rn:
            print("That's right ! YOU WON!")
            print("the word is " + new)
            break
        elif guess != rn and i == 2:
            print("GAME OVER! the word is: "+new+"\nYou're out of chances \nto try again, replay the program")
            break
        else:
            print("That's wrong plaese try again")
            i += 1
    
        
    