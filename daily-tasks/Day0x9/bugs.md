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

- writeup [here](https://www.assetnote.io/resources/research/digging-for-ssrf-in-nextjs-apps?utm_source=bugbountydaily.com&utm_medium=referral)

- SSRF in NextJS framework before v14.1.1

- Cool code review and technique to fool the server


<br>
<br>

### 2. CSRF

- writeup [here](https://infosecwriteups.com/csrf-bypass-using-domain-confusion-leads-to-ato-ac682dd17722)

- learnt about creating custom payload

- new term: __Domain Confusion__

<br>
<br>


### 3. Arbitrary File Uploads

- writeup [here](https://blog.doyensec.com/2025/01/09/cspt-file-upload.html?utm_source=bugbountydaily.com&utm_medium=referral)

- learnt about different libraries used in file type detection, using mimes, magic headers and hardcoded values at specific offsets.

- learnt how to bypass all of this to upload a JSON instead.


<br>
<br>

### 4. Path Traversal

- writeup [here](https://www.yeswehack.com/learn-bug-bounty/python-pitfalls-turning-developer-mistakes?utm_source=bugbountydaily.com&utm_medium=referral)

- Learnt about how pat traversal vulnerabilities are unwittingly created using bugged builtins in Python.

- Learnt about insecure de-serialisations leading to RCEs.

<br>
<br>

### 5. IDOR - Insecure Direct Object Reference

- writeup [here](https://josephthacker.com/hacking/cybersecurity/2022/08/18/unpredictable-idors.html?utm_source=bugbountydaily.com&utm_medium=referral)

- How unpredictable-idors are not low-level bugs and ways they can be identified.

- Portswigger [lab](https://portswigger.net/web-security/access-control/idor)
