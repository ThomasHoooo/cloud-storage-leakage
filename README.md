# cloud-storage-leakage

As cloud services are getting more and more popular, many users, including companies and organisations, are not utilising these resources carefully and this poses a threat on the data they store on cloud. As I was doing my internship, I saw that even big companies will have a chance to have misconfigured buckets and thus, I have decided to do a scan on S&P top 500 companies and Alexa top 10000 domains to check whether they have protected their data securely.

I have carried out scans on two most popular cloud providers, which is Amazon Web Service (AWS) and Google Cloud Platform (GCP). I wrote scripts that will scan for open buckets on these services by adding a few permutations of bucket names and checked whether these buckets are public.

Initially, I only did a scan on S&P top 500 companies and to my shock, there were so many public buckets that allow listing of contents! There are a total of 135 public buckets which are related to S&P 500 companies. As I was browsing through the listings of these buckets, some even included confidential secrets and information which should be stored private. 

After reporting these findings to my mentor, WatchTowr’s Principal Security Researcher Samuel Pua, he told me that I will be even more surprised if I do these scans on Alexa top 10000 domains as there will be more results and owners of these websites might be less aware of the current security threats as well. Due to my curiosity, I started to do more hunts on these domains. 

My script took me almost 30 hours to finish running on each service (it was mentally draining while waiting for the results), which sums up to 60 hours in total, as there were 120000 buckets to scan on each cloud provider. Nonetheless, I was able to get interesting results after a long wait. There are 106 and 590 public buckets related to Alexa top 10000 domains on AWS and GCP respectively, where most of them allow read permissions, with a little handful of them allowing write permissions. 

These buckets are dangerous as it may lead to:
Data breaching
Gaining control of the service hosted at the bucket by malicious users

Additionally, I tried testing my permissions on these buckets and realised that some of these buckets even have public bucket policies. Out of the 696 public buckets that I discovered, 79 buckets have public policies (11%) and I even have write permissions to modify some of them. 

Due to legal reasons, it is challenging for me to verify whether these buckets belong to the domains or companies. However, I urge these bucket owners to configure these buckets securely and block public access to these buckets before any damage is done.

All results and scripts are documented at https://github.com/ThomasHoooo/cloud-storage-leakage. 
