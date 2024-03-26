import unittest
from api.controllers.legal_proceeding import read_legal_proceeding
from mongomock import MongoClient

client = MongoClient()
db = client.my_database
collection = db.legal_proceedings
collection.insert_many(
    [
        {"_id": 1, "field": "value1", "process": "value1"},
        {"_id": 2, "field": "value2", "process": "value2"},
        {"_id": 3, "field": "value3", "process": "value3"},
        {"_id": 4, "field": "value4", "process": "value4"},
    ]
)


class TestReadLegalProceeding(unittest.TestCase):
    def test_read_legal_proceeding(self):
        result = read_legal_proceeding(
            page=1,
            page_size=2,
            sort_by=None,
            order="asc",
            search_field=None,
            search_value=None,
            mock_collection=collection,
        )

        self.assertDictEqual(
            result,
            {
                "message": "List of processes",
                "pagination": {"total_processes": 4, "page": 1, "page_size": 2},
                "processes_ids": ["1", "2"],
                "result": [
                    {"_id": "1", "field": "value1", "process": "value1"},
                    {"_id": "2", "field": "value2", "process": "value2"},
                ],
            },
        )

    def test_read_legal_proceeding_pagination(self):
        result = read_legal_proceeding(
            page=2,
            page_size=1,
            sort_by=None,
            order="asc",
            search_field=None,
            search_value=None,
            mock_collection=collection,
        )
        self.assertEqual(result["pagination"]["page"], 2)
        self.assertEqual(len(result["result"]), 1)
        self.assertListEqual(
            result["result"], [{"_id": "2", "field": "value2", "process": "value2"}]
        )

    def test_read_legal_proceeding_sorting(self):
        result_asc = read_legal_proceeding(
            page=1,
            page_size=3,
            sort_by="field",
            order="asc",
            search_field=None,
            search_value=None,
            mock_collection=collection,
        )
        result_desc = read_legal_proceeding(
            page=1,
            page_size=3,
            sort_by="field",
            order="desc",
            search_field=None,
            search_value=None,
            mock_collection=collection,
        )
        self.assertEqual(result_asc["result"][0]["_id"], "1")
        self.assertEqual(result_desc["result"][0]["_id"], "4")

    def test_read_legal_proceeding_search_field(self):
        result = read_legal_proceeding(
            page=1,
            page_size=10,
            sort_by=None,
            order="asc",
            search_field="field",
            search_value="value3",
            mock_collection=collection,
        )
        self.assertEqual(result["pagination"]["page"], 1)
        self.assertEqual(len(result["result"]), 1)
        self.assertListEqual(
            result["result"], [{"_id": "3", "field": "value3", "process": "value3"}]
        )

    def test_read_legal_proceeding_search_process(self):
        result = read_legal_proceeding(
            page=1,
            page_size=10,
            sort_by=None,
            order="asc",
            search_field="process",
            search_value="value1",
            mock_collection=collection,
        )
        self.assertEqual(result["pagination"]["page"], 1)
        self.assertEqual(len(result["result"]), 1)
        self.assertListEqual(
            result["result"], [{"_id": "1", "field": "value1", "process": "value1"}]
        )


if __name__ == "__main__":
    unittest.main()
