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

- writeup [here](https://infosecwriteups.com/story-of-a-2-5k-bounty-ssrf-on-zimbra-led-to-dump-all-credentials-in-clear-text-6fe826005ccc)

- Unauthorized Access to MAIL configuration, leads to SSRF, which in turn leads to credential and sensitive information disclosure


<br>
<br>

### 2. CSRF

- writeup [here](https://hackerone.com/reports/419891)

- Simple CSRF, can lead to associated email change of an unverified email account. If done before verifying email and if logged in.

<br>
<br>


### 3. Arbitrary File Uploads

- writeup [here](https://hackerone.com/reports/900179)

- File upload leads to Stored XSS and potential RCE.


<br>
<br>

### 4. Path Traversal

- writeup [here](https://infosecwriteups.com/bugbounty-journey-from-lfi-to-rce-how-a69afe5a0899)

- There was LFI, it was converted into RCE, since a file descriptor was opening the response logs. so simple storing executable code in the file storing response logs, executed and gave RCE.

<br>
<br>

### 5. IDOR - Insecure Direct Object Reference

- writeup [here](https://hackerone.com/reports/819807)

- IDOR leads to device wipeout. Anyone's device.
