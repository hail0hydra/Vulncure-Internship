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

- writeup [here](https://infosecwriteups.com/ssrf-that-allowed-us-to-access-whole-infra-web-services-and-many-more-3424f8efa0e4)

- SSRF WAF bypass for `169.254.169.254` using decimal representation: `2852039166`


---

<br>
<br>

### 2. CSRF

- writeup [here](https://labs.detectify.com/security-guidance/login-logout-csrf-time-to-reconsider/)

- learn about how `Login/Logout` CSRF is not worthless. It can be combined with serious issues and cause good damage.

---

<br>
<br>



### 3. Arbitrary File Uploads

- writeup [here](https://medium.com/@pm_/bug-bounty-como-encontrei-o-bug-unrestricted-file-upload-dd1a61adc9fd)

- Changing the `Content-Type` header to **text/html** but keeping the File extension same, still got the malicious file... How?



<br>
<br>

### 4. Path Traversal

- writeup [here](https://infosecwriteups.com/why-u-should-use-burp-to-test-path-traversal-vulnerability-and-also-get-rxss-2743cbb16a3c)

- Well not exactly the bounty for Path Traversal, but It was there.

<br>
<br>

### 5. IDOR - Insecure Direct Object Reference

- writeup [here](https://web.archive.org/web/20200624022122/https://wisdomfreak.com/2020/06/tail-of-idor/)

- understanding the technique is unique links generation for object, which was simple, IDOR was exploited.

- also due to lack of rate limiting
