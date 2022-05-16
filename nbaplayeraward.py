import pandas as pd
import matplotlib.pyplot as plt
import re
import csv


text = 'C:/Users/Emerson/Downloads/nbaplayerawards.csv'
read_file = pd.read_csv (r'C:\Users\Emerson\Downloads\nbaplayerawards.csv')


def has_accolades(text):
    patterns = '[1-9]'
    with open(text, 'rb') as csvfile:
        reader = csv.reader(open(text, 'rU'))
        for i in reader:
            string1=""
            for chr in i:
                string1=string1+chr
            if re.search(patterns, string1):
                print("accolade found!")

            else:
                print("no accolade")

class Database:
    """The Database class will evaluate the top 75 players from the 75th
    Anniversary team. Using the information from the top 75 players the
    user of the program will have the ability to see who is apart of this
    team as well as find specific information of any individual of this list
    ranging from the amount of MVPs, DPOYs, Championships, Finals MVPs, and
    Scoring Titles. With finding out this information they can decide to
    compare players of this list or find information soley on a player they
    want from the 75th Anniversary team. 
    
    Attributes:
        nbaplayers: The nbaplayers attribute is a list of dictionaries that give
        the information of an NBA player: Name, MVPs, DPOYs, Championships, 
        Finals MVPs, and Scoring Titles.
    """
    def __init__(self, path): 
        """The __init__ method will create and populate the nbaplayers attribute
        using the information provided in the txt file of The 75th Anniversary
        Team.

        Args:
            path (str): A path to the file being used that is filled with all of
            an NBA players stats.
            
        Side effects:
            Sets attribute, nbaplayers, to an empty list
        """
        self.nbaplayers = {}
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip().split("\t")
                self.nbaplayers[line[0]] = line[1:]
    
    def playerstats(self, name): #Orlando Aguilar (Optional parameters/use 
        #of keyword arguments)
        """The playerstats give the user the different number of accolades
        that the NBA player has won in their career. 
        
        Args:
            name (str): The name of the NBA player.
        
        Side effects:
            Prints the name of the NBA player and the 5 accolades 
            that belong to that specific player.
           
        """
        if name.upper() not in self.nbaplayers:
            raise KeyError("NBA Player not on the Top 75 Team.")
        else:
            name = name.upper()
            print(f"{name.title()} "
                f"and his accolades: MVP: {self.nbaplayers[name][0]}"
                    f", DPOY: {self.nbaplayers[name][1]}"
                        f", Champion: {self.nbaplayers[name][2]}"
                            f", FMVP: {self.nbaplayers[name][3]}"
                                f", Scoring Title: {self.nbaplayers[name][4]}")
        
    def compare(self, name1, name2): #Orlando Aguilar (Conditional Expressions)
        """The compare method is a method that will be used in order for the user
        of our program to compare two players and their different statistics being
        able to determine who is better between the two NBA players.

        Args:
            name1 (str): The name of the first NBA player the user wants to
            use to compare to the second player.
            name2 (str): The name of the second NBA player the user wants to use
            to compare to the first player.
            
        Side effects:
            Prints a string showing which player has more accolades than
            the other.
        """
        if name1.upper() not in self.nbaplayers or name2.upper() \
            not in self.nbaplayers:
            raise KeyError("Sorry, one or both NBA Players are not on " \
                "the 75th Anniversary Team.")
        else:
            name1 = name1.upper()
            name2 = name2.upper()
            mvp1 = int(self.nbaplayers[name1][0])
            dpoy1 = int(self.nbaplayers[name1][1])
            chip1 = int(self.nbaplayers[name1][2])
            fmvp1 = int(self.nbaplayers[name1][3])
            st1 = int(self.nbaplayers[name1][4])
            mvp2 = int(self.nbaplayers[name2][0])
            dpoy2 = int(self.nbaplayers[name2][1])
            chip2 = int(self.nbaplayers[name2][2])
            fmvp2 = int(self.nbaplayers[name2][3])
            st2 = int(self.nbaplayers[name2][4])
            name1_accolades = \
                int(mvp1)+int(dpoy1)+int(chip1)+int(fmvp1)+int(st1)
            name2_accolades = \
                int(mvp2)+int(dpoy2)+int(chip2)+int(fmvp2)+int(st2)
            
            #Conditional Expressions
            #Many f-strings here due to using "\" in one f-string will cause
            #much white space within the f-string statements.
        print(f"{name1.title()} has {name1_accolades} total accolades and "
            f"{name2.title()} has {name2_accolades} total accolades, so"
            f"{name1.title()} is the better player.") \
            if name1_accolades > name2_accolades else \
                print(f"{name2.title()} has {name2_accolades} total "
                    f"accolades and {name1.title()} has {name1_accolades}"
                    f" total accolades, so {name2.title()} "
                    f"is the better player.") \
                        if name2_accolades > name1_accolades else \
                            print(f"{name1.title()} has {name1_accolades} total"
                                  f" accolades and {name2.title()} has "
                                  f"{name2_accolades} total accolades,"
                                  f" so both players are equal!")  
    def panda_method(self, path):#Yaseen
        """This method is used to show the user if they want to, who has the most MVP in the top 75 players list

        Args:
            path (str): a path to the file being used that has TOP 75 NBA players stats
            
        Side effect: 
            prints the data frame of the total amount oF MVPs the 75 players has
            
        """
        df = pd.read_csv(path) 
        by_mvp = df[["Name","MVP"]].sort_values(by="MVP",ascending=False)
        print(by_mvp)

    def graph_method(self, path):#Yaseen
        """This method is used to display a graph that shows the amount of MVPs that the top 75 players have 

        Args:
            path (string): a path to the file being used that has TOP 75 NBA players stats
            
        Side effect:
            displays a graph of the data frame of the total amount of MVPs the 75 players has
            
        """
        df = pd.read_csv(path)
        dfg = df.groupby("MVP")["Name"].count()
        dfg.plot.bar(x="MVP",y="Name")
        plt.show()
                 
def main():
    """The main function will go through the entire program asking questions
    to the user about what and what they do and don't want to run.
    
    Side effects:
        Prints and runs the code
    """
    #Instantiating the Class
    db = Database("nbaplayerawards.txt")
    #Welcoming the user to our program.
    print("Hello! Welcome to the NBA 75th Anniversary Database!")
    #The different methods.
    try:
        playerstats_method = db.playerstats(name=input("Let's get you started! " \
        "What NBA Player would you like to know the accolades of? "))
    except:
        playerstats_method = db.playerstats(name=input("Player not found! " \
        "What NBA Player would you like to know the accolades of? "))
    question1 = input("Would you like to compare NBA Players? ")
    if question1 == "no":
        pass
    else:
        compare_method = db.compare(name1=input("NBA Player 1? "),name2=input("NBA Player 2? "))
        print(compare_method)
    question2 = input("Would you like to see a list of the amount of mvps each player has earned? ")
    if question2 == "no":
        pass
    else: 
        panda_method = db.panda_method("nba_top_75.csv")
        print(panda_method)
    question3 = input("Do you want to see a graph of the most MVPs based on the database? ")
    if question3 == "no":
        pass
    else: 
        graph_method = db.graph_method("nba_top_75.csv")
        print(graph_method)
    
    return playerstats_method
    
if __name__ == "__main__":
    main()
    
   # df = pd.read_csv("nba_top_75.csv")
    #print(df.query("MVP > 2"))
    #print(df.query("Name == \"LEBRON JAMES\""))