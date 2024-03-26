from typing import List
from api.db.database import database as db
from datetime import datetime
from bson import ObjectId
from api.utils.exception_handler import exception_handler

now = datetime.now()
legal_proceedings = db.legal_proceedings


def read_legal_proceeding(
    page: int,
    page_size: int,
    sort_by: str,
    order: str,
    search_field: str,
    search_value: str,
):
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    search_filter = {}
    if search_field and search_value:
        search_filter = {search_field: search_value}

    all_records = list(legal_proceedings.find(search_filter))

    if sort_by:
        reverse_order = True if order.lower() == "desc" else False
        all_records.sort(key=lambda x: x.get(sort_by, ""), reverse=reverse_order)

    paginated_records = all_records[start_index:end_index]
    cleaned_legal_proceedings = [
        {**process, "_id": str(process["_id"])} for process in paginated_records
    ]
    processes_ids = [str(process["_id"]) for process in paginated_records]
    count = legal_proceedings.count_documents({})

    return {
        "message": "List of processes",
        "pagination": {"total_processes": count, "page": page, "page_size": page_size},
        "processes_ids": processes_ids,
        "result": cleaned_legal_proceedings,
    }


def delete_process(process_id: str):
    object_id = ObjectId(str(process_id))
    existing_process = legal_proceedings.find_one({"_id": object_id})
    if existing_process:
        existing_process["_id"] = str(existing_process["_id"])
    else:
        raise exception_handler("404_NOT_FOUND")
    legal_proceedings.delete_one({"_id": object_id})
    return {
        "message": "Process deleted",
        "deleted": existing_process,
    }


def delete_processes(processes_ids: List[str]):
    if not processes_ids:
        raise exception_handler("422_NO_ID")
    object_ids = [ObjectId(process_id) for process_id in processes_ids]
    deleted_count = legal_proceedings.delete_many({"_id": {"$in": object_ids}})
    if deleted_count.deleted_count == 0:
        raise exception_handler("404_NOT_FOUND")

    return {
        "message": "Processs deleted",
        "deleted_count": deleted_count.deleted_count,
    }
