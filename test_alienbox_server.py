import pytest
import threading
import time
import requests
import json
from alienbox_server import AlienBoxHandler
import http.server

PORT = 8001

@pytest.fixture(scope="module")
def server():
    server_address = ('', PORT)
    httpd = http.server.HTTPServer(server_address, AlienBoxHandler)
    server_thread = threading.Thread(target=httpd.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    
    # Wait for server to start
    time.sleep(1)
    
    yield httpd
    
    httpd.shutdown()
    httpd.server_close()

def test_health_check_options(server):
    response = requests.options(f"http://localhost:{PORT}/alienbox")
    assert response.status_code == 200

def test_generate_mock_json_d1(server):
    payload = {
        "input": "Test Song",
        "daw": "Ableton",
        "mode": "D1",
        "breakdown": "all"
    }
    response = requests.post(f"http://localhost:{PORT}/alienbox", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "Test Song" in data["ficha_tecnica"]["titulo"]
    assert data["midi_data"]["mode"] == "D1"

def test_generate_mock_json_d2(server):
    payload = {
        "input": "https://youtube.com/watch?v=dummy",
        "daw": "Logic Pro",
        "mode": "D2",
        "breakdown": "lowend"
    }
    response = requests.post(f"http://localhost:{PORT}/alienbox", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert len(data["midi_data"]["tracks"]) == 2  # lowend breakdown has 2 tracks
    assert data["midi_data"]["breakdown"] == "lowend"

def test_404_not_found(server):
    response = requests.post(f"http://localhost:{PORT}/unknown_route", json={"test": 123})
    assert response.status_code == 404
