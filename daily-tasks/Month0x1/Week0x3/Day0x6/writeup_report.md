# CRLF Injection Shenanigans


## Summary

- This article explains how HTTP-Response splitting is not dead, using CRLF bugs

---

<br>
<br>

## Details

- The researcher explains about 2 major detection mechanisms

1. By stating a non-existant HTTP Version (HTTP/13.37)

```URL
https://www.moopinger.com/%20HTTP/13.37%0D%0Ax-end:%20a
```

this should generate a [==*505/HTTP Version Not Supported*==](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/505)


2. By specifiying a Non-Existant `Transfer-Encoding` header

```URL
https://www.moopinger.com/%20HTTP/13.37%0D%0ATransfer-Encoding:%20nonexistant%0D%0Ax-end:%20a
```

this should respond with [==*501 Not Implemented*==](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/501)


---

<br>

- The researcher also had a custom script to test for this [here](https://github.com/Moopinger/crlf-detection-script)

---

<br>
<br>

## Additional

- The researcher was inpspired from the Number 6 Vulnerability [here](https://portswigger.net/research/top-10-web-hacking-techniques-of-2023)
