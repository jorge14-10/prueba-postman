import requests

ENCRYPTED_VOUCHER = "LS0tLS1CRUdJTiBQR1AgTUVTU0FHRS0tLS0tDQpWZXJzaW9uOiBCb3VuY3lDYXN0bGUuTkVUIENyeXB0b2dyYXBoeSAobmV0Ni4wKSB2Mi4xLjErODUxZmVlZTAwOQ0KDQpoUUVNQTdTMFdMbUVaSHFCQVFmL1MwNXU0VUdMTURPbUtRbktUVndzbjB6TWRQeEc2ZmE5ZytJSjZxSXRkYUpaDQpCM3NhY2tWZFBRKzZ2Nm5VVHMwYXNieEd6ckgyU2QwYnpuc1pjSkIwaWRzcUcrK1orNUJxTVljdk0rOEM3WEZrDQpyMnRpcy9GMGFjOWhrVllVbzNQYndleGZsYkhNWDcrZWlqRXlRSGYyajg3UlhyaGxnUTZKY3V1MUlwTW1hdytoDQpreW1aQU5oOXFCRHlVTUZKdHlpdHpDUitjV2lWUnJISDJsTFlIbEt3eUdQdXloalczNDFPaWRMNnB5YWVyWmVIDQpiWmJsMmc2U0RCbTg0eFhuRzV6VEo3cXRuclRJbXRmSGhlVlV4NUp4U1lNMzBhQkQrMXpSd0NURU9hT0trSCtYDQordERlRzZUQ2FkK3hZeTlvNUd4dlRJNTZzR0xCbFBSV3JlZjdpYlBacnRJOUFRUkpmMi9sQnh3UFFjeUhRQmJ2DQpkTzBoVWI3L1lxM2Y0U1J4SXR4WXV5Rnp5M2RtL3FtbXA3dURsUFlHZXJKVllLTng3cFgxOHhRdGlPOUJyZz09DQo9YUNIRw0KLS0tLS1FTkQgUEdQIE1FU1NBR0UtLS0tLQ0K"
ENCRYPTED_PIN = "LS0tLS1CRUdJTiBQR1AgTUVTU0FHRS0tLS0tDQpWZXJzaW9uOiBCb3VuY3lDYXN0bGUuTkVUIENyeXB0b2dyYXBoeSAobmV0Ni4wKSB2Mi4xLjErODUxZmVlZTAwOQ0KDQpoUUVNQTdTMFdMbUVaSHFCQVFmL1V5Q0V0Q1FscEJlZVJIMG1BZ2pWT3ZUSnNxNm1LR1FtS2p5Zit0d3pPY1JSDQo3SHVZYWxOb3l5SXFsck4vbm1SaHR5K0lrZ0o3dDM2aXI0WVR3Wm1qVDVrMUhvVXdqZ2ZaMnBUUUdxdkNUSkx4DQpPUkg2YjAvQ3IyVkFveG9DVndoUlBPZlNRWTJ5aVlwbktISTNRNFZjcDVLU3p5b0JTMjI2UllmREo3NGF5SVZFDQo5MkJpZzdLZVlPeHZ4aXlUNHdBYittNHBUTTAxSmQwTU1lVVBBcSsrdkFEVlhUK3lTeFFiY0FJT0lQd1ZmMHNuDQozWnZpRmFEU3VNdWNGVDNackMzVnBPY1JKZ2RHS3VOU1Z1YUE4TkppNldWeEFNbmQrZllCRDlkOElOQ3p5WXVmDQpaYU9KelVqUS85RFRYSUJuYmw4ZkpPME1UZEZnQkNPU3RETmNzRUU3Y2RJekFWd0FwK3VyR21UNmpFZ3RDTmc1DQpTbnYrazBQSXVRZjdqNzNDelFidW1BN01UUnZkVy92MmYvYjFEQjV0MTlvdDlpQlUNCj1Da05KDQotLS0tLUVORCBQR1AgTUVTU0FHRS0tLS0tDQo="

#Variables generales
BASE_URL = "https://api-payments-qa.avtest.ink"
OCP_APIM_SUBSCRIPTION_KEY = "f80b16f56a3b4a4da66eb649178bbe9e"

#Dominio para solicitar el token
DOMINIO_TOKEN = "pendiente"

#Payload del token
PAYLOAD_TOKEN = {
    "grant_type": "pendiente",
    "client_id": "pendiente",
    "client_secret": "pendiente",
    "resource": "pendiente"
}

#Headers para la solicitud del token
HEADERS_TOKEN = {
    "Content-Type": "application/x-www-form-urlencoded"
}

#Generar el token
def get_token():
    response = requests.post(DOMINIO_TOKEN, data=PAYLOAD_TOKEN, headers=HEADERS_TOKEN)
    response.raise_for_status()
    access_token = response.json().get("access_token")
    return access_token

#Creacion del voucher
def create_voucher(access_token):
    url = f"{BASE_URL}/api_qwikcilver_in/createVoucher"
    headers = {
        "Ocp-Apim-Subscription-Key": OCP_APIM_SUBSCRIPTION_KEY,
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json;charset=UTF-8"
    }
    payload = {
        "create-voucher": {
            "channel": "AVCOM",
            "number-of-cards": "1",
            "reference-number": "CZ011",
            "group-name": "AV Refund/ Payment feedback",
            "amount": "100000",
            "currency": "COP",
            "carrier": "AV",
            "agent": "132",
            "office-id": "BOGAVL3",
            "first-name": "Gregory",
            "last-name": "Isakov",
            "email": "santiago.apellido@gmail.es",
            "mobile": "3107898787"
        }
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    print("Voucher creado")
    return response.json()

#Validar la respuesta de creacion del voucher
def create_voucher_validate_response(data_response_voucher):
    response_fields = [
        "transaction-id", "batch-number", "cards"
    ]
    response_fields_card = [
        "approval-code", "response-code", "response-message",
        "voucher", "card-status", "expiry-date", "balance",
        "pre-balance", "currency-code", "transferable", "reusable",
        "activation-date", "notes"
    ]

    data_response = data_response_voucher.get("response-createvoucher", {})
    response = [i for i in response_fields if i not in data_response]

    if response:
        print(f"Falta campos de la respuesta principal(raiz): {response}")
        return False

    data_response_cards = data_response["cards"][0]
    response_cards = [i for i in response_fields_card if i not in data_response_cards]
    if response_cards:
        print(f"Falta campos de la respuesta cards: {response_cards}")
        return False

    print(f"La respuesta de la creacion del voucher es valida: {data_response}")
    return True

#Reload del voucher
def reload_voucher(token, voucher, pin):
    url = f"{BASE_URL}/api_qwikcilver_in/reloadVoucher"
    headers = {
        "Authorization": f"Bearer {token}",
        "Ocp-Apim-Subscription-Key": OCP_APIM_SUBSCRIPTION_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "reload": {
            "channel": "AVCOM",
            "reference-number": "test-reload",
            "cards": [
                {
                    "voucher": voucher,
                    "pin": pin,
                    "currency": "COP",
                    "amount": "500",
                    "carrier": "AV",
                    "agent": "Avianca",
                    "office-id": "AirlineOffice1",
                    "beneficiaries": [
                        {
                            "first-name": "Test",
                            "last-name": "Test"
                        }
                    ]
                }
            ]
        }
    }

    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    print("Voucher recargado correctamente")
    return response.json()

#Validar la respuesta del reload
def reload_voucher_validate_response(data_response_reload_voucher):
    response_fields = [
        "transaction-id", "batch-number", "cards"
    ]
    response_fields_card = [
        "response-code", "response-message",
        "card-status", "card-type", "expiry-date", "balance", "activation-amount",
        "pre-balance", "transaction-amount", "currency", "activation-date",
        "card-group", "issuer-name", "transaction-date", "approval-code"
    ]

    data_response = data_response_reload_voucher.get("response-reload", {})
    response = [i for i in response_fields if i not in data_response]

    if response:
        print(f"Falta campos de la respuesta principal(raiz): {response}")
        return False

    data_response_cards = data_response["cards"][0]
    response_cards = [i for i in response_fields_card if i not in data_response_cards]
    if response_cards:
        print(f"Falta campos de la respuesta cards: {response_cards}")
        return False

    print(f"La respuesta del reload del voucher es valida: {data_response}")
    return True

#Retirar saldo
def preauth_balance(access_token):
    url = f"{BASE_URL}/api_qwikcilver_in/preauth"
    headers = {
        "Ocp-Apim-Subscription-Key": OCP_APIM_SUBSCRIPTION_KEY,
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    payload = {
        "preauth": {
            "channel": "AVCOM",
            "reference-number": "TESTNIC",
            "cards": [
                {
                    "voucher": ENCRYPTED_VOUCHER,
                    "pin": ENCRYPTED_PIN,
                    "currency": "GBP",
                    "amount": "1432305",
                    "carrier": "AV",
                    "agent": "Avianca",
                    "office-id": "AirlineOffice1",
                    "beneficiaries": [
                        {
                            "first-name": "Test",
                            "last-name": "Test"
                        }
                    ]
                }
            ]
        }
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()

#Validar la respuesta del preauth_balance
def preauth_balance_response(preauth_balance):
    response_fields = [
        "transaction-id", "batch-number", "cards"
    ]
    response_fields_card = [
        "response-code", "response-message", "approval-code",
        "card-status", "card-type", "card-group", "balance",
        "preauthcode", "currency-code", "currency-rate", "currency-converted"
    ]

    data_response = preauth_balance.get("response-preauth", {})
    response = [i for i in response_fields if i not in data_response]


    if response:
        print(f"Falta campos de la respuesta principal(raiz): {response}")
        return False

    data_response_cards = data_response["cards"][0]
    response_cards = [i for i in response_fields_card if i not in data_response_cards]
    if response_cards:
        print(f"Falta campos de la respuesta cards: {response_cards}")
        return False

    print(f"La respuesta del preauth_balance es valida: {data_response}")
    return True


if __name__ == "__main__":
    try:
        token = get_token()
        voucher_response = create_voucher(token)
        if not create_voucher_validate_response(voucher_response):
            raise Exception("Fallo la respuesta de creacion del voucher")

        reload_response = reload_voucher(token, ENCRYPTED_VOUCHER, ENCRYPTED_PIN)
        reload_voucher_validate_response(reload_response)

        preauth_response = preauth_balance(token)
        preauth_balance_response(preauth_response)

    except requests.HTTPError as e:
        print(f"Error HTTP: {e.response.status_code} - {e.response.text}")


