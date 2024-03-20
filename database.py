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

    def get_mpce_personnel(self) -> dict:
        personal_query = "EXEC LibraryAppUsers"
        result = self.exec_command(personal_query)

        # convert tuple to string so it can be loaded to json and parsed
        result_string = f"[{result[0][0]}]"
        return json.loads(result_string)

    def return_load(
        self,
        job_type_id: str,
        job_status_id: str,
        equipemnt_id: str,
        reported_fault: str,
        work_end_date: str,
        tech_id: str,
        work_done: str,
        user_id: str,
        visual_inspection: bool = None,
        est: bool = None,
        function_check: bool = None,
        battery_replaced: bool = None,
        battery_checked: bool = None,
        create_job: bool = None,
    ) -> None:
        """update the loan and create acceptance job"""

        sql_command = """EXEC LibraryCreateJob\
        @JobTypeId=:job_type_id,\
        @JobStatusId=:job_status_id,\
        @EquipmentId=:equipment_id,\
        @ReportedFault=:reported_fault,\
        @WorkEndDate=:workend_date,\
        @TechnicianId=:technician_id,\
        @WorkDone=:workdone,\
        @UserId=:user_id,\
        @VisualInspection=:visual_inspect,\
        @ElectricalSafetyTest=:est,\
        @FunctionCheck=:funct_check,\
        @BatteryReplaced=:batt_replaced,\
        @BatteryChecked=:batt_checked,\
        @CreateJob=:create_job,\
        """
        parameters = {
            "job_type_id": job_type_id,
            "job_status_id": job_status_id,
            "equipment_id": equipemnt_id,
            "reported_fault": reported_fault,
            "workend_date": work_end_date,
            "technician_id": tech_id,
            "workdone": work_done,
            "user_id": user_id,
            "visual_inspect": visual_inspection,
            "est": est,
            "funct_check": function_check,
            "batt_replaced": battery_replaced,
            "batt_checked": battery_checked,
            "create_job": create_job,
        }


if __name__ == "__main__":
    db = Database()
    location = db.get_mpce_personnel()
    print(location)

