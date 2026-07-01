## Documentation for 5 bugs

- The 5 bugs I have chosen to research more about are:

1. [x] __SSRF__

2. [x] __CSRF__

3. [x] __Arbitrary File Upload__

4. [x] __Path Traversal__

5. [x] __IDOR__

<br>
<br>


### 1. SSRF

- writeup [here](https://hackerone.com/reports/115748)

- SSRF in imgur leads to impersonation, version disclosure, etc.


<br>
<br>

### 2. CSRF

- writeup [here](https://medium.com/@Skylinearafat/a-very-useful-technique-to-bypass-the-csrf-protection-for-fun-and-profit-471af64da276)

- Changing request method from `POST` to `GET` and making the body parameters as request params, leads to CSRF protection bypass.

<br>
<br>


### 3. Arbitrary File Uploads

- writeup [here](https://medium.com/@cavdarbashas/unrestricted-file-upload-lead-to-stored-xss-at-microsoft-main-domain-baa9cadac6bd)

- vulnerable file upload of `Content-Type: image/svg+xml` leads to stored XSS.


<br>
<br>

### 4. Path Traversal / Local File Inclusion

- writeup [here](https://omespino.com/write-up-google-bug-bounty-lfi-on-production-servers-in-redacted-google-com-13337-usd/)

- Accessing google's server files without any authorization

<br>
<br>

### 5. IDOR - Insecure Direct Object Reference

- writeup [here](https://hackerone.com/reports/151465)

- using either `userUuid`  or `email`, you can see sensitive information without authorization.
