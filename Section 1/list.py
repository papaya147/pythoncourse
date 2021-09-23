my_list = ["cat","dog",546,"penguin","human"]

element1 = my_list[1] # element1 = 'dog'
element2 = my_list[-2] # element2 = 'penguin'
element3 = my_list[1:4] # element3 = ['dog', 546, 'penguin']
element4 = my_list[1:-1] # element4 = ['dog', 546, 'penguin']
element5 = my_list[2:] # element5 = [546, 'penguin', 'human']

my_list.append("rat") # my_list = ['cat', 'dog', 546, 'penguin', 'human', 'rat']
my_list[1] = "rat" # my_list = ['cat', 'rat', 546, 'penguin', 'human', 'rat']
my_list.insert(1,"dog") # my_list = ['cat', 'dog', 'rat', 546, 'penguin', 'human', 'rat']

print(my_list)