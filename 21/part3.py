with open("output2.txt") as file:
    data = file.read().splitlines()


results = []
for i in range(len(data) - 1):
    results.append(int(data[i + 1]) - int(data[i]))

print(results)



# result = 4
# difference = 5
# for i in range(26501365):
#     print(i)
#     result += difference
#     print(result)
#     difference += 2
# print(result)

