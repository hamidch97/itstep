first_list = ['Neo', 'Trinity', 'Mouse']
second_list = ['Matrix', 'Forever', 'Alone']
output_list = []
for i in range(len(first_list)):
    for j in range(len(second_list)):
        output_list.append(first_list[i] + ' ' + second_list[j])

print(str(output_list))
