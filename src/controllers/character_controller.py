
from src.controllers.abstract_controller import AbstractController
from src.models.character_model import CharacterModel 
from datetime import datetime

class CharacterController(AbstractController):
    """
    CharacterController is responsible for managing character data in the database.
    It provides methods to create, read, update, and delete character records.
    It also handles the connection to the database and executes SQL queries.

    Methods
    -------
    #### create(character: CharacterModel) -> CharacterModel:
        Creates a new character in the database.
        
        Args:
            character (CharacterModel): The character object to be created.
            
        Returns:
            CharacterModel: The created character object with its ID and timestamps.

    #### delete(character_id: int) -> bool:
        Deletes a character from the database.
        
        Args:
            character_id (int): The ID of the character to be deleted.
            
        Returns:
            bool: True if the character was deleted successfully, False otherwise.

    #### get_all(order_by: str = "id") -> List[CharacterModel]:
        Gets all characters from the database.
        
        Args:
            order_by (str): The column to order by. Default is "id".
                            Accepts "id", "first_name", "last_name", "age", "lineage", "job".
                            
        Returns:
            List[CharacterModel]: A list of CharacterModel instances.
            
        Raises:
            ValueError: If the order_by parameter is not one of the accepted values.

    #### get(character_id: int) -> CharacterModel:
        Gets a character by ID.
        
        Args:
            character_id (int): The ID of the character to retrieve.
            
        Returns:
            CharacterModel: An instance representing the character with the given ID.
            
        Raises:
            ValueError: If the character_id is not found in the database.

    #### update(character: CharacterModel) -> CharacterModel:
        Updates a character in the database.
        
        Args:
            character (CharacterModel): The character object to be updated.
            
        Returns:
            CharacterModel: The updated character object with its timestamps.
    """
    def create(self, character: CharacterModel):
        """Create a new character in the database.
        ### Parameters
        - character (CharacterModel): The character object to create.
        ### Returns
        - CharacterModel: The created character object with its ID and timestamps.
        ### Raises
        - Exception: If there is an error during the creation process.
        """
        query = """
            INSERT INTO characters (first_name, last_name, age, lineage, job, image, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        params = (character.first_name, character.last_name,character.age, character.lineage,
                  character.job, character.image , datetime.now(), datetime.now())
        row_id = self.execute_insert(query, params)
        if row_id:
            character.id = row_id
            character.created_at = datetime.now()
            character.updated_at = datetime.now()
            return character
        return None
        
    def delete(self, character_id: int):
        """Delete a character from the database.
        ### Parameters
        - character_id (int): The ID of the character to delete.
        ### Returns
        - bool: True if the character was deleted successfully, False otherwise.
        ### Raises
        - Exception: If there is an error during the deletion process.
        """
        query = "DELETE FROM characters WHERE id = ?"
        params = (character_id,)
        try:
            self.execute_delete(query, params)
            # Check if the character was deleted successfully
            check_query = "SELECT * FROM characters WHERE id = ?"
            result = self.execute_query(check_query, params)
            if not result:
                print(f"Character with ID {character_id} deleted successfully.")
                self.close()
                return True
            else:
                print(f"Character with ID {character_id} still exists.")
                self.close()
                return False

        except Exception as e:
            print(f"Error deleting character: {e}")
            return False
    
    def get_all(self, order_by: str = "id"):
        """Get all characters from the database.
        ### Parameters
        - order_by (str): The column to order by. Default is "id". Accepts "id", "first_name", "last_name", "age", "lineage", "job".
        ### Returns
        - List[CharacterModel]: A list of CharacterModel instances representing all characters in the database.
        ### Raises
        - ValueError: If the order_by parameter is not one of the accepted values.
        """
        query = "SELECT * FROM characters"
        if order_by not in ["id", "first_name", "last_name", "age", "lineage", "job"]:
            raise ValueError("Invalid order_by parameter. Must be one of: id, first_name, last_name, age, lineage, job.")
        else:
            query += f" ORDER BY {order_by}"
        result = self.execute_query(query)
        return [CharacterModel(*row) for row in result]

    def get(self, character_id: int):
        """Get a character by ID.
        ### Parameters
        - character_id (int): The ID of the character to retrieve.
        ### Returns
        - CharacterModel: An instance of CharacterModel representing the character with the given ID.
        ### Raises
        - ValueError: If the character_id is not found in the database.
        """
        query = "SELECT * FROM characters WHERE id = ?"
        params = (character_id,)
        result = self.execute_query(query, params)
        if result:
            return CharacterModel(*result[0])
        else:
            raise ValueError(f"Character with ID {character_id} not found.")
    
    def update(self, character: CharacterModel):
        """Update a character in the database."""
        query = """
            UPDATE characters
            SET first_name = ?, last_name = ?, age = ?, lineage = ?, job = ?, image = ?, updated_at = ?
            WHERE id = ?
        """
        params = (character.first_name, character.last_name, character.age, character.lineage,
                  character.job, character.image, datetime.now(), character.id)
        self.execute_update(query, params)
        character.updated_at = datetime.now()
        return character