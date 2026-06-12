## Techs

---

1. `X-Xsrf-Token`

- Got to know about `X-Xsrf-Token` header. This is also used for CSRF token and CSRF attack prevention.

- The Cookie in this case is automatically read by the JS

---

2. `SameSite` attribute

- Cookies have `SameSite` attribute as well in addition to **Secure** and **HTTPOnly**.

- It can have two values: `Lax` and `Strict`.

- **Strict** prohibits CSRF tokens to be attached to any kind of Cross Site Requests.

- **Lax**, (I think short for relax), gives some relaxation, only mainly focusing on POST cross site request and locking them. Cross Site GET are allowed.

---
