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

- writeup [here](https://dphoeniixx.medium.com/vimeo-upload-function-ssrf-7466d8630437)

- Cool SSRF in VIMEO, partial download leads to downloading metadata.

- Simple hexeditor open would show the retrieved data, since you can download your uploaded file.


<br>
<br>

### 2. CSRF

- writeup [here](https://freedium-mirror.cfd/https://infosecwriteups.com/executing-csrf-with-phone-validation-103c525dd310)

- Using CSRF to add and bypass 2fa of OTP quickly via some programmatic design, since numbers were not being forwarded to Twilio, attacker uses Google voice and then forwards to Twilio

<br>
<br>


### 3. Arbitrary File Uploads

- writeup [here](https://binamrapandey.medium.com/unrestricted-file-upload-e95e1c6fb80)

- upload vs publish functionalities, lead to rce via file upload


<br>
<br>

### 4. Path Traversal

- writeup [here](https://infosecwriteups.com/directory-ttraversal-vulnerability-in-huawei-hg255s-products-dce941a1d015)

- simple path traversal leading to access of sensitive files. This was in a device being used by a lot of people in Turkey.

<br>
<br>

### 5. IDOR - Insecure Direct Object Reference

- writeup [here](https://footstep.ninja/posts/idor-via-websockets/)

- IDOR in websockets request.
