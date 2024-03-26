from bson import ObjectId


def get_mock_process():
    return [
        {
            "_id": ObjectId("6602222d5a48ca0518a42451"),
            "field": "value1",
            "process": "value1",
        },
        {
            "_id": ObjectId("6602222d5a48ca0518a42452"),
            "field": "value2",
            "process": "value2",
        },
        {
            "_id": ObjectId("6602222d5a48ca0518a42453"),
            "field": "value3",
            "process": "value3",
        },
        {
            "_id": ObjectId("6602222d5a48ca0518a42454"),
            "field": "value4",
            "process": "value4",
        },
    ]
