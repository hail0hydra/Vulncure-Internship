# Writeup - Bypassing a login page and getting admin access on an internal training platform

- Researcher: [Louis Shyers](https://medium.com/@l_s_)

- writeup report [here](https://medium.com/@l_s_/bypassing-a-login-page-and-getting-full-admin-access-on-an-internal-training-platform-ff5abd88135e)

<br>
<br>

## Shodan

- searcher with `ssl:target.com 200`

- found

```
platform.com
```
<br>
<br>

## dirsearch

- `ReportServer`

- directory listing of reports.

- MSSQL Server Reporrting Services

![page](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*Q-u4B5jjr5oW-A4LAeHOJA.png)


- clicking on report, getting redirected to an internal endopoint like:

```
internal.platform/ReportServer/?%2fRegion&rs:Command=ListChildren.
```


- Just replaced `internal.platform/ReportServer` back to `platform.com/ReportServer` &  the report loaded!.

<br>
<br>

### Looking for sensitive information

- found one report that disclosed user’s full names and unique user IDs.

- reported, got response as just and INFORMATIONAL vulnerability.


<br>
<br>


###  Persistence: Juicy Stuff

- landed on a report named __“Content Usage”__ which was huge because it contained information on the ___most visited endpoints___ within that platform.

- on this report the researcher started noticing a pattern of where many of the endpoints followed this structure:

```
platform.com/app/region/courses.aspx

platform.com/app/region/calendar.aspx
```

- this page gave a 401 error , but new `dirsearch` potential endpoints, found:

```
platform.com/app/scripts/views/courses/
```

- I started _bruteforcing_ for _javascript_ files under __`courses/`__ and eventually got a hit for __`index.js`__.

-  In the JS file we could see how this page was being constructed without seeing the actual page and we got to know that it was utilizing the `Backbone.js framework`.

<br>
<br>

### Backbone.js

- Architecture

![arch](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*cxPmHnD_ZqWysLuCKJfyFQ.jpeg)


- the directory names under `views/` were the same name as the `.aspx` files listed on the __“Content Usage Report”__.

- logically there should be a `views/calendar/index.js` as well. Bingo. There was!

### time to look for more sensitive files

-  content usage report and found a reference to a __`users.aspx`__ file, so the researcher tried navigating to `views/users/index.js` and the file loaded!

- used for some administrative functions of managing users, found this snippet in the file:

```js
function addNewUser() {
 window.location = Platform.Paths.ControllerData + "/Users.aspx/manageUserProfile?userId=&searchValues=&actionType=A";
 }
```

- Knowing that the value for _`Platform.Paths.ControllerData`_ in the same script was __`platform.com/app/region/`__, he navigated to `platform.com/app/region/Users.aspx/manageUserProfile?userId=&searchValues=&actionType=A` and a portion of this admin page fully rendered on his browser.


>- BARRIER: you had to have an internal email address to create a user !

<br>
<br>

### User Search page

-  he removed the `userId=&searchValues=&actionType=A` parameters from the URL but that didn’t do much, it just broke the page and it wouldn’t load. He then removed `manageUserProfile` to make it:

```
platform.com/app/region/Users.aspx/
```

![user-search-page](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*yQO2XtR7B8m9NMmjhUhwlw.png)

- we have been here before?

>- __Single Forward Slash (/)__: URL that actually did load was `platform.com/app/location/Users.aspx/` the one that didn’t is `platform.com/app/location/Users.aspx` The difference here is a singular forward slash at the end of the URL!

- Using this technique researcher could access a lot of different admin functions/pages within the platform

<br>
<br>

### Next Steps

- Went on search page, just clicked search button, tried to go to a user profile and got and error.

- The link being loaded was:

```
platform.com/app/PageNotFound.aspx?aspxerrorpath=/app/region/Users.aspx/Users.aspx/manageUserProfile
```

- There’s a clear misconfiguration here that was appending `Users.aspx` twice on the URL!

- In __BurpSuite__, the request sent to server, when hitting the search button was:

```
platform.com/app/location/Users.aspx/Users.aspx/manageUserProfile?userId={}&searchValues=&actionType=E
```

- removed one of the `Users.aspx`, and got the __EDIT PROFILE PAGE__ for the user.

- request when initially loaded the profile:

![reqprof](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*cWanuH_rDn94N9y9tu-EYg.png)


- couldnt change anything with the user edit form. Because the server was sending our broswer requests to know what kind of user we are and our access over its resources.


<br>
<br>

### Incoming: Response Manipulation

- intercepting a HTTP response from a server and changing it’s values before it hits your browser.

- The page asks the server if this profile should be read only to which the server responds YES (the number 1 in the screenshot above). disabling all the fields

- Intercepting this response and changing it to `0` made all the buttons editable and clickable!

<br>

> [IMPORTANT]
>  __had write access to any user profiles!__
> __modify and or delete an upwards of an 50000+ accounts, completely unauthenticated__

