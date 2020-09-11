"""
-------------------------------------------------------
CLASS FOOD_utilities
-------------------------------------------------------
Author:  Anshul Khatri
ID:      193313680
Email:   khat3680@mylaurier.ca
__updated__ = "2020-01-15"
-------------------------------------------------------
"""

from Food import Food



def get_food():
    """
    -------------------------------------------------------
    Creates a food object by requesting data from a user.
    Use: f = get_food()
    -------------------------------------------------------
    Returns:
        food - a completed food object (Food).
    -------------------------------------------------------
    """
    name=input("Name:")
    print("Origin")
    print(Food.origins())
    ori=int(input(": "))
    vegTemp = input("Vegetarian (Y/N):")
    if vegTemp=="Y":
        veg=True
    else:
        veg=False
    cal=int(input("Calories:"))
    food = Food(name, ori, veg, cal)
    return food

def read_food(line):
    """
    -------------------------------------------------------
    Creates and returns a food object from a line of string data.
    Use: f = read_food(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of food data in the format
          name|origin|is_vegetarian|calories (str)
    Returns:
        food - contains the data from line (Food)
    -------------------------------------------------------
    """

    l=line.split("|")
    name=l[0]
    ori=int(l[1])
    vegTemp=l[2]
    if vegTemp=="True":
        veg=True
    else:
        veg=False
    cal=int(l[3]) 
    food=Food(name,ori,veg,cal)
    

    return food


def read_foods(file_variable):
    """
    -------------------------------------------------------
    Reads a file of food strings into a list of Food objects.
    Use: foods = read_foods(file_variable)
    -------------------------------------------------------
    Parameters:
        file_variable - a file of food data (file)
    Returns:
        foods - a list of food objects (list of Food)
    -------------------------------------------------------
    """
    foods = []

    file_variable.seek(0)
    for line in file_variable:
        f=read_food(line)
        foods.append(f)
    return foods


def write_foods(file_variable, foods):
    """
    -------------------------------------------------------
    Writes a list of food objects to a file.
    file_variable contains the objects in foods as strings in the format
          name|origin|is_vegetarian|calories
    Use: write_foods(file_variable, foods)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file)
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """
    for f in foods:
        f.write(file_variable)
        
    return


def get_vegetarian(foods):
    """
    -------------------------------------------------------
    Creates a list of vegetarian foods.
    Use: v = get_vegetarian(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        veggies - Food objects from foods that are vegetarian (list of Food)
    -------------------------------------------------------
    """
    veggies=[]
    for f in foods:
        if f.is_vegetarian ==True:
            veggies.append(f)
    
    return veggies

def by_origin(foods, origin):
    """
    -------------------------------------------------------
    Creates a list of foods by origin.
    Use: v = by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - a food origin (int)
    Returns:
        origins - Food objects from foods that are of a particular origin (list of Food)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))
    origins=[]
    for i in range(len(foods)):
        if foods[i].origin== origin: 
            origins.append(foods[i])
    
    return origins

def average_calories(foods):
    """
    -------------------------------------------------------
    Determines the average calories in a list of foods.
    Use: avg = average_calories(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        avg - average calories in all Food objects of foods (int)
    -------------------------------------------------------
    """
    avg = 0
    tot = 0
    
    for i in range(len(foods)):
        tot += foods[i].calories
        
    avg = tot/(len(foods))

    return avg

def calories_by_origin(foods, origin):
    """
    -------------------------------------------------------
    Determines the average calories in a list of foods.
    Use: a = calories_by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the Food objects to find (int)
    Returns:
        avg - average calories for all Foods of the requested origin (int)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))
    avg=0
    k = []
    k=by_origin(foods,origin)
    
    for f in range(len(k)):
        
        avg+=k[f].calories
    avg=avg/len(k)
    
    return avg
    # Your code here
def food_table(foods):
    """
    -------------------------------------------------------
    Prints a formatted table of foods, sorted by name.
    Use: food_table(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """
    print("Food                                Origin       Vegetarian Calories")
    print("----------------------------------- ------------ ---------- --------")
    for i in foods:
        if (i.is_vegetarian==True):
            veg = "True"
        else:
            veg = "False"
        calories = str(i.calories)
        print("{:36}{:18}{:>5}{:>9}".format(i.name,Food.ORIGIN[int(i.origin)],veg,calories))
    
    #print("{}".format(i.name))
    return


def food_search(foods, origin, max_cals, is_veg):
    """
    -------------------------------------------------------
    Searches for foods that fit certain conditions.
    Use: results = food_search(foods, origin, max_cals, is_veg)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the food; if -1, accept any origin (int)
        max_cals - the maximum calories for the food; if 0, accept any calories value (int)
        is_veg - whether the food is vegetarian or not; if False accept any food (boolean)
    Returns:
        result - a list of foods that fit the conditions (list of Food)
            foods parameter must be unchanged
    -------------------------------------------------------
    """
    assert origin in range(-1, len(Food.ORIGIN))

    result = []
    for i in range(len(foods)):
        if is_veg == "True":
            is_veg = True
        if is_veg == "False":
            is_veg = False
        if (foods[i].origin==origin or origin == -1) and (foods[i].calories<=max_cals or max_cals == 0) and (foods[i].is_vegetarian is is_veg):
            result.append(foods[i])

    return result

