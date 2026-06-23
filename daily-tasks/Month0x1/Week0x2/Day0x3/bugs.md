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

- writeup [here](https://nechudav.blogspot.com/2021/12/ssrf-vulnerability-in-appsheet-google.html?utm_source=bugbountydaily.com&utm_medium=referral)

- saw a new term called `WebHook`

- using redirection to `GET` the work done! [ref](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Redirections)


<br>
<br>

### 2. CSRF

- writeup [here](https://shahjerry33.medium.com/csrf-with-idor-a-deadly-combo-203e93967702)

- account name is the eye of the eye DOOR?

- ofcourse the CSRF token isnt present so CSRF request can be sent

- But the __Cookie__ is there!

- So the malicious website of supposed to send 100000000 CSRF requests?

<br>
<br>


### 3. Arbitrary File Uploads

- writeup [here](https://blog.sicuranext.com/breaking-down-multipart-parsers-validation-bypass/?utm_source=bugbountydaily.com&utm_medium=referral)


>_in order to make the webserver to proxy_pass the content of the file to fastcgi or similar._

- what does the above statement mean



- just crrrazzzyyy!

- Learnt how so many trusted WAFs by not following the strict RFC guidelines, allow bypass for file upload!

- just modify `x-www-form-urlencoded` to `multipart/form-data`. __Content-Type__ HEADER

- `multipart-formdata` parsers are... something.

- issues from the side of [PHP](https://bugs.php.net/bug.php?id=81987&ref=blog.sicuranext.com)

<br>
<br>

### 4. Path Traversal

- writeup [here](https://jorianwoltjer.com/blog/p/coding/cache-deception-on-my-new-site?utm_source=bugbountydaily.com&utm_medium=referral)

- new term: __[Cache Deception](./notes/notes.md)__


<br>
<br>

### 5. IDOR - Insecure Direct Object Reference

- writeup [here](https://infosecwriteups.com/api-based-idor-to-leaking-private-ip-address-of-6000-businesses-6bc085ac6a6f)

- learnt that even though __CSRF__ tokens are there, even though __Cookies__ are in place, `IDOR` can still occur.

- I used to think a simple IDOR request would look something like:

```
GET /user/profile/logs/1234 HTTP/1.1
Host: redacted.com

#no cookies, no csrf
```

- but it can still occur, even if the {user, request} identifiers are present!
