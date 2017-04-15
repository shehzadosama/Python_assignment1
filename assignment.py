#             ------------- Question 3.4 -------------
# list= ['shehzad','hassan','saboor'];
# for i in range(0,len(list)):
#     print(list[i]+", You are invited to Dinenr");
#
#           --------------- Question 3.5 -------------
# print(list[1]+", Can't come in dinner");
# list[1] = 'ali rehan';
# for i in range(0,len(list)):
#     print(list[i]+ " still coming");
#
#           ---------------- Question 3.6 --------------
# print("We have more space for a Dinner !!");
# list.insert(0,'noman');
# list.insert(2,'anwar');
# list.append('saad');
#
# for i in range(0,len(list)):
#     print(list[i]+", You are invited to Dinenr");
#
#          ------------------ Question 3.7 --------------
# print("Sorry We can invite only two people for dinner :(");
# for i in range(0,len(list)-2):
#     print(list.pop() + ",Sorry we can't invit u to Dinenr");
# for i in range(0, len(list)):
#      print(list[i]+", You are still invited to Dinenr");
#
# del list[0];
#
# del list[0];
# # print(list);
# print("After removing all elements");
# print(list);

#             ---------------- Question 3.8  ---------------
# places = ['bangladesh','australia','zimbabwe','uae'];
# print(places);
# print(sorted(places));
# print(places);
# print(sorted(places,reverse=True));
# print(places);
# places.reverse()
# print(places);
# places.reverse()
# print(places);
# places.sort();
# print(places);
# places.sort(reverse=True);
# print(places);

#             ---------------- Question 3.9  ---------------
# list= ['shehzad','hassan','saboor'];
# for i in range(0,len(list)):
#     print(list[i]+", You are invited to Dinenr");
# print(len(list));


#             ---------------- Question 3.10 ---------------
# mountains = ['Denali','Longs peak','k2'];
# rivers = ['indus river','ganges','nile'];
# countries = ['pakistan','america','usa','uae','india'];
# cities = ['karachi','lahore','islamabad'];
# languages = ['english','urdu','french'];
# print("Length of Mountains List: "+str(len(mountains)));
# print("Length of Rivers List: "+str(len(rivers)));
# print("Length of Countries List: "+str(len(countries)));
# print("Length of Cities List: "+str(len(cities)));
# print("Length of Language List: "+str(len(languages)));
# mountains.append('mount evens');
# rivers.append('River thames');
# countries.append('canada');
# cities.append('peshawar');
# languages.append('spanish');
#
# print(mountains);
# print(rivers);
# print(countries);
# print(cities);
# print(languages);
#
# mountains.insert(1,'mount everest');
# rivers.insert(1,'River thames');
# countries.insert(1,'qatar');
# cities.insert(1,'faislabad');
# languages.insert(1,'chinese');
#
# print(mountains);
# print(rivers);
# print(countries);
# print(cities);
# print(languages);
#
# mountains.sort();
# rivers.sort();
# countries.sort();
# cities.sort();
# languages.sort();
#
# print(mountains);
# print(rivers);
# print(countries);
# print(cities);
# print(languages);
#
# mountains.sort(reverse=True);
# rivers.sort(reverse=True);
# countries.sort(reverse=True);
# cities.sort(reverse=True);
# languages.sort(reverse=True);
#
#
# print(mountains);
# print(rivers);
# print(countries);
# print(cities);
# print(languages);
#
# mountains.pop();
# rivers.pop();
# countries.pop();
# cities.pop();
# languages.pop();
#
#
# print(mountains);
# print(rivers);
# print(countries);
# print(cities);
# print(languages);
#
#
# mountains.reverse();
# rivers.reverse();
# countries.reverse();
# cities.reverse();
# languages.reverse();
#
# print(mountains);
# print(rivers);
# print(countries);
# print(cities);
# print(languages);
#
# del mountains[0];
# print(mountains);

#             ---------------- Question 4.10 ---------------
# list = ['laptop','pc','mobile','ipad','tablet'];
# print("First three elements of List are: ");
# print(list[:3]);
# print("Three items from the middle of the list are: ");
# print(list[2:5]);
# print("The last three items in the list are: ");
# print(list[-3:-1]);

#             ---------------- Question 4.11 ---------------
# pizzas = ['fajita','chiken','garlic'];
# friend_pizzas =  pizzas[:];
# pizzas.append('vegetable');
# friend_pizzas.append('bbq');
# print("My favorite pizzas are: ");
# for pizza in pizzas:
#     print(pizza);
# print("My friend’s favorite pizzas are: ");
# for friend_pizza in friend_pizzas:
#     print(friend_pizza);

#             ---------------- Question 4.12 ---------------
# my_foods = ['pizza', 'falafel', 'carrot cake'];
# friend_foods = my_foods[:];
# print("My favorite foods are:");
# for my_food in my_foods:
#     print(my_food);
# print("\nMy friend's favorite foods are:");
# for friend_food in friend_foods:
#     print(friend_food);

#             ---------------- Question 4.13 ---------------
# foods = ('biryani','chicken roll','bbq','pizza','zinger burger');
# for food in foods:
#     print(food);
# # foods[0] = 'fried rice';  #ERROR
# foods = ('chowmin','french fries','bbq','pizza','zinger burger');
# print('Revised Menu');
# for food in foods:
#     print(food);


#             ---------------- ProjectEuler Problem 2 (FibonacciS Sum) ---------------
n1=0;
n2=1;
sum=0;
for i in range(1,40):
    n3=n1+n2;
    if n3 % 2==0 and n3 < 4000000:
        sum +=n3;
    # print(" "+str(n3));
    n1=n2;
    n2=n3;
print(sum);
