# A Story About How I Found XSS in ASUS

- writeup [here](https://infosecwriteups.com/a-story-about-how-i-found-xss-in-asus-cb233ce3bb9c)

- Researcher [Karthikeyan.V](https://medium.com/@karthithehacker)

---

<br>

## Summary

- The researcher found an RXSS in the url of a domain owned by **Asus**, with high impact.

---


<br>
<br>

## Details

- The subdomain `adam.asus.com` have Debug mode on in the production server, powered by Laravel

- Becoz of that, the debug developer endpoints like `/_ignition` were accessableo.

- Once such nested endpoint seemed to have an RXSS in the URL


![RXSS](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*Dx3iowTStEWjlOTnYhjrPA.png)

- the payload is:

```URL
--%3E%3Csvg%20onload=alert('cappriciosec.com')%3E
```

<br>

- This has different IMPACTS based on the account privilege level which is getting compromised.

---

<br>
<br>

## Extra

- The researcher also released a tool to test for the same vulnerability, which can be found here :

    - [laravel-ignition-Rxss](https://github.com/Cappricio-Securities/laravel-ignition-Rxss)
