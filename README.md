# Web-Authentication

## Contents

*   [Normal Easy Auithorization Server](#Normal-Easy-Auithorization-Server)
    *   [Important URLs](#Important-URLs)
    *   [How To Use Our API](#How-To-Use-Our-API)
*   [OAuth2 Auithorization Server](#OAuth2-Auithorization-Server)



We have built two types of authorization systems. One is JWT authorization which has some flaws and back lags.
Another one is industry standard OAuth2 Service. Feel free to use any of them.

## Normal Easy Auithorization Server
At first this is version 1.1 which is live. There can be more changes in api of later versions

### Important URLs
First Important URL is the Registration API URL:
```
https://codexauthv2.onrender.com/api/register/
```
Next URL is the Login API URL:
```
https://codexauthv2.onrender.com/api/login/
```
Then the updating of profile is accomodated with the following URL:
```
https://codexauthv2.onrender.com/api/update-profile/
```
The last URL is if someone wants to delete the user profile:
```
https://codexauthv2.onrender.com/api/delete/
```


### How To Use Our API
This API system is easy to use APIs. There can be small changes time to time. But the format is fixed for calling. Most of the fields which are mandatory will be mentioned with a *. Other optional fields can be ommited from the request body.

### First API for Register
![image](https://github.com/javedcoding/CODEXAuthenticationPannel/assets/59325753/502cb9b6-64fa-4367-9eee-3011ed84fe48)

Format is below for the POST request:
```
{
    "username": "Anonymous",
    "email": "mashnunul.huq@stud.fra-uas.de",
    "password": "Human055",
    "role": "Base User",
    "provider": "infosys"
}
```
username*:- Provide the username to be used while login
email*:- Provide the email to be used while registering and a confirmation will come to this email if its correct.
password*:- Provide a password
role:- Provide user role between Basic User, Admin, Super Admin
provider:- Provider details which is upto 50 characters long

A response will come up like the below

![image](https://github.com/javedcoding/CODEXAuthenticationPannel/assets/59325753/180c1604-bd16-43e5-a29a-a739c98bb590)


```
{
"message":"User registered successfully!! Please keep the token in a safe place as it will not be shown again.",
"username":"Anonymous",
"email":"mashnunul.huq@stud.fra-uas.de",
"role":"Base User",
"token":"527cebf7c984a9ba58fbf7bb3304ae111dadabdf"}
```

Important you will need the token to pass while updating profile and deleting profile so save it in your database or somewhere else.

### Second API for Login
![image](https://github.com/javedcoding/CODEXAuthenticationPannel/assets/59325753/943177b7-ae5a-4115-8a2e-12fd2d0bb754)


Format is below for the POST request:
```
{
    "username": "Anonymous",
    "password": "Human055"
}
```
username*:- Provide the username used while registering
password*:- Provide a password used while registering

A Response will be provided just like below:
![image](https://github.com/javedcoding/CODEXAuthenticationPannel/assets/59325753/60c1b910-47ee-4dab-9962-264622b25f2c)

```
{
    "message": "Login successful. User data retrieved successfully!!",
    "user-account-details": {
        "username": "Anonymous",
        "first_name": null,
        "last_name": null,
        "email": "mashnunul.huq@stud.fra-uas.de",
        "role": "Base User",
        "provider": "infosys",
        "registration_datetime": "2024-01-18T12:42:43.281427Z",
        "last_login": "2024-01-18T12:51:15.831999Z",
        "is_active": true
    },
    "phone": null,
    "address": null,
    "city": null,
    "state": null,
    "zip": null,
    "country": null
}
```
If token is changed there will be a token field also which is required for Updating Profile or Deleting Profile
### Third API for Update-Profile

Use in the PUT request Header this key and value:
![image](https://github.com/javedcoding/CODEXAuthenticationPannel/assets/59325753/6100abec-dc6d-40a9-850d-c911dc96af90)

```
Authorization
Token 527cebf7c984a9ba58fbf7bb3304ae111dadabdf
```


Format for the body of PUT request:
![image](https://github.com/javedcoding/CODEXAuthenticationPannel/assets/59325753/04c0bc37-3b14-4625-aeed-eaf574f0676f)

```
{
    "first_name": "Mashnunul",
    "last_name": "Huq",
    "phone": "123123",
    "city": "Frankfurte",
    "addresse": "ben-gurion-ring 50",
    "state": "hessen",
    "zip": "60422",
    "roll": "Super Admin",
    "Provider": "Audi"

}
```

Response of the API:
![image](https://github.com/javedcoding/CODEXAuthenticationPannel/assets/59325753/2a5ecd8c-73cf-4b33-a4f0-4b4f787b4483)

```
{
    "message": "Profile updated successfully!!!",
    "user": {
        "email": "mashnunul.huq@stud.fra-uas.de",
        "first_name": "Mashnunul",
        "last_name": "Huq",
        "role": "Base User",
        "provider": "infosys",
        "phone": "123123",
        "address": null,
        "city": "Frankfurte",
        "state": "hessen",
        "zip": "60422",
        "country": null
    }
}
```

### Last API for Deleting Profile
Use in the PUT request Header this key and value:
![image](https://github.com/javedcoding/CODEXAuthenticationPannel/assets/59325753/2ff0a0e6-daf6-456d-b95a-aaf0d668d3fe)

```
Authorization
Token 527cebf7c984a9ba58fbf7bb3304ae111dadabdf
```


Format for the body of POST request:
![image](https://github.com/javedcoding/CODEXAuthenticationPannel/assets/59325753/18aca9d6-08d6-4b03-8a0b-6ef25732859d)

```
{
    "username": "Anonymous",
    "email": "mashnunul.huq@stud.fra-uas.de",
    "password": "Human055"
}
```

Response of the API:
![image](https://github.com/javedcoding/CODEXAuthenticationPannel/assets/59325753/6b70bd89-d149-46c9-95ca-2912fbb5d335)

```
{
    "message": "User deleted successfully"
}
```

## OAuth2 Authorization Server
This is an industry standard authorization system. Oauth2 is implemented aith PKCE type Authorization Code. This is stable version 2.0.

### Step 1: Registering the Application
First you need to register the application. The Developer of the application is responsible registering his/her
application. For that you need to go to the following URL:
```
https://codex-auth.azurewebsites.net/auth/applications/register
```
Remember before pressing registering button you need to copy the Client ID and Client Secret and redirect url. You will
need them later. The following picture shows the registering page

**_Note: The redirect url shouldn't be behind any protected uri._**

![Application Registering](https://github.com/javedcoding/CODEXAuthenticationPannel/blob/ayan_forked_hung/readme_pics/register.png)

### Step 2: Generating Access & Auth Token (Create an OAuth2 Client)

Here are some tutorials from the web on how to create a OAuth2 Client. You can follow any of them to get a glimpse of
how to create a OAuth2 Client.

1. [NodeJS Tutorial](https://blog.bitsrc.io/step-by-step-guide-to-implementing-oauth2-in-a-node-js-application-89c7e8d202bd)
2. [Django](https://songrgg.github.io/programming/django-oauth-client-setup/)

**_Note: You'll need to create a code verifier and code challenge. Here is a python code and Js code to generate them
they are not mentioned in all the tutorials_**

```python
import random
import string
import base64
import hashlib

code_verifier = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(43, 128)))

code_challenge = hashlib.sha256(code_verifier.encode('utf-8')).digest()
code_challenge = base64.urlsafe_b64encode(code_challenge).decode('utf-8').replace('=', '')
```

You'll need to add the code_challenge when requesting the authorization code along with other parameters.

```js
const queryParams = new URLSearchParams({
    response_type: 'code',
    client_id: process.env.CLIENT_ID,
    redirect_uri: process.env.REDIRECT_URI,
    code_challenge: code_challenge,
    code_challenge_method: 'S256'
  })
```

And the code verifier when requesting the access token.

```js
const bodyParams = new URLSearchParams({
    grant_type: 'authorization_code',
    client_id: process.env.CLIENT_ID,
    client_secret: process.env.CLIENT_SECRET,
    redirect_uri: process.env.REDIRECT_URI,
    code_verifier: code_verifier,
    code: auth_code
  })
```

### Step 2: Generating Access & Auth Token (Using Postman)

**_Note: Code verifier and code challenge is automatically created by postman._**

Change these parameters under the `Authorization` tab in postman:

```json
{
    "Client ID": "your_client_id",
    "Client Secret": "your_client_secret",
    "Grant type": "Authorization Code (With PKCE)",
    "redirect_uri": "your_redirect_uri",
    "Auth URL": "https://codex-auth.azurewebsites.net/auth/authorize/",
    "Access Token URL": "https://codex-auth.azurewebsites.net/auth/token/"
}
```
Then you can get the token by pressing the `Get New Access Token` button. The following picture shows the postman:

![Token Creation](https://github.com/javedcoding/CODEXAuthenticationPannel/blob/ayan_forked_hung/readme_pics/token_creation.png)

### Step 2: Generating Access & Auth Token (Using Commandline & Browser)

**_Note: You'll need to create a code verifier and code challenge. Here is a python code and Js code to generate them
they are not mentioned in all the tutorials_**

```python
import random
import string
import base64
import hashlib

code_verifier = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(43, 128)))

code_challenge = hashlib.sha256(code_verifier.encode('utf-8')).digest()
code_challenge = base64.urlsafe_b64encode(code_challenge).decode('utf-8').replace('=', '')
```

To start the Authorization code flow go to this URL which is the same as shown below:

`https://codex-auth.azurewebsites.net/auth/authorize/?response_type=code&code_challenge=<code_challeneg>&code_challenge_method=S256&client_id=<Client ID>&redirect_uri=<Redirect url>`

After making a request to the above URL you will be redirected to the login page. After logging in you will be
redirected to the redirect url you provided with a code. The code will be used to get the token. Some similar to

`<callback url>/callback?code=<code>`

This code can then be used to get the token.

```bash
curl -X POST \
    -H "Cache-Control: no-cache" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    "http://127.0.0.1:8000/o/token/" \
    -d "client_id=${ID}" \
    -d "client_secret=${SECRET}" \
    -d "code=${Auth_CODE}" \
    -d "redirect_uri=http://127.0.0.1:8000/noexist/callback" \
    -d "grant_type=authorization_code"
```

Where you'll get a response from the server with the Oauth2 access token

```json
{
  "access_token": "jooqrnOrNa0BrNWlg68u9sl6SkdFZg",
  "expires_in": 36000,
  "token_type": "Bearer",
  "scope": "read write",
  "refresh_token": "HNvDQjjsnvDySaK0miwG4lttJEl9yD"
}
```

### Step 3: Using the token

Once you have the token you should put it in the header of the request like this while making requests to the API's
protected resources.

```js
const headerParams = new URLSearchParams({
    Authorization: 'Bearer jooqrnOrNa0BrNWlg68u9sl6SkdFZg',
  })
```

### Resources behind API:

1. https://codex-auth.azurewebsites.net/auth/user-detail/ (GET): Provides you with all the user details of the user.
    ```json
    {
        "first_name": "Mashnunul",
        "last_name": "Huq",
        "phone": "123123",
        "city": "Frankfurte",
        "addresse": "ben-gurion-ring 50",
        "state": "hessen",
        "zip": "60422",
        "roll": "Super Admin",
        "Provider": "Audi"

    }
    ```
2. https://codex-auth.azurewebsites.net/auth/user-profile-update/ (POST): Gives you access to change the role of the
   user.
    ```json
    {
        "role": "Super Admin",
        "provider": "Audi"
    }
    ```
   The role can be only changed between `Base User`, `Admin`, `Super Admin`. The provider can be changed to any string.
