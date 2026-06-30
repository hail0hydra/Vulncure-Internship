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

- writeup [here](https://notsosecure.com/exploiting-ssrf-aws-elastic-beanstalk)

- Cool SSRF and how it can be leveraged to further get an RCE, via CI/CD pipelines.


<br>
<br>

### 2. CSRF

- writeup [here](https://hackerone.com/reports/301862)

- hard to understand this report.

<br>
<br>


### 3. Arbitrary File Uploads

- writeup [here](https://machevalia.blog/blog/remote-code-execution-in-tgz-file-upload)

- Cool file upload, concerning a `.tgz` file and its content. Because of discrepancies between how the filtering logic and how server treated the file.

- The concerned company didnt fix the logic, but restricted access to files!


<br>
<br>

### 4. Path Traversal/Local File Inclusion

- writeup [here](https://hackerone.com/reports/827052)

- Critical File inclusion with path traversal sequence in GitLab, due to improper checking of file and their types.


<br>
<br>

### 5. IDOR - Insecure Direct Object Reference

- writeup [here](https://hackerone.com/reports/149907)

- Adding a customized CSV as a datasource and changing the `datasource_id` leads to access to sensitive information of unauthorized data.
