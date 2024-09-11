import requests
import pytest

@pytest.mark.parametrize("url", [
    "https://opensource-demo.orangehrmlive.com/web/index.php",
])
def test_sql_injection(url):
    payloads = [
        "' OR '1'='1",
        '" OR "1"="1',
        "' OR 1=1--",
        '" OR 1=1--',
        "' OR 'a'='a",
        '" OR "a"="a',
    ]

    for payload in payloads:
        test_url = f"{url}?id={payload}"
        response = requests.get(test_url)
        if "sql" in response.text.lower() or response.status_code == 200:
            print(f"Possible SQL Injection found with payload: {payload}")
        else:
            print(f"No SQL Injection with payload: {payload}")
