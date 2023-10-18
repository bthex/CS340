from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):

    def __init__(self, username, password):
        try:
            self.client = MongoClient('mongodb://%s:%s@nv-desktop-services.apporto.com:30483' % (username, password))
            self.database = self.client['AAC']
            self.collection = self.database['animals']
            
            print("Initialization successful")
        except Exception as e:
            print("An error occurred during initialization: ", e)

    # This method is used to create and add documents
    def create(self, newDoc  = None):
        # Check for document information
        if Newdata is None:
            raise Exception("Nothing to save, because data parameter is empty")
        
        # Attempt to create new document    
        newDocAdded = self.database.animals.insert(data)  # data should be dictionary
        if newDocAdded is None:
            raise Exception('Failed to add new document check data.')
            
    # This method is used to find documents
    def read(self, findData = None):
        if findData is None:
            raise Exception('\nERROR: No valid data was specified.')

        #Return documents that match filter
        return self.database.animals.find(findData, {'_id': False})
        
    # This method is used to update documents
    def update(self, filter, update):
        #Validate parameters
        if (filter is None):
            raise Exception('\nERROR: No valid filter was specified.')
        if (update is None):
            raise Exception('\nERROR: No valid changes were specified.')  
        
        #Update records based on specified parameters
        updated = this.db.animals.update_one(filter, update)
        if (updated is None):
            raise Exception('\nERROR: Failed to update document based on filter')
            
    # This method is used to delete documents
    def delete(self, removeFilter = None):
        # Check for a valid filter
        if removeFilter is None:
            raise Exception('\nERROR: No valid filter was specified.')
        
        #Delete records basd on filter
        deleted = this.db.animals.delete_many(removeFilter)
        if deleted is None:
            raise Exception('\nERROR: Failed to delete records based on filter.')
