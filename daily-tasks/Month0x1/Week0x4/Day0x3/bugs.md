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

- writeup [here](https://hackerone.com/reports/643622)

- SSRF in service fetching remote videos.


<br>
<br>

### 2. CSRF

- writeup [here](https://hackerone.com/reports/334139)

- csrf leading to expiration of free trails of all phished accounts.

<br>
<br>


### 3. Arbitrary File Uploads

- writeup [here](https://thibaud-robin.fr/articles/bypass-filter-upload/)

- uploading `.htaccess` to change directory configuration to upload webshell (php).


<br>
<br>

### 4. Path Traversal or Local File Inclusion

- writeup [here](https://medium.com/@jonathanbouman/local-file-inclusion-at-ikea-com-e695ed64d82f)

- PDF template manipulation leads to LFI.

<br>
<br>

### 5. IDOR - Insecure Direct Object Reference

- writeup [here](https://yasserali.com/how-i-could-change-your-ebay-password/)

- IDOR leads to ATO on ebay.
