"""Functions to parse a file containing villager data."""

from unicodedata import name


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    unique_species = set()
    
    data = open(filename)
    for line in data:
        species = line.rstrip().split("|")[1]
        unique_species.add(species)

    return unique_species

#print(all_species("villagers.csv"))

def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """
    data = open(filename)
    villagers = []

    for line in data:
        name, species = line.rstrip().split("|")[:2]

        if search_string == "All":         #if search_string in ("All", species):
            villagers.append(name)
        elif search_string == species:
            villagers.append(name)

    return sorted(villagers)
    
#print(get_villagers_by_species("villagers.csv", "Anteater"))

def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    data = open(filename)
    
    fitness = []
    education = []
    play =[]
    fashion = []
    nature = []
    music = []
    
    for line in data:
        name, _, _, hobby, _ = line.rstrip().split("|")  #name, hobby= line.rstrip().split("|")[0],line.rstrip().split("|")[3]
        if hobby == "Fitness":
            fitness.append(name)
        elif hobby =="Nature":
            nature.append(name)
        elif hobby == "Education":
            education.append(name)
        elif hobby == "Fashion":
            fashion.append(name)
        elif hobby == "play":
            play.append(name)
        elif hobby == "Music":
            music.append (name)


    # TODO: replace this with your code

    return [(fitness), (nature), (education), (play), (fashion), (music)]
print(all_names_by_hobby("villagers.csv"))


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []
    data = open(filename)
    for line in data:
        all_data.append(tuple(line.rstrip().split("|")))

    # TODO: replace this with your code

    return all_data
#print(all_data("villagers.csv"))

def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """
    data = open(filename)
    for line in data:
        name, _, _, _, motto = line.rstrip().split("|")
        if villager_name == name:
            return motto

#print(find_motto("villagers.csv", "Cyrano"))

def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """
    likeminded = set()
    select_personality = None
    data = open(filename)
    
    for line in data:
        name

    # for line in data:
    #     name, _, personalities, _ = line.rstip().split("|")

    #     if name == villager_name:
    #         chosen_personalities == personalities
    #         break
        
    
    # if similar_personalities:
    #     for line in data:
    #         name, _, personalities, _ = line.rstip().split("|")
    #         if chosen_personalities == personalities:
    #             similar_personalities.add(name)  
            

    return similar_personalities
#print(find_likeminded_villagers("villagers.csv",name))