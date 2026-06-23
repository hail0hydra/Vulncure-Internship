# Privacy Violation in Chat System

- Researcher [Rashsahacks AKA Inderjeet](https://hackerone.com/encodedguy?type=user)

<br>
<br>

## Summary

- A bug in a chatting application, which lets user delete their messages, and files attached, but it doesn't really delete the file attached. 

- The messages disappear, but the files persist. Not deleted. Leak of PII

<br>
<br>

## Impact

- Medium Severity

<br>
<br>

## Details

- The chat application was analyzed by the researcher, when creating a message, It was associated with a `message-id`.


- same was the case with any files. When attaching/uploading files, it was associated with `file-id`

<br>

#### The issue

- When the researcher deleted the message, and tried accessing it with the `message-id` as before, he couldn't. That is a good thing.

- But when he tried accessing the files with `file-id` or more specifically, the pre-signed url, which required `file-id` to generate a resource link, he was able to still access it.

- It was not expiring, it was getting accessed even after deletion.

<br>
<br>

## Reporting Timeline

![timeline](https://web.archive.org/web/20221118174721im_/https://rashahacks.com/content/images/2022/11/image-39.png)
