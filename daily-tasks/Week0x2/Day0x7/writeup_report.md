# Bypassing airport security via SQL injection

- The writeup can be read [here](https://ian.sh/tsa)

- The researchers are:

1. [Ian Carrol](https://twitter.com/iangcarroll)

2. [Sam Curry](https://twitter.com/samwcyo)


<br>
<br>

## Summary

- Getting high level clearance in the Airport just because of a simple plain SQL injection attack

<br>
<br>

## Details

- The airport normally have two systems:

1. KCM - Known Crew Memeber: If you are a known crewmember you will be able to bypass physical security checks.

2. CASS - Cockpit Access Security System: To access the jumpseat in Cockpit, you need to be a verified pilot. Also something bypassing physical security checks


- The way this was handled was via [ARINC](https://en.wikipedia.org/wiki/ARINC)

- Currently 76 airlines are registered with it:

```js
document.querySelectorAll('.ms-formsbody').length
```

- But what about small airlines?


- That is where [FlyCASS.com](https://www.flycass.com/) comes in!

- It pitches for you and provides those KCM and CASS checks.

<br>
<br>

## Next Steps

- The researchers were able to find many login endpoints for each different airline.

- For example for __Air Transport International (8C)__:

```
https://flycass.com/ati/
```

- It had a login page. They tried a single quote `'`

![disaster](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/7ed29a04-c03b-44f4-934d-107be6abbc1a/Untitled/w=1920,quality=90,fit=scale-down)

- Soon __sqlmap__ was brought into play.

- The researchers were ADMIN of ati!

<br>
<br>

## Finals

- They were able to see all lists of pilots and crewemebers applied for the bypass system.

![1](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/c87f2023-3162-45ba-b76e-5c976807e690/Untitled/w=1920,quality=90,fit=scale-down)

- This did not require any further authorization. Once you are admin, you are IT.


- They tried adding their own account with images, that are used physically to cross verify:

![approved](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/c8f35f9c-f7f9-433d-8479-4c07b1668218/Untitled/w=1920,quality=90,fit=scale-down)

- APPROVED!

- Full Access to anything serious.
