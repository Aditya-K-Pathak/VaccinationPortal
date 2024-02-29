import json

class databaseOperations:
    @staticmethod
    def read_admin_data() -> dict:
        with open('database/admin.json') as file:
            return json.load(file)
        
    @staticmethod
    def read_centre_data() -> dict:
        with open('database/centers.json', 'r') as file:
            return json.load(file)
        
    @staticmethod
    def write_center_data(data):
        with open('database/centers.json', 'w') as file:
            return json.dump(data, file, indent = 4)
        
class VaccinationCenter:

    @staticmethod
    def add_center(
        code: str, name: str,
        location: str, vaccine_name: str,
        opening_time: str, closing_time:str,
        available_doses: int
    ):
        data = databaseOperations.read_centre_data()
        data.update({
            code:{
                'Name': name,'Location':location,
                'Vaccine Name': vaccine_name,
                'Available Dose': available_doses,
                'Opening Time': opening_time,
                'Closing Time': closing_time,
            }
        })
        return databaseOperations.write_center_data(data)
    
    @staticmethod
    def update_center(
        code: str, name: str,
        location: str, vaccine_name: str,
        opening_time: str, closing_time:str,
        available_doses: int
    ):
        data = databaseOperations.read_centre_data()
        if code not in data:
            raise ValueError
        data.update({
            code:{
                'Name': name,'Location':location,
                'Vaccine Name': vaccine_name,
                'Available Dose': available_doses,
                'Opening Time': opening_time,
                'Closing Time': closing_time,
            }
        })
        return databaseOperations.write_center_data(data)
    
    @staticmethod
    def delete_center(
            code: str
    ):
        centers = databaseOperations.read_centre_data()
        centers.pop(code)
        return databaseOperations.write_center_data(centers)
    
    @staticmethod
    def get_all_centers() -> dict:
        return databaseOperations.read_centre_data()