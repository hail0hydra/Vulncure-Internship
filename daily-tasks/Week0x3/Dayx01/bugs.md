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

- writeup [here](https://medium.com/@oXnoOneXo/a-story-of-a-nice-ssrf-vulnerability-51e16ff6a33f)

- another DNS rebinding shenanigan

- Important takeaway:

>according to the documentation here(https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-identity-documents.html) that we need to add the header `(X-aws-ec2-metadata-token-ttl-seconds: 21600)` to get a token then we use the returned token with the header `(X-aws-ec2-metadata-token: TOKEN)`. 


<br>
<br>

### 2. CSRF

- writeup [here](https://hazanasec.github.io/2023-07-30-Samesite-bypass-method-override.md/)

- Bypassing the **SameSite:Lax** restrictions with builtin `HTTP Method Overriding` in Web Frameworks.

- NEW: `SameSite` cookie attribute (existing Secure, HTTPOnly)

<br>
<br>


### 3. Arbitrary File Uploads

- writeup [here](https://medium.com/@fa1c0n/how-a-simple-directory-listing-leads-to-pii-data-leakage-remote-code-execution-and-many-more-104b09e644f4)

- Improper Access Control and Authorization checks. No Authentication

- PII leakage, Stored XSS

- Simple file upload  to RCE


<br>
<br>

### 4. Path Traversal

- writeup [here](https://www.erasec.be/blog/client-side-path-manipulation/)

- Client Side path traversal, leads to account card deletion.

- Has a mix of CSRF token. 

- New thing: `X-Xsrf-Token` header.

```
Importantly, because the Javascript code is executed normally to build the request,
the POST includes the CSRF header X-Xsrf-Token: My-CSRF-TOKEN and (obviously) the session cookies.
```

- what does the above mean??

<br>
<br>

### 5. IDOR - Insecure Direct Object Reference

- writeup [here](https://ian.sh/mcdonalds)

- Default Credentials and Too much sensitive data leakage. Too much PII leaked.
