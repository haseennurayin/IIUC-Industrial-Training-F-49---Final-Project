import requests

def get_with_headers():
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    headers = {
        'User-Agent': 'My User Agent 1.0',
        'Accept': 'application/json'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        print("GET request with custom headers successful!")
        print(response.json())
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Connection Error: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
    except Exception as e:
        print(f"Unknown Error: {e}")

def post_with_authentication():
    url = 'https://jsonplaceholder.typicode.com/posts'
    data = {
        'title': 'foo',
        'body': 'bar',
        'userId': 1
    }
    headers = {
        'User-Agent': 'My User Agent 1.0'
    }
    auth = ('user', 'pass')
    
    try:
        response = requests.post(url, json=data, headers=headers, auth=auth)
        response.raise_for_status()
        print("POST request with authentication successful!")
        print(response.json())
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Connection Error: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
    except Exception as e:
        print(f"Unknown Error: {e}")

def main():
    print("Executing GET request with custom headers...")
    get_with_headers()
    print("\nExecuting POST request with authentication...")
    post_with_authentication()

if __name__ == "__main__":
    main()
