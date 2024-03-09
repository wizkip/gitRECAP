#LETS GOOOOOOO

from itertools import permutations


def perms(str):

    permlist = permutations(str)


    #Iterate through the LIST

    for perm in list(permlist):

        print(''.join(perm))

if __name__ == "__main__":

    str = "WAS"
    perms(str)

















