import json

class centerDatabaseOperations:
    @staticmethod
    def read_centre_data() -> dict:
        with open('database/centers.json', 'r') as file:
            return json.load(file)

class databaseOperations:
    @staticmethod
    def read_users_database() -> dict:
        with open('database/users.json', 'r') as file:
            return json.load(file)
        
    @staticmethod
    def write_users_database(data: str) -> any:
        with open('database/users.json', 'w') as file:
            return json.dump(data, file, indent = 4)
        
    @staticmethod
    def register_user(
            username: str, name: str, password: str,
            address: str, Email: str, date: str = '', 
            vaccination_status: bool = False,
            dose_name: str = '', vaccination_location: str = '',
    ) -> bool:
        data = databaseOperations.read_users_database()
        data.update(
            {
                username + ':' + password :{
                    'name': name,
                    'VaccinationStatus': vaccination_status,
                    'Date': [date], 'VaccineName': dose_name,
                    'VaccinationLocation': vaccination_location,
                    'Address': address, 'E-Mail': Email,
                }
            }
        )
        return databaseOperations.write_users_database(data)

class Users:
    @staticmethod
    def login(username: str, password: str) -> bool:
        credentials = username + ":" + password
        return True if credentials in databaseOperations.read_users_database() else False

    @staticmethod
    def register(username, password, date, vaccination_status, dose, loc):
        credential = username + ":" + password
        if credential not in databaseOperations.read_users_database():
            return databaseOperations.register_user(username, password, date, vaccination_status, dose, loc)
        raise KeyError

class book_slot:
    @staticmethod
    def book(
        username: str, 
        password: str,
        vaccine: str,
        date: str,code: str
    ):
        with open('database/centers.json', 'r') as file:
            centerdata = json.load(file)
            if centerdata[code]['Available Slots'][date] <= 0:
                raise ValueError
            centerdata[code]['Available Slots'][date] -= 1
            centerdata[code]['AvailableDose'] = int(centerdata[code]['AvailableDose']) - 1
            with open('database/centers.json', 'w') as file:
                json.dump(centerdata, file, indent=4)

        credential = f"{username}:{password}"
        with open('database/users.json', 'r') as file:
            userdata = json.load(file)
            userdata[credential]['VaccinationStatus'] = True
            userdata[credential]['Date'] = [date]
            userdata[credential]['VaccinationLocation'] = code
            userdata[credential]['VaccineName'] = vaccine
            with open('database/users.json', 'w') as file:
                json.dump(userdata, file, indent=4)
        
        