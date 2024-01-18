# Web-Authentication

## Contents

*   [API Documentation](#API-Documentation)
    *   [Normal Easy Auithorization Server](#Normal-Easy-Auithorization-Server)
        *   [Important URLs](#Important-URLs)
        *   [How To Use Our API](#How-To-Use-Our-API)
    *   [OAuth2 Auithorization Server](#OAuth2-Auithorization-Server)
        *   [Important URLs](#Important-URLs)
        *   [How To Use Our API](#How-To-Use-Our-API)
*   [Getting started](#getting-started)
    *   [Requirements](#requirements)
    *   [Install](#install)
    *   [Usage](#usage)


## API-Documentation
We have built two types of authorization systems. One is JWT authorization which has some flaws and back lags. Another one is industry standard OAuth2 Service. Feel free to use any of them.

### Normal Easy Auithorization Server
At first this is version 1.1 which is live. There can be more changes in api of later versions

#### Important URLs 
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


#### How To Use Our API
This API system is easy to use APIs. There can be small changes time to time. But the format is fixed for calling. Most of the fields which are mandatory will be mentioned with a *. Other optional fields can be ommited from the request body.

##### First API for Register
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

#### Second API for Login
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
#### Third API for Update-Profile

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

#### Last API for Deleting Profile
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

### OAuth2 Auithorization Server
This is an industry standard authorization system. Oauth2 is implemented aith PKCE type Authorization Code. This is stable version 2.0.

#### Important URLs 
First Important URL is the Application Registration API URL (as like through google you are registering for chatgpt):
```
https://codex-auth.azurewebsites.net/auth/applications/register
```
Corresponding Important URL is the Application Registration API AUTH URL:
```
https://codex-auth.azurewebsites.net/auth/authorize
```
Another corresponding Important URL is the Application Registration API AUTH Token URL:
```
https://codex-auth.azurewebsites.net/auth/token
```
Next URL is the User Register URL:
```
https://codex-auth.azurewebsites.net/register/
```
Next URL is the Login URL:
```
https://codex-auth.azurewebsites.net/login/
```
Then the updating of profile is accomodated with the following API URL:
```
https://codex-auth.azurewebsites.net/api/user-profile-update/
```
The last URL is the user profile API:
```
https://codex-auth.azurewebsites.net/api/user-detail/
```

#### How To Use Our API
This API system is implemented through secured Oauth2 authentication system. The format is fixed for calling. Most of the fields which are mandatory will be mentioned with a *. Other optional fields can be ommited from the request body.

##### First API for Register


Format is below for the POST request:
```

```
username*:- Provide the username to be used while login
email*:- Provide the email to be used while registering and a confirmation will come to this email if its correct.
password*:- Provide a password
role:- Provide user role between Basic User, Admin, Super Admin
provider:- Provider details which is upto 50 characters long

A response will come up like the below




```

```

Important you will need the token to pass while updating profile and deleting profile so save it in your database or somewhere else.

#### Last API for Login



Format is below for the POST request:
```

```
username*:- Provide the username used while registering
password*:- Provide a password used while registering

A Response will be provided just like below:


```

```
If token is changed there will be a token field also which is required for Updating Profile or Deleting Profile
