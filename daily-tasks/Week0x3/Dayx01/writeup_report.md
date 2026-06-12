# 3 Easy cash via cache

- the writeup can be found [here](https://medium.com/@mohamed0xmuslim/3-easy-cash-via-cache-99d600565ac5)

- the researcher is [Muhammad Mostafa](https://medium.com/@mohamed0xmuslim)

<br>
<br>

---

## Summary

- Three different Cache Deception bugs in 3 different websites, exploited with 3 different ways.

<br>
<br>

---

## Details

- As explained, there are 3 different websites, so let's start with site 1

<br>
<br>

---

### 1. test.css

- The target assumed to be a subdomain of this kind: `subdomain.target.com`, had a account page with all details of a user were accessible.

```url
https://subdomain.target.com/gb/account/
```

- The `Cf-cache-status` for this was **DYNAMIC** which means, caching is disabled.


<br>

- The page had a JS which called `window.current_user`, which retrieve user sensitive info like user_id, email, phone, etc.


- The researcher tried simple payload as follows:

```url
https://subdomain.target.com/gb/account/test.css
```

<br>

- This returned a partricular HEADER: `Cf-cache-status` changed from **DYNAMIC** to **MISS**

- This meant the caching server tried to look for the resource, couldn't find it, and will cache it now.

- Accessing the same URL with a private tab, researcher was able to get all user details being loaded.

![bug1](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*4lqRlkQ0bGrVXfsAdRkzLA.jpeg)

---

<br>
<br>

### 2. ;test.css

- Similar case, getting **DYNAMIC** for `Cf-cache-status` HEADER.

- so the researcher tried the following:

```
https://www.target.com/-/x/us/us/open/user/get/test.css
```

<br>

- It caused a 404, so now information, but... `Cf-cache-status` changed to **MISS** again.

- easy bypass payload:

```
https://www.target.com/-/x/us/us/open/user/get;test.css
```

- This makes the web app think of `;test.css` as something similar to `?a=test.css`, so the app ignores it.

- But the caching server takes it as a static resource.

- Hence, accessing the page with private tab, lead to data exposure.


---

<br>

---

### 3. url encoding and path sequence

- A website was claiming that it was caching everything except anything under `/_api` endpoint.

```
/_api/ucenter/user-info
```

- initial status for `Cf-cache-status`: **DYNAMIC**

- tried payload with URL encoding:

```url
/any-cached-endpoint%2F../_api/ucenter/user-info
```

- The `Cf-cache-status` changed to **MISS**

- We all know this story :)

---
