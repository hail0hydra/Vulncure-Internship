# Writeup - IDOR and Broken Access Control Risking Private Data Exposure

- The writeup can be read [here](https://c0nqr0r.medium.com/idor-and-broken-access-control-risking-private-data-exposure-dd808412ed13)

- This author for this writeup is [Ahmed Qaramany](https://c0nqr0r.medium.com/)

<br>
<br>

## Details

- The researcher was able to find and IDOR, leading to Broken Access Control in a webapplication which lets user manage their posts with CRUD operations.

- The WebApp provides services like medium and wordpress.


<br>
<br>

## Methodology

- The researcher created an account and mostly focused on requests with IDs and UUIDs.

- There were many such requests, one of which was getting a `user's post's report to email`.

- The above said functionality could be seen as follows:

![postmail](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*tjJf9MLtYJBjIbsEtf4nKA.png)

- The __`projectID`__ reference could be manipulated and the email to which the post report will be sent is also attacker controlled, but the backend did a good job to protect this endpoint.

- even though the mail was changed, the reports were being sent only to the actual author's mails.

<br>
<br>


## Next Steps

- In the same place, the researcher found option to extract and download the post report locally:

![extract](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*fIyY_5j4nGLNAp3gCdTjJw.png)

- so the researcher thought of giving it a try and captured the request in BurpSuite as follows:

![capture](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*GdQPgBrNZ2e5pqn8gVIBBQ.png)

- the above marked requests seem perfect for IDOR

![burp](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Bdb6sniE3P9sJxyW1jbqPg.png)


- in __request(1)__,  we can see a `backgroundJobId` and __`CREATED`__ response.


```
“backgroundJobId”:”d69047b7–3a7a-4784–96be-6633b6d8bd45",”status”:”CREATED”
```


<br>


- If we look at the next request, __request(2)__:

![next](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*3Uj1UpMUS2vQXtP0AeIGzA.png)

- we can see it is using the same `backgroundJobId`  as an endopoint to fetch the PDFs


<br>
<br>

#### Flow found

1. The first request is sent with a `postID`

2. The response contains `backgroundJobId`

3. The second response if sent with `backgroundJobId` and remote pdf cloud link is received with following format:

```
https://s3.amazonaws.com/xxxxxcompanyname/report/xxxxxxx/20241013/{backgroundJobId}.pdf
```

<br>
<br>

- The researcher passed the first request through a list of number from __`0-9999999`__ in order to get all valid `backgroundJobId`s

- by doing this he could access all posts!

![posts](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*lhPWshR7DV2Ldcf8azJXsg.png)

<br>
<br>

## Vulnerabilities:

1. The ability to try random fuzz list IDs against the `postId` to get `backgroundJobId` is an example of ___IDOR___.

2. The ability to then access the PDFs generated directly with `backgroundJobId` without any authentication or authorization checks in places is and example of ___Broken Access Control___.
