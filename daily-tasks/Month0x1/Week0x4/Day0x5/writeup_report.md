# Logic Flaw: I Can Block You from Accessing Your Own Account

- The writeup can be read [here](https://hashimamin.medium.com/logic-flaw-i-can-block-you-from-accessing-your-own-account-63fc2a88bb72)

- The researcher is [Hashim Amin](https://hashimamin.medium.com/)

<br>

---

## Summary

- Any legitimate account can be blocked access to their profile.

<br>
<br>

---

## Details

- The application maintains a forum, where users can create posts and respond to them.

- Depending on your activities, a leaderboard is generated.

- The researcher was able to Identify a logic flaw which led him to easily climb the leaderboard.

![post](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*jbscVGcTPTvbCUQsDx3mcg.png)

<br>

---

### Leaderboard Bypass

- It required 3 requests:

    1. Like a POST

    2. Unlike the same POST

    3. Go the user profile of the person who created the POST


- By alternating between these 3, an attacker can gain a ton of points to climb the leaderboard.

![leaderboard](https://miro.medium.com/v2/resize:fit:1152/format:webp/1*P4txlb1cCsM_ptE6NXHOTg.png)

- But for some reason, due to so much traffic, the legitimate account which created the post, gets blocked.

![blocked](https://miro.medium.com/v2/resize:fit:1152/format:webp/1*NsHI6IJds06dCLmkop7D4w.png)


<br>
<br>

---

## Next Steps

- So the attacker can target any legitimate account and stop their access to their own accounts.

- Although this has a high impact in theory, this bug was termed as INFORMATIONAL by the triagers.

![report](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*GXZ4_YX_W332eNMVKdIIEg.png)
