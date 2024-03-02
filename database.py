import json

from sqlalchemy import create_engine, text
import sqlalchemy_access as sa_a
import sqlalchemy_access.pyodbc as sa_a_pyodbc


with open("config.json", encoding="utf-8") as config:
    data = json.load(config)
    SERVER = data["server"]
    DB_NAME = data["database"]
    USERNAME = data["username"]
    PASSWORD = data["password"]
    DRIVER = data["driver"]


class Database:
    def __init__(self) -> None:
        self.engine = create_engine(
            "mssql+pyodbc://{}:{}@{}/{}?DRIVER={}".format(
                USERNAME, PASSWORD, SERVER, DB_NAME, DRIVER
            )
        )

    def exec_command(self, sql_command: str, params=None) -> list:
        """takes sql command with paramater
        Connects to the database,  returns the result"""
        # create connection to the engine and execute the sql commands
        try:
            with self.engine.begin() as conn:
                try:
                    result = conn.execute(text(sql_command), params)
                    return result.fetchall()
                except Exception as e:
                    print(f"An error was generated: {e}")
        except Exception as e:
            print(f"An error was generated: {e}")

    def get_location(self) -> dict:
        sql_command = "EXEC LibraryLocation"
        location = {}
        result = self.exec_command(sql_command=sql_command)
        output_string = result[0][0]
        result = json.loads(output_string)

        for item in result:
            location_name = item["LocationShortName"].strip()
            location_id = item["LocationId"].strip()
            location[location_name] = location_id
        return location

    def get_asset(self, equipment_number) -> list:
        sql_command = "EXEC LibraryGetAsset @EquipmentCode=:equipment_no "
        parameters = {"equipment_no": equipment_number}

        return self.exec_command(sql_command, parameters)

    def issue_loan(self, equipment_id, location_id) -> None:
        sql_command = "EXEC LibraryCheckout @EquipmentId=:equipment_id,\
            @LocationId=:location_id"
        parameters = {"equipment_id": equipment_id, "location_id": location_id}

        self.exec_command(sql_command=sql_command, params=parameters)


if __name__ == "__main__":
    db = Database()
    location = db.get_location()
    print("why is it pring this")
