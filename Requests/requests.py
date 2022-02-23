import requests

#generate api_key on site https://favqs.com/api_keys and auth
api_key = "96d5d85c684c4a952b15c9e885166cf8"
auth_header = {"Authorization": f'Token token={api_key}'}


#create user
def create_user(login, email, password):

  data = {
    "user": {
      "login":      f"{login}",
      "email":      f"{email}",
      "password":   f"{password}"
    }
  }

  url = "https://favqs.com/api/users"

  response = requests.post(url, json=data, headers=auth_header).json()

  return response


def get_users(token, login):

  user_token = {"User_Token": f"{token}"}

  url_users = f"https://favqs.com/api/users/{login}"

  response = requests.get(url_users, headers={**auth_header, **user_token})

  return response.json()


def update_users(user_token, ols_login, new_login, new_email):

  header = {"User-Token": user_token}

  data = {
    "user": {
      "login": f"{new_login}",
      "email": f"{new_email}"
    }
  }

  update_url = f"https://favqs.com/api/users/{ols_login}"

  response = requests.put(update_url, json=data, headers={**header, **auth_header})

  return response.json()


def destroy_session(token):

  url_session = "https://favqs.com/api/session"

  response = requests.delete(url_session, headers={**auth_header, **{"User-Token": token}})

  return response.json()