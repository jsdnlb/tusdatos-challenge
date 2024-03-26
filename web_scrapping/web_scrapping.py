from concurrent.futures import ThreadPoolExecutor
import requests as r
import csv
import json

BASE_URL = "https://api.funcionjudicial.gob.ec"


def count_number_processes(id: str) -> int:
    url = f"{BASE_URL}/EXPEL-CONSULTA-CAUSAS-SERVICE/api/consulta-causas/informacion/contarCausas"
    payload = {
        "actor": {"cedulaActor": id, "nombreActor": ""},
        "demandado": {"cedulaDemandado": "", "nombreDemandado": ""},
        "recaptcha": "verdad",
    }
    res = r.post(url, json=payload)
    return res.text


def get_all_process_with_data(id: str, filename: str) -> dict:
    page_size = count_number_processes(id)

    url_processes = f"{BASE_URL}/EXPEL-CONSULTA-CAUSAS-SERVICE/api/consulta-causas/informacion/buscarCausas?page=1&size={page_size}"
    url_act = f"{BASE_URL}/EXPEL-CONSULTA-CAUSAS-SERVICE/api/consulta-causas/informacion/actuacionesJudiciales"

    payload = {
        "actor": {"cedulaActor": id, "nombreActor": ""},
        "demandado": {"cedulaDemandado": "", "nombreDemandado": ""},
        "recaptcha": "verdad",
    }
    list_data = []

    response = r.post(url_processes, json=payload)
    all_processes = response.json()

    for process in all_processes:
        data = {}
        if payload["actor"]["cedulaActor"]:
            process["type_process"] = "demandante"
        else:
            process["type_process"] = "demandado"
        data = process
        data["id_process"] = data.pop("id")
        all_details = r.get(
            f"{BASE_URL}/EXPEL-CONSULTA-CAUSAS-CLEX-SERVICE/api/consulta-causas-clex/informacion/getIncidenteJudicatura/{process['idJuicio']}"
        )
        details = all_details.json()
        data["details"] = details

        if details:
            for detail in details:
                payload_judicial_updates = {"aplicativo": "web"}
                payload_judicial_updates["idJuicio"] = process["idJuicio"]
                payload_judicial_updates["idJudicatura"] = detail["idJudicatura"]
                payload_judicial_updates["nombreJudicatura"] = detail[
                    "nombreJudicatura"
                ]
                for incidente in detail["lstIncidenteJudicatura"]:
                    payload_judicial_updates["idIncidenteJudicatura"] = incidente[
                        "idIncidenteJudicatura"
                    ]
                    payload_judicial_updates["idMovimientoJuicioIncidente"] = incidente[
                        "idMovimientoJuicioIncidente"
                    ]
                    payload_judicial_updates["incidente"] = incidente["incidente"]
                    all_judicial_updates = r.post(
                        url_act, json=payload_judicial_updates
                    )
                    a = all_judicial_updates.json()
                    data["judicial_updates"] = a
        list_data.append(data)

    file_path = f"{filename}.json"
    with open(file_path, "w") as file:
        json.dump(list_data, file)

    print("Data exportada exitosamente como JSON.")


print(get_all_process_with_data("0968599020001", "name"))
