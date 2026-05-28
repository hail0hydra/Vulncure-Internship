# Writeup - IDOR “Insecure direct object references”, my first P1 in Bugbounty

- The writeup can be read [here](https://infosecwriteups.com/idor-insecure-direct-object-references-my-first-p1-in-bugbounty-fb01f50e25df)

- These vulnerabilities were found by a researcher called  __[Dris R.](https://medium.com/@jedus0r)__, a Security Researcher from Paris, France.

<br>
<br>

## Description

- The writeup is about a P1 and P3 vulnerability both based on IDOR, found in a web application, which allows users to create and Manage CMS (Content Management System).


- The two vulnerabilities found by the researcher are continuation of each other and shows how continuous persistence can lead to High severity vulnerability discoveries.

- These vulnerabilities show how backends fail to properly authorize and defend end points, letting any user with low privilege get access to resources they are not authorized to.

<br>
<br>

## Details

- While pentesting the Web app, the researcher had already found a P4 vulnerability, details of which are not mentioned, but having found so many P4s and P3s, this was actually a motivating factor for him to look for some P1s.


<br>
<br>

### What is an IDOR?

- standing for __Insecure Direct Object Reference__, it allows an attacker to gain unauthorized access to resources or perform unauthorized actions.


![IDOR](https://miro.medium.com/v2/resize:fit:1200/format:webp/1*Wrp3jYojPgbnvDOXIEaRew.png)



## Details Contd...


- The researcher mentioned having 3 important questions, which led him to finding his FIRST P1 bug:

1. How do they identify us? (session tokens and identification mechanism)

2. What are the sensitive features of the site? (most creating CMS)

3. What are out restrictions?

<br>

- while the researcher used `BurpSuite` to explore the webapp, he collected all the requests made to the site.

<br>

####  __Answers__:

1. after analyszing all the requests, it was made clear that the website __identified__ users with a __Unique ID__.

2. The website allows users to __Create and manage CMS__


<br>

- With just this much of information, he started sending all the API requests which contain the unique ID to the server, and then back to repeater.


- Below is one such request:

![PUT](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Nw86jPKpFxPoNXXWIPC_cg.png)

- The ID of researcher is `405`

```HTTP
PUT /api/v1/cmd/405 HTTP/2
```

<br>

### What is a PUT request?

- also one the common HTTP request methods, `PUT` is used to __create,modify__ data at an end point.

- you can look at it [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods/PUT)

<br>

### What is a DELETE request?

- the `DELETE` method asks the server to delete specified resource

- you can look at it [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods/DELETE)

<br>

- so the attacker tried modifying the __`ID`__ to something else:

```HTTP
PUT /api/v1/cms/419 HTTP/2
```

![mod-id](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*8TAOxelUBmk9PJ9gw8CCgA.png)

- we can look at the response above and see that, we received a __200 OK__ response.

```
An HTTP PUT request returns a 200 OK status code when an existing
resource is successfully modified and the server includes a message body
describing the result or status
```

- this proves that a user id `ID: 419` __exists!__

- The next thing the researcher did was send a `DELETE` request for the same resource to the server:

![del](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*r7gt7jrCgMUwSvSDoyV9Lg.pngo)

- response:

![del-res](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*8TAOxelUBmk9PJ9gw8CCgA.png)

<br>

- If we notice properly, the Response of the `DELETE` method exposes _USER DETAILS_ as can be seen in the picture above.

- Just to make sure that the resource (CMS) is deleted, another `PUT` request to the resource was sent.

![test](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*2YDQwdu2ti94Uz7sBSjCBA.png)

![resp-test](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*5XJTPDhzOlKYULKUg3H40g.png)

<br>

- As is visible from above request and response, the resource has successfully been deleted!


- When this bug was reported, the researcher received a __P3 IDOR__ tag.

![p3](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*eGOLjDmsDjUWM_s8VpOMtw.png)


<br>
<br>

## Next Steps

- the next question that arises is:

 >  _"if we can perform actions on the resources, can we access them? Can we access all users data?"_

- there was an endpoint for getting _users_ details:

```HTTP
/api/v1/users/{uid}
```

- so the researcher sends a `GET` request to the end point with his UID: `19795`

```HTTP
GET /api/v1/users/19795 HTTP/2
```

![get](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*AgVAh5rPKg4L-gr90VBv2A.png)

- surely enough, it gives back a JSON response of user details.

![get-rsp](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*OZGbp-BAPta7tkJw51yJmg.png)


- so the researcher tried the same once again, trying to change the ID:

```HTTP
GET /api/v1/users/19782 HTTP/2
```

- But this time it didn't work...

- But one method was still remaining: `DELETE`, so the researcher tried sending a DELETE request to the endpoint.


```HTTP
DELETE /api/v1/users/19782 HTTP/2
```

![del-user](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*yboqIam2lfUk7JXS0xc-Dw.png)

- and this actually __DID WORK!__

![del-rsp-usr](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*sMpm5S5FPUvxVbBp0A6uvA.png)

<br>

- To make sure that this actually did the job, he sent a DELETE requests once again but got a `404` error.

![success](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*QrqAjnlwVbNIGiaM-XEBlw.png)

- and this time it lead to a  __`P1 vulnerability`__

![p1](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*hAJ2whN5gDebiTdLSX1kdw.png)
