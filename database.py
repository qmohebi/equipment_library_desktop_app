import json

from sqlalchemy import create_engine, text
import sqlalchemy_access as sa_a
import sqlalchemy_access.pyodbc as sa_a_pyodbc

from cryptography.fernet import Fernet


with open("config.json", encoding="utf-8") as config:
    data = json.load(config)
    SERVER = data["server"]
    DB_NAME = data["database"]
    USERNAME = data["username"]
    pwd = data["password"]
    DRIVER = data["driver"]

# Decode the password.
key = b"p7JzAptU00KJFTT30ezqTr0_j0YW30UZVH57wnscOwU="
cipher_suite = Fernet(key)
encrypted_pwd = pwd.encode()
byte_pwd = cipher_suite.decrypt(encrypted_pwd.decode())

PASSWORD = byte_pwd.decode("utf-8")


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

    def get_mpce_personnel(self) -> dict:
        personal_query = "EXEC LibraryAppUsers"
        result = self.exec_command(personal_query)

        # convert tuple to string so it can be loaded to json and parsed
        result_string = f"[{result[0][0]}]"
        return json.loads(result_string)

    def create_job(
        self,
        equipment_id: str,
        job_type_id: str = None,
        job_status_id: str = None,
        reported_fault: str = None,
        tech_id: str = None,
        user_id: str = None,
        taken_by_id: str = None,
        work_end_date: str = None,
        work_done: str = None,
        visual_inspection: bool = None,
        est: bool = None,
        function_check: bool = None,
        battery_replaced: bool = None,
        battery_checked: bool = None,
        create_job: bool = None,
    ) -> None:
        """update the loan and create acceptance job"""

        sql_command = """
        SET NOCOUNT ON;
        DECLARE @out int;
        EXEC LibraryCreateJob
        @EquipmentId=:equipment_id,
        @JobTypeId=:job_type_id,
        @JobStatusId=:job_status_id,
        @ReportedFault=:reported_fault,
        @WorkEndDate=:workend_date,
        @TechnicianId=:technician_id,
        @TakenById=:taken_by_id,
        @WorkDone=:workdone,
        @UserId=:user_id,
        @VisualInspection=:visual_inspect,
        @ElectricalSafetyTest=:est,
        @FunctionCheck=:funct_check,
        @BatteryReplaced=:batt_replaced,
        @BatteryChecked=:batt_checked,
        @CreateJob=:create_job,
        @JobNumber = @out OUTPUT;
        SELECT @out AS job_number;
        """
        parameters = {
            "equipment_id": equipment_id,
            "job_type_id": job_type_id,
            "job_status_id": job_status_id,
            "reported_fault": reported_fault,
            "workend_date": work_end_date,
            "technician_id": tech_id,
            "taken_by_id": taken_by_id,
            "workdone": work_done,
            "user_id": user_id,
            "visual_inspect": visual_inspection,
            "est": est,
            "funct_check": function_check,
            "batt_replaced": battery_replaced,
            "batt_checked": battery_checked,
            "create_job": create_job,
        }

        with self.engine.begin() as conn:
            result = conn.execute(text(sql_command), parameters).scalar()
            return result


if __name__ == "__main__":
    db = Database()
    # db.create_job(
    #     equipment_id="5F96806AEDDE45ADA9717BA14604665C                  ",
    #     job_type_id="STG2005061300001",
    #     job_status_id="STG2005071800000",
    #     reported_fault="Test",
    #     tech_id="4641D85257D046CABB36FB7A575DECC2                  ",
    #     user_id="962A1467-EC25-42AE-9F86-9F572652C4E5",
    #     create_job=True,
    # )
