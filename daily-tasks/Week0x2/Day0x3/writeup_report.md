# Writeup - Critical information disclosure on Wappalyzer.com

- Researcher: [Davide Tampellini](https://x.com/tampe125)

- Date of report: 24th March 2017

<br>
<br>

## Summary

- How a simple dirbuster brute force enumeration of available directories on a prominently used tool's website, lead to complete Admin level information disclosure.

- Could have lead to access of Admin level functionalities, but the attacker never tried.

> - __Doubt__: should someone in this case, try to at-least download one file?

<br>
<br>

## Details

- while working on one project and continually using `Wappalyzer`, the researcher came across an article about how the recon never ends.

- here is the article [SQLi+XXE+File path traversal Deutsche Telekom]()

- so just out of curiosity, the researhcer started fuzzing __wappalyzer.com__

- here is something interesting he saw:

![admin](https://www.nc-lp.com/user/pages/01.blog/critical-information-disclosure-on-wappalyzer-com/wappalyzer_dirbuster_1.png)

- we can see __`admin:401`__, but that is not where it stops:

![Admin](https://www.nc-lp.com/user/pages/01.blog/critical-information-disclosure-on-wappalyzer-com/wappalyzer_dirbuster_results.png)


- An __`Admin:200`__ ???


- It was this easy

<br>
<br>

## Proof of Concept

- Below are some findings the researcher did, once he accessed the CASE SenSitiVe, __/Admin__ directory:

![admin panel](https://www.nc-lp.com/user/pages/01.blog/critical-information-disclosure-on-wappalyzer-com/wappalyzer_admin_resize.png)

- These image shows the most recent orders and their value. The only visible email researcher's my own personal address

![functions](https://www.nc-lp.com/user/pages/01.blog/critical-information-disclosure-on-wappalyzer-com/wappalyzer_order_resize.png)

<br>
<br>

## Conclusion

- Once the access was confirmed, below is the timeline for how much time it took for the issue to be resolved!

```
2017-03-20    Initial report to Wappalyzer
2017-03-20    Fix by the vendor
2017-03-24    Full disclosure
```
