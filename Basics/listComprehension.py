# # Decimel point ex. 22.1
# temps = [221, 234, 340, 230]

# # More difficult way to do it
# new_temps = []
# for temp in temps:
#     new_temps.append(temp / 10)
# print(new_temps)

# # One line way
# new_temps2 = [temp / 10 for temp in temps]
# print(new_temps2)

# With no data value comprehended
weather_temps = [221, 234, 340, -9999, 230]

new_weather_temp = [temp / 10 for temp in weather_temps if temp != -9999]

print(new_weather_temp)

# with else statment, listComprehension
new_weather_temp = [temp / 10 if temp != -9999 else 0 for temp in weather_temps]