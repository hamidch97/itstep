day_list = ['monday', 'thuesday', 'wednesday', 'thursday', 'saturday', 'sunday']
taskes = [["homework , call mom"],
          ['work , call frind'],
          ['work'],
          ['work'],
          ['work'],
          ['play foot-ball'],
          ['meting with frinds']
          ]
user_input = input("enter your day")
result = dict({})
for i in range(0, len(day_list)):
    if user_input == day_list[i]:
        result[day_list[i]] = taskes[i]


print(result)
