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

- writeup [here](https://hackerone.com/reports/381129#activity-3952106)

- ability to create a custom personal endpoint and make it point to whatever, leads to SSRF of the internal server of slack.


<br>
<br>

### 2. CSRF

- writeup [here](https://hackerone.com/reports/423022)

- Account takeover in the **connect account with yahoo feature.**

- => No CSRF tokens, so attacker controlled site visit and an unconnected yahoo account, leads to full ATO.

<br>
<br>


### 3. Arbitrary File Uploads

- writeup [here](https://www.synack.com/exploits-explained/guest-blog-from-file-upload-to-rce/)

- Image upload functionality changes file exif data and resizes it and changes file data.

- Inserting php code in unchaged regions of file allows for RCE.

- php file was uploaded without any fuss.


<br>
<br>

### 4. Path Traversal

- writeup [here](https://blog.blackfan.ru/2018/01/pda-test.yandex.ru-file-reading.html)

- due to discrepancies in how **NGINX** and **NodeJS** handles the `/` character for path traversal, this attack worked.

- There was a catch, the patch needed to have `_` (underscore). It was met, and also, It required files to have `.js` extension

- Since this was being accessed through the static portal?

- and the **.js** extentsion was discarded with the `?` symbol, ofc urlencoded `%3F`.

<br>
<br>

### 5. IDOR - Insecure Direct Object Reference

- writeup [here](https://yasserali.com/microsoft-careers-com-remote-password-reset/)

- in `https://microsoft-careers.com`, this site is not longer supported by Microsoft.

- IDOR in **RESET PASSWORD** functionality, where and `ID` is being used to change the password, instead of a unique key that has been sent on the mail.

- Can lead to autmated change of all of the accounts's password with a simple script.
