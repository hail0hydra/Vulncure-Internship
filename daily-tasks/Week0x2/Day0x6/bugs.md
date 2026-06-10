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

- writeup [here](https://infosecwriteups.com/a-tale-of-my-first-ever-full-ssrf-bug-4fe71a76e9c4)

- email sign-up functionality leads to some internal mailing list endpoint, mentioned by a `?url=` parameter.

- That is vulnerable to AWS creds access. But not localhost. (maybe try DNS rebinding?)


<br>
<br>

### 2. CSRF

- writeup [here](https://smaranchand.com.np/2019/10/an-inconsistent-csrf/)

- Brute force way to doing CSRF. Brute Forced parameter: `addressID`

<br>
<br>


### 3. Arbitrary File Uploads

- writeup [here](https://medium.com/@frostnull/from-file-upload-to-email-pass-dc7141aa1ff6)

- ASP reverse shell upload via `Content-Type` header manipulation

- Access of `ConnectionString.config` file which stored clear text __PASSWORD, USERNAME & DATABASE NAME__

- lead to credential compromise of many Domain Admins


<br>
<br>

### 4. Path Traversal

- writeup [here](https://labs.detectify.com/security-guidance/how-i-found-the-grafana-zero-day-path-traversal-exploit-that-gave-me-access-to-your-logs/)

- Due to usage of `filepath.Clean()` function in go library, an attacker could easily cause path traversal and access sensitive files over the graphana instance 

![path traversal](https://labsadmin.detectify.com/app/uploads/2021/12/docker_test_path_traversal.png)

<br>
<br>

### 5. IDOR - Insecure Direct Object Reference

- writeup [here](https://infosecwriteups.com/all-about-getting-first-bounty-with-idor-849db2828c8)

- two very cool and a little complex than others, IDORS!

 1. Metioning Other users, apart from the post creator, by uid

 2. Joining random groups and seeing group description and group leader id, by group id IDOR.
