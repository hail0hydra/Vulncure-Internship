# Vulnerability Report

- The writeup can be read [here](https://web.archive.org/web/20190312192719/https://blog.jr0ch17.com/2018/No-RCE-then-SSH-to-the-box/)

- The researcher is [Jasmin Landry](https://x.com/JR0ch17)

---

<br>
<br>

## Summary

- How a very vulnerable CMS lead to **root** level **RCE** on a webapp that was using that CMS.

---

<br>
<br>

## Details

- The researcher was browsing through a lot of sudomains via EyeWitness, and found a subdomain that looked like and old CMS website.

- He was able to login with `admin:admin`

- There was no Acess Control, He found XSS, XXE and LFD/File Inclusion.

---

<br>
<br>

## Next Steps

- He found an endpoint where you could upload/update files.

![upload](https://web.archive.org/web/20190312192719im_/https://blog.jr0ch17.com/images/POST_request.png)

- so the attacker tried uploading like this:

```
/../../../../../../../../../../../../tmp/test.txt
```

- And it worked!


<br>


- Now since there was LFD, he confirmed it as well:

![uploaded](https://web.archive.org/web/20190312192719im_/https://blog.jr0ch17.com/images/LFI.png)


- Since there was SSH service running, and the CMS was running as **root**, that meant all actions by the researcher over the OS were also root level.

- He uploaded his **ssh keys** over the machine:

![ssh](https://web.archive.org/web/20190312192719im_/https://blog.jr0ch17.com/images/SSH.png)

- And it worked.


<br>

- He tried the SSH and he was root! RCE!:

![ssh](https://web.archive.org/web/20190312192719im_/https://blog.jr0ch17.com/images/ID.png)

---


<br>
<br>

## Reporting

- Since this was an issue in the CMS, he got in touch with the CMS team, they resolved it together.

- He also let the client using the CMS about the same.
