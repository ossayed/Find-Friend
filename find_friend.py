def openfile():
    global user_input
    iscorrect = False
    user_input = input("please enter the file name:")
    while iscorrect != True:
        if user_input != "network.txt":
            user_input = input("file name is incorrect please try again:")
        else:
            iscorrect = True

def readfile(user_input):
    global network,user_num
    network = []
    with open(user_input) as f:
        for line in f:
            network.append(line.strip().split(' '))
    user_num = int(network[0][0])
    network.pop(0)


def num_in_common_between_lists(list1,list2):
    common_items = 0
    for y in range(0,len(list2)):
        if list1[y] == 1 and list2[y] == 1:
            common_items = common_items + 1
    return common_items



def calc_similarity_scores(network):
    global similarity_matrix
    similarity_matrix= [[0 for col in range(user_num+1)] for row in range(user_num+1)]
    friend_list = [[0 for col in range(user_num+1)] for row in range(user_num+1)]

    for x in range(0,len(network)):
        friend_list[int(network[x][0])][int(network[x][1])] = 1
        friend_list[int(network[x][1])][int(network[x][0])] = 1

    for x in range(user_num+1):
        for y in range(user_num):
            similarity_matrix[x][y] = num_in_common_between_lists(friend_list[x],friend_list[y])





def recommend(user_id,network,similarity_matrix):
    similarity_matrix[user_id][user_id] = 0
    for x in range(0,user_num):
        if similarity_matrix[user_id][x] == max(similarity_matrix[user_id]):

            for y in range(0,len(network)):
                if network[y][0] == user_id and network[y][1] == x:
                    similarity_matrix[user_id][x] = 0
                elif network[y][1] != x:
                    friend_request = x

    print(friend_request)


def main():
    openfile()
    readfile(user_input)
    calc_similarity_scores(network)
    loop_control = True
    while loop_control == True:
        try:
            user_id = int(input("enter a user you want a friend recommendation for:"))
            recommend(user_id, network, similarity_matrix)
            again = input("would you like to continue?")
            if again == "No"or again == "NO" or again == "no" or again == "nO":
                loop_control = False


        except:
            print("invalid input please try again")


main()




