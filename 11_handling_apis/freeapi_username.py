import requests

def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()
    if data['success'] and "data" in data: 
        username = data['data']['name']
        loc = data['data']['location']
        return username['title'] + '. ' + username['first'] + ' ' + username['last'], loc['country']
    else:
        raise Exception("Failed to fetch username")

def main():
    try:
        username, country = fetch_random_user_freeapi()
        print(f'Username : {username}')
        print(f'Country : {country}')
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()

