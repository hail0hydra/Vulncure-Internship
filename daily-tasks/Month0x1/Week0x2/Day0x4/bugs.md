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

- writeup [here](https://infosecwriteups.com/story-of-a-really-cool-ssrf-bug-cf88a3800efc)

- simple SSRF in request parameter, leads to AWS credential theft.


<br>
<br>

### 2. CSRF

- writeup [here](https://bhupendra1238.medium.com/how-i-got-my-first-bounty-hof-from-google-csrf-lead-to-account-delete-85f9906ba9ec)

- how did you know not to close HTML tag?? __[doubt]__

<br>
<br>


### 3. Arbitrary File Uploads

- writeup [here](https://www.synack.com/exploits-explained/guest-blog-from-file-upload-to-rce/)

- understanding file modifications performed by server and leveraging it to get and RCE.


<br>
<br>

### 4. Path Traversal

- writeup [here](https://research.aurainfosec.io/disclosure/papercut/CVE-2023%E2%80%9331046/)

- path traversal in print management product leads to users with least privilege to access and download sensitive files and data. Mapped to __CVE-2023-31046__

<br>
<br>

### 5. IDOR - Insecure Direct Object Reference

- writeup [here](https://infosecwriteups.com/accidental-observation-to-critical-idor-d4d910a855bf)

- simple `id` parameter and curious attention leads to P1 bug, account takeover.
