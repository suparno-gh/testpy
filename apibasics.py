import requests

def fetch_user_data():
    url="https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response=requests.get(url)
    data=response.json()

    if data["statusCode"]==200 and "data" in data:
        user=data.get("data",{})
        name=user.get("name",{})
        first_name=name.get("first","<unknown>")
        last_name=name.get("last","<unknown>")
        gender=user.get("gender","<unknown>")
        return first_name, last_name, gender
    else:
        raise Exception("Failed to fetch user data")
    
def main():
    try:
        fn,ln,g = fetch_user_data()
        print(f"Name : {fn} {ln}")
        print(f"Gender : {g}")
    except Exception as e:
        print(str(e))

if __name__=="__main__":
    main()