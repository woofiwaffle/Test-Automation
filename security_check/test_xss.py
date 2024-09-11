import requests
import pytest

@pytest.mark.parametrize("url", [
    "https://opensource-demo.orangehrmlive.com/web/index.php",
])
def test_xss(url):
    payloads = [
        "<script>alert('XSS')</script>",
        "<img src='x' onerror='alert(1)'>",
        "<svg onload=alert('XSS')>",
        "javascript:alert('XSS')"
    ]

    for payload in payloads:
        test_url = f"{url}?search={payload}"
        response = requests.get(test_url)
        if payload in response.text:
            print(f"Possible XSS found with payload: {payload}")
        else:
            print(f"No XSS with payload: {payload}")
