# ROUTINES TO CREATE, WRITE AND READ ATHLETE DATA FILE
# ====================================================

# LIBRARIES AND MODULES

import json

# CLASS DEFINITIONS

class ProcessJsonFile():

    def __init__(self):
        pass



    def saveData(self, file, data):
        """Saves all athlete data to disk

        Args:
            file (str): Name of the file
            data (list): List of dictionaries
       
         Returns:
            tuple: Error code, Error message, detailed error message
        """
        
        with open(file, 'w') as fileToWrite: # w koska halutaan kirjoittaa json.
            json.dump(data, fileToWrite, indent=4) # Haetaan json kirjastosta dump. dump haluaa objektin ja fp eli tiedoston. 
        status = (0, 'Tallennus onnistui', 'All data saved successfully')   # Jos haluaa AINA vikaksi voi laittaa indent=4 eli 4 välin sisennys (sisentää tekstin helpommin luettavaksi)
        return status                             # Palauttaa statustiedon  # Sen jälkeen tallenna ja aja terminaali
       
    

    
    def readData(self, file):
        """Reads athlete data from file

        Args:
            file (str): Name of the file

        Returns:
            tuple: Error code, Error message, detailed error message, data
        """

        # Read previous athlete_data from disk
        with open(file, 'r') as fileToRead:  # 'r' = luetaan file
            athlete_data = json.load(fileToRead)
            message = 'OK'
            detailedMessage = 'Data read successfully from disk'
            data = (0, message, detailedMessage, athlete_data)
            return data
    
    def appendData(self, file, data):   # tiedostonimi ja tallennettava data(omakeksimä nimi)
        """Adds a new json object to the file
        
        Args:
            file (str): Name of the file
            data (dict): python dictionary containing data
        
        Returns:
            tuple: Error code, Error message, detailed error message
        """

        status = (0, 'Tallenus onnistui', 'Data saved successfully')
        return status

# PRELIMINARY TEST

if __name__ == "__main__":
    pass