print("Title of program: Post-exam bot")
print()
while True:
  description = input("Could you describe how you feel in a sentence?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "bored":
      feelings_list.append("bored")
      encouragement_list.append("google a joke lah")
      counter += 1
    if each_word == "results":
      feelings_list.append("results")
      encouragement_list.append("they define you")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("you are stronger than you think")
    if each_word == "enjoying":
      feelings_list.append("enjoying")
      encouragement_list.append("share the fun")
      counter += 1
    if each_word == "lazy":
      feelings_list.append("lazy")
      encouragement_list.append("do something you like")
      counter += 1
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("cheer up the days will get better")
      counter += 1
    if each_word == "confused"
      feelings_list.append("confused")
      encouragement_list.append("talking to someone may help")

  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember that "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
