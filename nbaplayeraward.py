from argparse import ArgumentParser

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
            Sets attribute, nbaplayers, to an empty list.
        """
        self.nbaplayers = {}
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip().split("\t")
                self.nbaplayers[line[0]] = line[1:]
                
                #split_test = line.strip().split("\t")
                #self.nbaplayers[split_test[0]] = int(split_test[1]),int(split_test[2]),int(split_test[3]),int(split_test[4]),int(split_test[5])
    
    def playerstats(self, name):
        """

        Args:
           
        """
        if name.upper() not in self.nbaplayers:
            raise KeyError("NBA Player not on the Top 75 Team.")
        else:
            name = name.upper()
            print(f"{name} and his accolades: MVP: {self.nbaplayers[name][0]}, DPOY: {self.nbaplayers[name][1]}, Champion: {self.nbaplayers[name][2]}, FMVP: {self.nbaplayers[name][3]}, Scoring Title: {self.nbaplayers[name][4]}")
            
                    
    def statsonly(self, mvp, champion, fmvp, scoring_title):
        """The statsonly method will look at specifcally all the stats seeing the most
        of a specific stat that the user would like to see. This method allows for the
        user to answer the question of the 75 players on this anniversary team, what
        is the most common award of all these players.

        Args:
            mvp (int): The number of MVP awards an NBA player has received
            champion (int): The number of championships an NBA player 
            has received.
            fmvp (int): The number of Finals MVP awards an NBA 
            player has received.
            scoring_title (int): The number of scoring titles an NBA player 
            has received.
        """
        
def compare(player1, player2, stats):
    """The compare method is a method that will be used in order for the user
    of our program to compare two players and their different statistics being
    able to determine who is the Greatest of All Time according to the NBA
    75th Anniversary team. 

    Args:
        player1 (str): The name of the first player the user wants to use 
        to compare to player 2. 
        player2 (str): The name of the second player the user wants to use
        to compare to player 1.
        stats (bool): If one player has more stats (awards) than the other
        player it will return the result (better player) of the two individuals.
        
    Returns:
        str: It will return a string stating who the better player is between
        player 1 and player 2. 
    """
    
def main(file, name, mvp, champion, fmvp, scoring_title, name2):
    """Displays the stats of an NBA player or comparing two NBA players,
    using the information from the file.

    Args:
        file (str): The path to the file used for this program.
        name (str): The name of the NBA player.
        mvp (int): The number of MVPs of that NBA player.
        champion (int): The number of championships of that NBA player.
        fmvp (int): The number of Finals MVPs of that NBA player.
        scoring_title (int): The number of scoring titles of that NBA
        player.
        name2 (str): The name of the second NBA player to compare. 
    """
    
def parse_args(arglist):
    """Parse command-line arguments.

    Args:
    
    """
  
a = Database("nbaplayerawards.txt")  
if __name__ == "__main__":
    a.playerstats("stephen curry")