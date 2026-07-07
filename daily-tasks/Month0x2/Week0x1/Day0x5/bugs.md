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

- writeup [here](https://medium.com/@th3g3nt3l/how-i-found-an-ssrf-in-yahoo-guesthouse-recon-wins-8722672e41d4)

- Interesting bug in cookie value. Domain was being passed in cookie, changing it lead to SSRF (DNS interaction).


<br>
<br>

### 2. CSRF

- writeup [here](https://medium.com/@saneem7/csrf-to-one-tray-red-bull-6564cd884a47)

- Vulnerable component in phpmyadmin, leading to CSRF, mapped to a cve

- A `nuclei` template for the same is [here](https://github.com/projectdiscovery/nuclei-templates/blob/master/cves/2019/CVE-2019-12616.yaml)

<br>
<br>


### 3. Arbitrary File Uploads

- writeup [here](https://stazot.com/?article=bolt-cms-file-upload-bypass-rce)

- very cool file upload bypass technique, after source code review.


<br>
<br>

### 4. Path Traversal

- writeup [here](https://medium.com/@abhishekY495/bypassing-lfi-local-file-inclusion-ebf4274e7027)

- Base64 path traversal sequence worked as a payload?? -> urlencode-> base64 -> payload

<br>
<br>

### 5. IDOR - Insecure Direct Object Reference

- writeup [here](https://yogesht7.medium.com/how-i-was-able-to-delete-google-gallery-data-idor-53d2f303efff)

- Vulnerable API parameter, even though Session tokens were present, they were not being considered, leading to ability to delete media from anyone's google Gallery.
