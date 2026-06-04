# Writeup - How I was able to discover ATO Via IDOR vulnerability

- researcher [Ahmed Tarek](https://medium.com/@0x_xnum)

<br>
<br>

## Summary

- and IDOR bug lead to Account Takeover.

- wierd auth_token verification

<br>
<br>


## Methodology

- `/api/v1/user/profile`

- Account 1 req:

```
GET /api/v1/user/profile?
user_id=273948261&auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWI
iOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxw
RJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c&timestamp=1349328731
```


- `user_id`:`27394826|1`


- Account 2 req:

```
GET /api/v1/user/profile?
user_id=273948262&auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ
zdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkF0dGVudG9yIiwiaWF0IjoxNjQ5MjQwNjcwL
CJleHAiOjE2NDkyNDExNzB9&timestamp=1349328732
```

- `user_id`: `27394826|2`


- Upon further investigation, it was seen that the application doesn’t validate the __token’s validity__ based on the token itself.

- Instead, it validates it based on the __timestamp__ so if the timestamp is __RIGHT__, and even if the token is __WRONG__ but it will accept the request.

- once a token is generated, it remains valid for 60 seconds from the time it was create, if the token is used after this 60-second period, it is considered expired and be invalid.

<br>

### timestamp

-  the timestamp increments by 1 every 10 seconds. After 60 seconds, it deems the token invalid.
``
- if the timestamp was `1349328731`, and a request sent 10 seconds later it will increase by 1 and the timestamp will be `1349328732` and would be accepted.

- But after 60 seconds, it will increase by 6 and will be `1349328737`, and it would be considered an invalid token, because the Token Validity Window will be expired

<br>
<br>

## Exploit

- Trying timestamp between `1349328731` and `1349328735`, account takeover was possible.
