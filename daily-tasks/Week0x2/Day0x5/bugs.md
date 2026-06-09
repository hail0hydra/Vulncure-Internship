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

- writeup [here](https://geleta.eu/2019/my-first-ssrf-using-dns-rebinfing/)

- SSRF & DNS rebinding


<br>
<br>

### 2. CSRF

- writeup [here](https://infosecwriteups.com/a-web-cache-deception-chained-to-a-csrf-the-recipe-9e9a5b5f53aa)

- cache deception, leads to csrf token leak, which leads to CSRF attack

<br>
<br>


### 3. Arbitrary File Uploads

- writeup [here](https://blog.voorivex.team/uncovering-a-command-injection-2400-bounty)

- not exactly file upload, but RCE via file upload functionality


<br>
<br>

### 4. Path Traversal

- writeup [here](https://infosecwriteups.com/hacking-the-dutch-government-153678a191c0)

- Simple path traversal because of how NGINX and Apacahe tomcat look at the input differently.

<br>
<br>

### 5. IDOR - Insecure Direct Object Reference

- writeup [here](https://fortbridge.co.uk/idor-exploitation-via-hpp-api-hacking-case-study/)

- using HTTP Parameter Pollution to bypass IDOR restrictions, to cause IDOR
