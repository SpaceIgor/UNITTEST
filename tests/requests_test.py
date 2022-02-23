from Requests.requests import get_users, create_user, update_users, destroy_session
from unittest import TestCase, main
from User.user import User


class Parent:

    user = User.default_users()

    data = create_user(user.login, user.email, user.password)

    user_token = data.get("User-Token")

    get_response = get_users(user_token, user)

    get_login = get_response['login']
    get_email = get_response['account_details']['email']


class CreateUserTest(TestCase, Parent):

    def test_auth(self):

        self.assertEqual(self.user.login, self.get_login)

        self.assertEqual(self.user.email.lower(), self.get_email)


class UpdateUserTest(TestCase, Parent):

    new_user_data = User.default_users()

    new_login = "deftestlogin"
    new_email = "qwevova@gmail.com"

    update_user_data = update_users(Parent.user_token, new_login, new_email, Parent.get_login)

    get_update_users = get_users(Parent.user_token, new_login)

    if update_user_data['message'] == 'User successfully updated.':

        def test_update(self):

            self.assertEqual(self.new_login, self.get_update_users['login'])

            self.assertEqual(self.new_email.lower(), self.update_user_data['account_details']['email'])
    else:
        raise Exception('User was not updated')

    print(destroy_session(Parent.user_token)['message'])
    

if __name__ == "__main__":
    main()