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

- writeup [here](https://logicbomb.medium.com/the-journey-of-web-cache-firewall-bypass-to-ssrf-to-aws-credentials-compromise-b250fb40af82)

- Bypassing Nginx Cache by just appending a simple `?` in the end to make a successful request to the AWS endpoint.


<br>
<br>

### 2. CSRF

- writeup [here](https://hackerone.com/reports/834366)

- login page of Hackerone, Had a cookie attached to csrf, but was validating even without cookie.

- basically only csrf validation when cookie is present, else bypass.

<br>
<br>


### 3. Arbitrary File Uploads

- writeup [here](https://sagarsajeev.medium.com/file-upload-bypass-to-rce-76991b47ad8f)

- 3 consecutive fixes, 3 consecutive php file uploads, all leading to RCE.


<br>
<br>

### 4. Path Traversal

- writeup [here](https://freedium-mirror.cfd/https://systemweakness.com/common-nginx-misconfiguration-leads-to-path-traversal-d58701e997bc)

- how a Vulnerable Misconfiguration in Nginx can look like

<br>
<br>

### 5. IDOR - Insecure Direct Object Reference

- writeup [here](https://infosecwriteups.com/stories-of-idor-4966369e6d82)

- Email can be sent as admin, people could be unsubscribed, Profile info like name, email leaked. 
