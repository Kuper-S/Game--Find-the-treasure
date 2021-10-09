player_name = input("What is your name ? ")
print(f"Hello {player_name} , Welcome to Treasure Island.")
print("""
Your mission is to find the treasure. Do you think you have the skills to find it?  
Alright lets find out what you got! remember one wrong move and you done!
            ,.  ,.
            ||  ||
           ,''--''.
          : (.)(.) :
         ,'        `.
         :          :
         :          :
         `._m____m_,' """)
# first chapter
print("""first chapter:
You left your castle in the dark, you walk throw the "Evil Forest" , and then you've reached a crossroads ,
You have to choose your own path , where do you wanna go ? left of right.""")
left_right = input("Left or Right ? \n").lower()

if left_right == "left":
    print("\nThat is a good choose , you save your self from a ruthless bandit gang!!!")

elif left_right == "right":
    print(f"poor {player_name} , you just caught by a ruthless bandit gang!!! , they took your money and map ,"
          f"and now you lost in the Evil Forest , Game Over !")
else:
    print("Invalid option , pls try again ")
# second chapter

print("""Second chapter : now , After you've safely left the Evil Forest , you reach to the Giant Orc Bridge 
, unfortunately there is a suspicious Orc guard at the entrance to the bridge , you have two options :
1)To wait until he will go to his night patrol
2)Jump into the river below the bridge and swim to the other side.
             ___
       .----.        <  ))
       | == |      <     )))- |
    ___| :: |___    <   )))
    \  `----'  //  (/) (
     \   `.   /( // ///
     |    :   |   ////
     \   _._  /  `"   <_>
      xxx(o)xx""")

swim_wait = input("Swim / Wait ?").lower()
if swim_wait == "swim":
    print("The flow in the river was too strong and you fell from the highest waterfall in the world ,Game over ",
          player_name)
elif swim_wait == "wait":
    print("that's was the right thing to do, while you waited "
          ", the guard left the entrance to the bridge and you quickly went through the bridge")
else:
    print("Invalid option , Game over")

# third chapter

print("""Third chapter : Last mission , after a really long and way ,
now you're facing the most important task of all to guess behind which door the treasure is hidden ???   
yes, it's sounds easy for a skillful and brave player like you , but now is your money time . . .

          
          
            __________    
           | |  ||  | |    (1)
           | |  ||  | |                                                    
           |  __  __  |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |  __  __()|
           | |  ||  | |
           | |  ||  | |  
           | |__||__| |
           
                   
           |__________|
           | |__||__| |   (2)
           |  __  __()|
           | |  ||  | |                                
           | |  ||  | |                                 
           | |  ||  | |
           | |  ||  | |                                   
           | |__||__| |
           |__________| 

           
            __________       
           |  __  __  |   (3)
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |  __  __()|
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |__________|


""")


doors = input("which door you choose ? Blue / Green / Yellow ? ").lower()
if doors == "yellow":
    print(f"Unbelievable , {player_name} you are the best !  you've chose the right door and you found the treasure !!")
    print(f"{player_name} you won!!! the first to ever find the treasurer!! you are the best! :);)")
elif doors == "blue":
    print("Ops , you tried the wrong door and you went straight to the guards' room , Game over!")
elif doors == "green":
    print("Oh no ! , you tried the wrong door and you went straight to the Orc King bedroom!!! , Game over!!")
else:
    print("Invalid option , Game over")

