from api.db.database import database as db
from datetime import datetime

now = datetime.now()
legal_proceedings = db.legal_proceedings


def read_legal_proceeding(page: int, page_size: int):
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    all_records = [x for x in legal_proceedings.find()]
    paginated_records = all_records[start_index:end_index]
    cleaned_legal_proceedings = [
        {**process, "_id": str(process["_id"])} for process in paginated_records
    ]
    process_ids = [str(process["_id"]) for process in paginated_records]

    return {
        "message": "List of processes",
        "processes_ids": process_ids,
        "result": cleaned_legal_proceedings,
    }
