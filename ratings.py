"""Restaurant rating lister."""
new_file = open("scores.txt")
rest_dict = {}
for line in new_file:
    line = line.rstrip()
    file_in_array = line.split(":")
    for idx in range(0,len(file_in_array)):
        rest_dict[file_in_array[0]] = file_in_array[1]
  
# put your code here

resta_name = input('Restaurant Name:').title()
score = input("Restaurant Score:")
rest_dict[resta_name] = score
print("========= Ratings============")
for keynames in sorted(rest_dict.items()):
    print(f'{keynames[0]} is rated at {keynames[1]}.')

    

