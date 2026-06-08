# Accidental IDOR that Deleted Admin Account.

<br>
<br>

## Summary

- This is a report about a bug, that was not found intentionally and happened just because  of habit.

- The researcher found an IDOR, or more like got to know about it after he had exploited it.


<br>
<br>

## Impact

- High/Critical, but from the context of the program, it was a private program and not a big deal, but in real life scenario, this would've been a bug deal.

<br>
<br>

## Details

- The attacker was able to find some simple rate limit issue, that did not make much bounty

- While browsing and spidering, he had made a request as follows:

![req](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*fdcQGf1BAWN_lQWO2ONUrg.jpeg)



- visible here in the `DELETE` account api, are several numbers. So he just subconsciously sent a request to:

```
DELETE /api/corporates/practice/members/1 HTTP/1.1
```

- changed the last `id` kind of REST styled parameter to 1. and closed his laptop.


- after some time he could see a notification pop up.

![admin](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*e2XhBx8qcjgEx_5mKonfYg.jpeg)

- This lead to a $300 bounty for IDOR, since this meant he could delete any user. Also a $25 bounty for initial rate limiting bug, about which much details are not mentioned.
