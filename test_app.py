import requests as r

def test_request_status():
    re = r.get('https://jsonplaceholder.typicode.com/posts/1')
    assert re.status_code == 200