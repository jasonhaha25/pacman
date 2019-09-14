if s == "cherry":
            screen.blit(cherry,[j, i,20,20])

def check_path(s):
    return s == "" or s == "-" or s == "c" or s =="cherry"


if score % 700 == 0 and score != 0: 
        maze[17][13]= "cherry"