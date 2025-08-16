import logic_2048
if __name__=='__main__':
    mat=logic_2048.start_game()
while(True):
    x=input("Press the command : ")
    if(x.lower()=='w'):
        mat,flag=logic_2048.move_up(mat)
        status=logic_2048.get_current_state(mat)
        print(status)
        if(status=='Game Not Over'):
            logic_2048.add_new_2(mat)
        else:break
    elif(x.lower()=='s'):
        mat,flag=logic_2048.move_down(mat)
        status=logic_2048.get_current_state(mat)
        print(status)
        if(status=='Game Not Over'):
            logic_2048.add_new_2(mat)
        else:break
    elif(x.lower()=='a'):
        mat,flag=logic_2048.move_left(mat)
        status=logic_2048.get_current_state(mat)
        print(status)
        if(status=='Game Not Over'):
            logic_2048.add_new_2(mat)
        else:break
    elif(x.lower()=='d'):
        mat,flag=logic_2048.move_right(mat)
        status=logic_2048.get_current_state(mat)
        print(status)
        if(status=='Game Not Over'):
            logic_2048.add_new_2(mat)
        else:break
    else:
        print("Invalid Key Pressed")
    for row in mat:
        print(row)