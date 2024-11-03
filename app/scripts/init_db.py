from user_classes import User, Address, Tasks, TaskAssigments, TaskNotes
from session import Database
from config import config
import logging
import json
import uuid

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    try:
        logger.info("Connect to database")

        # This class managment commits, rollbacks and close session
        db = Database(config.database_url)

        with open("db.json", "r") as file:
            data = json.load(file)

            people = data["people"]
            tasks = data["tasks"]
            task_notes = data["task_notes"]
            task_assignments = data["task_assignments"]

            list_users = list()
            list_address = list()

            for user in people:
                user_obj = User(
                    id=user["id"],
                    user_name=user["user_name"],
                    first_name=user["first_name"],
                    last_name=user["last_name"],
                    email=user["email"],
                    address_id=user["id"],
                )

                address_obj = Address(
                    id=user["id"],
                    street=user["address"]["street"],
                    city=user["address"]["city"],
                    state=user["address"]["state"],
                    zip=user["address"]["zip"],
                )

                list_users.append(user_obj)
                list_address.append(address_obj)

            list_tasks = [
                Tasks(
                    id=task["id"],
                    title=task["title"],
                    details=task["details"],
                    completed=task["completed"],
                    priority=task["priority"],
                    date_created=task["date_created"],
                )
                for task in tasks
            ]

            list_assigments = [
                TaskAssigments(
                    id=task_assigment["id"],
                    task_id=task_assigment["task_id"],
                    user_id=task_assigment["person_id"],
                    accepted=task_assigment["accepted"],
                )
                for task_assigment in task_assignments
            ]

            list_notes = list()
            for task_note in task_notes:
                new_uuid = uuid.uuid4()

                if task_note["task_id"] != 0:
                    if task_note["person_id"] != 0:
                        new_note = TaskNotes(
                            id=new_uuid,
                            task_id=task_note["task_id"],
                            user_id=task_note["person_id"],
                            notes=task_note["notes"],
                        )

                        list_notes.append(new_note)

            db.insert_objects(list_address)
            logger.info("Address created")
            db.insert_objects(list_users)
            logger.info("Users created")
            db.insert_objects(list_tasks)
            logger.info("Tasks created")
            db.insert_objects(list_assigments)
            logger.info("Tasks Assigments created")
            db.insert_objects(list_notes)
            logger.info("Tasks Notes created")

    except Exception as e:
        logger.error(f"Error: {e}")


if __name__ == "__main__":
    logger.info("Creating initial data")
    main()
    logger.info("Initial data created")
