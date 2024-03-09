#LETS GOOOOOOO


from itertools import permutations

#lets define a simple function

def sang(str):


    #create a LIST
    permlist = permutations(str)

    #Iterate through this list

    for perm in list(permlist):

        print(''.join(perm))


if __name__ == "__main__":

    str = "SANG"
    sang(str)

