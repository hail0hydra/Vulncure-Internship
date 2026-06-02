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

- This vulnerability allows an remote attacker, to leverage some web application misconfiguration and make the application server send requests to either other internal hosts or external internet connected machines or both.

- This bug generally arises when non-sanitized user input get the ability to control the __URL__ parameter/value to which the server makes request.

- This can be found directly in the url as a parameter, in the POST request body, etc.

<br>

##### Writeup

- I read [this](https://medium.com/bugbountywriteup/ssrf-in-apis-how-a-single-url-parameter-can-expose-internal-systems-63128bff63a4) writeup today to better understand SSRF.

<br>
<br>

### 2. CSRF

- This vulnerability allows an attacker to forge requests on behalf of a victim, when the victim visits their website.

- Improper configuration and lack of CSRF tokens can allows such a bug to have a huge impact on the website.

- Although SOP prevents one origin (scheme+domain+port) from accessing/reading data from other origin, it doesn't do much in case of sending/POSTING a request from one origin on behalf of another origin.

- This means that when a victim visits an attacker controlled website, that website can have a simple `JavaScript` which loads and makes a request to a certain endpoint of another important origin.

- Even though the attacker, won't be able to read and see if the attack happened successfully or not, pairing this attack with an XSS makes the visibility even clearer.

- This works because the client Browser is by default designed to send the stored client cache for target website, if a request for the target website is being generated.

- Many-a-times, admins can simply visit some URLs like:

```
https://target.com/admin/delete/user/?uid=xxxx?confirm=true
```


- in Order to delete some user, with a `uid=xxxx`, and admin might visit the above URL. If there is no protection against CSRF setup, and the admin visits the attacker controlled website, a simple __GET__ request can easily be generated from the attacker's page, which can potentially delete user/users.


- To prevent such attacks, instead of Cookies, sites have started using __Authorization: Bearer___, which is not sent by default with every request, unlike Cookies.

- a CSRF token also is generated from the server side, which should be sent with each request by the browser, to prove that there was no CSRF attack.

- an Attacker without the knowledge of CSRF token (thanks to SOP), can no longer perform a CSRF, unless, there is a stored XSS, which lets the attacker read incoming responses from the website, ultimately stealing both the __CSRF token__ and the __Authorization: Bearer__.

<br>

##### Writeup

- I read basic DVWA walk-through to explain CSRF which can be found [here](https://medium.com/@Kamal_S/dvwa-cross-site-request-forgery-csrf-vulnerability-low-security-b02dce2423b4)

<br>
<br>


### 3. Arbitrary File Uploads

- This bug can lead to serious compromises if not handled properly, leading to RCE, Arbitrary File Access, and exploitation of Trusts, just to say a few.

- If a web application allows an attacker to upload any kind of arbitrary file to its server, including the scripting files being used by the server, the attacker could upload a malicious script and make it execute by the server, ultimately having complete control over the server.

- If an application has a PHP backend, and it also allows PHP files to be uploaded, a simple file with the following contents:

```PHP
<?php echo system($_GET['cmd']); ?>
```

- the above file can give a webshell.

- the root cause of such vulnerabilities is robust file validation mechanisms and improper implementation of file validation mechanisms as well mechansisms which can easily be changed/controlled by client side.

- these include MIME type checking, and not checking actual contents, or using a blacklist which is missing some variations of the script file.

<br>

##### Writeup

- I read [this](https://medium.com/@gokulsspace/hitting-the-jackpot-with-rce-43755cac1415) writeup regarding the bug today.

<br>
<br>

### 4. Path Traversal

- This bug, allows an attacker to read any arbitrary file present on the application server, due to improper input sanitization and input validation.


- If an image is being loaded from the local server storage as follows:

```html
<img src="/images/background.jpg" alt="" />
```

- it is possible, this image resource could be in some kind of a common directory like `/var/www/data/images/`

- in such instances we can make use of `../` or `..\` for (windows) to try and see if we cat escape out of these directories and access some file over the server.

- a simple payload as follows (for linux server):

```
GET /images/../../../../etc/passwd HTTP/1.1
```

- could easily let us read the `/etc/passwd` file.

- There is one more thing called __Client Side Path Traversal__ (CSPT), which I will be exploring as we go ahead.

<br>

##### Writeup

- A mix of SSRF and Path Traversal, providing access to internal sensitive files. The writeup I read is [here](https://medium.com/fmisec/how-i-exploited-a-secondary-context-bug-to-trigger-ssrf-path-traversal-in-backend-api-calls-f1023cac5384)

<br>
<br>

### 5. IDOR - Insecure Direct Object Reference

- This bug arises, when an individual token, or and identifier for a resource, object of functionality can be controlled by the client and modified to access other objects.

- In such a scenario, this bug can lead of broken access control or arbitrary file read.

- we can look at an example below:

```
https://readacted.com/accounts/user?id=008
```

- the `id` parameter above if guessed correctly can give access to the resources of other users. This can be fuzzed over to check and see if that is the case or not.

- This bug becomes highly exploitable specially if such parameters are easy to guess and the pattern can be easily understood.

<br>

##### Writeup

- Cool IDOR vulnerability writeup, how random IDs were found easily and used for IDOR based bug exploitations. writeup is [here](https://kresec.medium.com/idor-vulnerability-despite-non-enumerable-object-identifiers-fd4379b89fa0)
