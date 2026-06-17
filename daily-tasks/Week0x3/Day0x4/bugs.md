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

- writeup [here](https://medium.com/@pflash0x0punk/ssrf-via-ffmpeg-hls-processing-a04e0288a8c5)

- ffmpeg has ability to send requests to remote files: HLS (HTTP Live Streaming).

- generated a malicious .avi file for the same and SSRF.


<br>
<br>

### 2. CSRF

- writeup [here](https://infosecwriteups.com/csrf-leads-to-account-takeover-in-yahoo-aa96c678d2aa)

- HTTP Method Override for **Ruby on Rails**

- Changing and playing with different HTTP methods, **PATCH->POST**

<br>
<br>


### 3. Arbitrary File Uploads

- writeup [here](https://web.archive.org/web/20200601005729/https://vict0ni.me/unrestricted-file-upload-on-pdf/)

- file upload vulnerability with CSRF. Potential infection and creation of malware. On both user side and the reviewer of CV.


<br>
<br>

### 4. Path Traversal

- writeup [here](https://feed.bugs.xdavidhu.me/bugs/0006)

- very interesting bug. Safari took `<title></title>` name as title.

<br>
<br>

### 5. IDOR - Insecure Direct Object Reference

- writeup [here](https://osintteam.blog/how-to-discovered-idor-from-a-blank-page-bug-bounty-tuesday-5af784533d1a)

- Blank page-> JS code analysis -> endpoints detection -> response for missing param -> simple FUZZ -> information disclosure -> $200 bounty
