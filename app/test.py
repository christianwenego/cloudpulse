import pytest
from app import app

# ── Configuration ─────────────────────────────────────
@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

# ── Tests ──────────────────────────────────────────────

def test_home(client):
    """Test que la page d accueil repond"""
    reponse = client.get("/")
    assert reponse.status_code == 200

def test_home_contenu(client):
    """Test que la reponse contient le bon message"""
    reponse = client.get("/")
    data = reponse.get_json()
    assert data["status"] == "ok"
    assert "message" in data

def test_health(client):
    """Test que le endpoint health repond"""
    reponse = client.get("/health")
    assert reponse.status_code == 200

def test_health_contenu(client):
    """Test que health retourne healthy"""
    reponse = client.get("/health")
    data = reponse.get_json()
    assert data["status"] == "healthy"

def test_metrics(client):
    """Test que les metriques repondent"""
    reponse = client.get("/metrics/system")
    assert reponse.status_code == 200

def test_metrics_contenu(client):
    """Test que les metriques contiennent cpu memoire disque"""
    reponse = client.get("/metrics/system")
    data = reponse.get_json()
    assert "cpu" in data
    assert "memoire" in data
    assert "disque" in data
    assert "uptime_secondes" in data
