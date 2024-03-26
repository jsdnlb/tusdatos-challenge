import unittest
from bson import ObjectId
from mongomock import MongoClient
from api.controllers.legal_proceeding import delete_processes
from api.utils.exception_handler import exception_handler
from tests.test_utils import get_mock_process


class TestDeleteProcesses(unittest.TestCase):
    def setUp(self):
        self.client = MongoClient()
        self.db = self.client.my_database
        self.collection = self.db.legal_proceedings
        self.collection.insert_many(get_mock_process())

    def test_delete_processes_valid(self):
        process_ids = ["6602222d5a48ca0518a42451", "6602222d5a48ca0518a42452"]
        result = delete_processes(process_ids, mock_collection=self.collection)

        self.assertEqual(result["message"], "Processes deleted")
        self.assertEqual(result["deleted_count"], 2)

    def test_delete_processes_no_ids(self):
        with self.assertRaises(Exception) as context:
            delete_processes([], mock_collection=self.collection)

        self.assertEqual(str(context.exception), str(exception_handler("422_NO_ID")))

    def test_delete_processes_non_existing_ids(self):
        non_existing_process_ids = [
            "7602222d5a48ca0518a42452",
            "7602222d5a48ca0518a42452",
        ]
        with self.assertRaises(Exception) as context:
            delete_processes(non_existing_process_ids, mock_collection=self.collection)

        self.assertEqual(
            str(context.exception), str(exception_handler("404_NOT_FOUND"))
        )


if __name__ == "__main__":
    unittest.main()
