import requests

def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad status codes
        users = response.json()
        return users

    except requests.RequestException as e:
        print("Error fetching data:", e)
        return []

def process_users(users):
    print(f"{'Name':<20} | {'Email':<25} | {'City'}")

    for user in users:
        name = user['name']
        email = user['email']
        city = user['address']['city']
        print(f"{name:<20} | {email:<25} | {city}")

def main():
    users = fetch_users()
    if users:
        process_users(users)

if __name__ == "__main__":
    main()
