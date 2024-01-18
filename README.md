# Web-Authentication

## Contents

*   [API Documentation](#API-Documentation)
    *   [Normal Easy Auithorization Server](#Normal-Easy-Auithorization-Server)
        *   [Important URLs](#Important-URLs)
        *   [How To Use Our API](#How-To-Use-Our-API)
    *   [OAuth2 Auithorization Server](#OAuth2-Auithorization-Server)
*   [Getting started](#getting-started)
    *   [Requirements](#requirements)
    *   [Install](#install)
    *   [Usage](#usage)


## API-Documentation
We have built two types of authorization systems. One is JWT authorization which has some flaws and back lags. Another one is industry standard OAuth2 Service. Feel free to use any of them.

### Normal Easy Auithorization Server
At first this is version 0.1 which is live. There will be more changes in api of later versions

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


<img width="857" alt="login with token" src="https://github.com/javedcoding/CODEXAuthenticationPannel/assets/59325753/67c3c305-d14f-4914-97a4-bec4893cf81d">

This is a second method to login with registration token. This will later be changed to project login system. So it is not suggested to implement right now.

<img width="858" alt="logout with token" src="https://github.com/javedcoding/CODEXAuthenticationPannel/assets/59325753/638dd8c0-9dac-4033-b301-7938e2efea63">

This is the logout API. The login token will be revoked by this.

<img width="858" alt="update profile token field" src="https://github.com/javedcoding/CODEXAuthenticationPannel/assets/59325753/dd64d56e-5cad-44d6-be9b-1aee6c252e77">

For Updating user profile one needs to put login authentication token.

<img width="849" alt="update profile" src="https://github.com/javedcoding/CODEXAuthenticationPannel/assets/59325753/abec53df-1d3e-4e05-b454-0366f803ef18">

This is the API format for user profile updating.
```
{
    "first_name": "TeleTest",
    "last_name": "Test",
    "phone": "123123",
    "city": "mashnunul.huq@stud.fra-uas.de",
    "state": "uganda",
    "zip": "60422"
}
```
