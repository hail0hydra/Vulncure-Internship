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

- writeup [here](https://medium.com/@xvnpw/from-in-regex-to-ssrf-part-1-31d5706854ef)

- bypassing url whitelisting because of improper regex checking

- Cleverly redirecting all url to enumerate internal network for open ports, subdomains and AWS creds.


<br>
<br>

### 2. CSRF

- writeup [here](https://rajeshranjan457.medium.com/how-i-csrfd-my-first-bounty-a62b593d3f4d)

- when csrf token is not send, validation is skipped. Leading to CSRF.

<br>
<br>


### 3. Arbitrary File Uploads

- writeup [here](https://shahjerry33.medium.com/sql-wildcard-dos-hang-till-death-adbae66d1f7b)

- SQL wildcard injection leads to DOS.


<br>
<br>

### 4. Path Traversal

- writeup [here](https://medium.com/@hritkmjth/directory-traversal-and-lfi-worth-400-c4422785d3bd)

- Path traversal leads to admin account credentials leak.

<br>
<br>

### 5. IDOR - Insecure Direct Object Reference

- writeup [here](https://web.archive.org/web/20191223160434/https://gh0st.cn/archives/2019-10-01/1)

- Account info disclosure
