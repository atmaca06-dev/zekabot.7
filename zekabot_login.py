import requests

def login_to_site(url, payload):
    try:
        session = requests.Session()
        response = session.post(url, data=payload)
        return {"status": response.status_code}
    except Exception as e:
        return {"error": str(e)}