import unittest
from bson import ObjectId
from mongomock import MongoClient

from api.controllers.legal_proceeding import delete_process
from api.utils.exception_handler import exception_handler
from tests.test_utils import get_mock_process


class TestDeleteProcess(unittest.TestCase):
    def setUp(self):
        self.client = MongoClient()
        self.db = self.client.my_database
        self.collection = self.db.legal_proceedings_mock
        self.collection.insert_many(get_mock_process())

    def test_delete_existing_process(self):
        process_id = self.collection.find_one({})["_id"]
        result = delete_process(process_id, mock_collection=self.collection)

        self.assertEqual(result["message"], "Process deleted")
        self.assertEqual(result["deleted"]["_id"], str(process_id))

    def test_delete_non_existing_process(self):

        non_existing_process_id = str(ObjectId())
        with self.assertRaises(Exception) as context:
            delete_process(non_existing_process_id, mock_collection=self.collection)

        self.assertEqual(
            str(context.exception), str(exception_handler("404_NOT_FOUND"))
        )


if __name__ == "__main__":
    unittest.main()
