import server


def test_index():
    with server.app.test_client() as c:
        r = c.get("/")

    assert r.status_code == 200
    assert "<title>GUDLFT Registration</title>" in str(r.data)
