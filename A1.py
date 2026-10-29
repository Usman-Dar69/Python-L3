name = input("Enter your real name, Agent:  ")
gadget = input("Enter your favorite gadget:  ")

agent_number = 7
speed_rating = 9.8
mission_count = 27
height = 6.2 
is_active = True


print("Name: ", name, "type: ", type(name))
print("Gadget: ", gadget, "type: ", type(gadget))
print("Agent Number: ", agent_number, "type: ", type(agent_number))
print("Speed Rating: ", speed_rating, "type: ", type(speed_rating))
print("Mission Count: ", mission_count, "type: ", type(mission_count))
print("Height: ", height, "type: ", type(height))
print("Is Active: ", is_active, "type: ", type(is_active))


agent_number_text = str(agent_number)
mission_count_text = str(mission_count)
mission_rating_text = str(speed_rating)
status_text = str(is_active)
height_text = str(height)
speed_rating = str(speed_rating)   

print("Agent Number: ", agent_number_text, "type: ", type(agent_number_text))
print("Mission Count: ", mission_count_text, "type: ", type(mission_count_text))
print("Speed Rating: ", mission_rating_text, "type: ", type(mission_rating_text))
print("Height: ", height_text, "type: ", type(height_text))
print("Is Active: ", status_text, "type: ", type(status_text))
print("Status_as_text: ", status_text, "type: ", type(status_text))
 

first_three = name[0:3]
last_one = name[-1:]
code_name = first_three + last_one
print("First three letters of your name: ", first_three)
print("Last letter of your name: ", last_one)
print("Your code name is: ", code_name)

reversed_gadget = gadget[::-1]
print("Your favorite gadget reversed is: ", reversed_gadget)

badge_line_1 = "Agent Name: " + code_name.upper() 
badge_line_2 = "ID: " + agent_number_text + "Missions: " + mission_count_text
badge_line_3 = "Speed Rating: " + speed_rating + "Active: " + status_text
badge_line_4 = "Gadget: " + reversed_gadget.upper()


print("")
print("Your Agent Badge:")
print(badge_line_1)
print(badge_line_2)
print(badge_line_3)
print(badge_line_4)
print("==========================================")

