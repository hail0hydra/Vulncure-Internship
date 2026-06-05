# Writeup - How I found 3 rare security bugs in a day

<br>

- writeup can be found at [this](https://infosecwriteups.com/how-i-found-3-bug-bounties-in-a-day-c82fe023716e) link.


<br>
<br>

## Description

- This writeup is about 3 different bugs found on the same website, they weren't chained together or anything, just 3 isolated bugs in a website.

- the target website is a __Travel and Trip Company__. The researcher got to know about this target from Hackerone.

- These 3 vulnerabilities seem very trivial and things of common sense but it just shows how important it is to follow every aspect of attack methodology.

<br>
<br>


## Details

- The author & researcher of these 3 bugs is [zer0dac](https://zer0dac.medium.com/)

- The 3 bugs are namely:

1. Bypassing Single Sign-in link

2. Credit Card Checker Bypass

3. No Rate Limit, leading to potential Email bombing

<br>
<br>

## Methodology

### Bug 1: single sing-in Link


- The researcher used email login to create an account over the target website, which after entering the email sends a link to sing-in, claiming that it is valid for just one time and it will expire in 10 minutes.

- The researcher signs-in with the link, then opens the sing-in link in a private browser window.

![success=false](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*tnAthJpgZ8EEKm9F7TNqWw.png)

- It can be seen that in the end of the link, there is a parameter saying `success=false`.

- Simply changing this value to __true__, it was BYPASSED easily.

<br>
<br>

### Bug 2: Credit card checker

- since this website is for travel and tourists, if would have payment options, one of them being credit card.

- there was specifically a `Cread Card Checker` function at the following endpoint:

```
/hi/ccui/getcarddata
```

- below is screenshot showcasing the __POST__ request for credit card and its response:

![credit-card-function](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*tmjSQMa1kWhd09eZ53h33g.png)


- as we can see the body takes 2 parameters are request:

```
cardFirstSix=123123

cardLength=6
```

- as explained by the researcher, it was checking the __first six digits__ of the card.

- the researcher was able to bypass this function by changing the request body parameters to the following:

```
cardFirst=454545&cardLength=16
```

- we can see the req-res output in Burpsuite below:

![card-bypass](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*zGpVRFiv1Ge-BIKlKiJjsQ.png)


- This was a little confusing to understand, and I have doubts about it too. But I made this explanation for it:

#### Explanation for Card bypass

- since `VISA` cards start with 4 and are generally 16 characters in length, the payload makes sense.

- but why exactly did it work, was not mentioned in the writeup.

- It might be the case where the card length is not getting verified and is user controlled variable only!

- if that is the case then the backend logic might look like:

```python
if cardLength == 16 and cardFirstSix.startswith("4"):
    return "VISA"
```

instead of:

```python
if len(cardFirstSix) == 16:
    validate()
    #...
```

- So this is Client Controlled Validation Logic

- something similar to what we saw in the first bug, where we set `success=true`

<br>
<br>

### Bug 3: Email-verification & Potential Email Bombing

- The researcher mentioned that there was a button for setting up notifications in case of cheaper travel options.

- When you click on that, you have to enter your email for the notification.

![email](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*-Do-BK_YNwFHsGb1HdfqeQ.png)


- The logic flow is like this:

1. You enter your Email

2. You receive an inbox to verify that you need a notification

3. You start receiving them


- But the bug was at __step 2__!

- The researcher noticed that even without verifying the notification for receiving mail, he was still getting the mails.

- The request inn Burpsuite for opting-in for the notification looks like this:

![notification](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*jJz_-uKd6SZt05RzaRBqnA.png)


- even though the response looks like a negative feedback, but emails are still getting generated.

- This could potentially be used for Email-Bombing if you have a Database of Emails lying around.

