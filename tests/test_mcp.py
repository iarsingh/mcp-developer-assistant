from fastapi.testclient import TestClient
from mcpx.main import app
client = TestClient(app)

def test_allow_and_approval():
    assert "github.list_pr" in client.get("/tools").json()["tools"]
    assert client.post("/call", json={"name": "github.list_pr", "arguments": {"q": "status"}}).json()["ok"] is True
    blocked = client.post("/call", json={"name": "github.list_pr", "arguments": {"cmd": "kubectl apply"}}).json()
    assert blocked["needs_approval"] is True and blocked["applied"] is False
