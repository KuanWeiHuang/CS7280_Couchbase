# CS7280 Special Topics in Database
## Project 2: Couchbase

### Introduction
Couchbase Server, originally known as Membase, is an open-source, distributed, JSON document database. Couchbase is used to support applications where a flexible data model, easy scalability, and consistent high performance are required, such as tracking real-time user activity or providing a store of user preferences or online applications. It is written using C++, Erlang, C, Go languages. Its server is designed to provide us with easy-to-scale key-value or JSON document access with high sustained throughput and low latency. This repo would demo the first step of using Couchbase, including installation, configuration and basic CRUD operation using python SDK.

### Installation Process
1. Download Couchbase Server Community Edition from https://www.couchbase.com/downloads
2. Install it locally on your computer (https://docs.couchbase.com/tutorials/getting-started-ce/install-manage/tutorial_en.html)
3. Go to http://localhost:8091 to access the couchbase server

### Configurations
1. Setup New Cluster, configure it as following:
![Configurations](/images/cluster-configuration.png)
2. Go to "Buckets" tab on the side bar and click "ADD BUCKET" in the top right corner. Configure the bucket as following:
![Bucket Configurations](/images/bucket-configuration.png)
3. Go to the "Query" tab on the side bar and create primary index for "travel-sample" bucket. (In order to use N1QL, we have to create primary index)
![Create Primary Index](/images/create-primary-index.png)
4. Go to the "Security" tab on the side bar and click "ADD USER" in the top right corner. Configure the user as following(password is test1234): 
![Add User](/images/user-configuration.png)

### Install Python SDK and run the application code
(https://docs.couchbase.com/python-sdk/current/hello-world/start-using-sdk.html)

1. install the latest python SDK 
```
sudo -H python3 -m pip install couchbase
``` 
2. run `python3 connect.py` in the terminal, the result should be as following:
![Result](/images/result.png)
3. The result shows that we upsert 3 documents from `data.py` into the `travel-sample` bucket, retrive documents using its key, update an existing document and delete 1 document(CRUD operations).

### Query Workbench in the Couchbase UI:
We can use the built-in query workbench to query the bucket. Go to the query tab and insert `` SELECT * FROM `travel-sample` `` after executing `connect.py`, the result should be as following:
![Query Workbench](/images/query-workbench.png)


### Terms

N1QL:
According to Couchbase, N1QL is a JSON query language for executing industry-standard ANSI joins and querying, transforming, and manipulating JSON data – just like SQL.
The most important difference between N1QL and SQL is the data model. Other notable differences relate to the projection, selection, and filtering of data.

Data Bucket: a logical container of uniquely keyed documents. Logically related documents roughly equate to a "table", but tge schema is not enforced by Couchbase. We need different buckets because caching, replication and indexing on bucket level in Couchbase.

### References

https://docs.couchbase.com/python-sdk/3.0/hello-world/start-using-sdk.html
https://docs.couchbase.com/python-sdk/3.0/concept-docs/documents.html
https://www.youtube.com/watch?v=cyN_Az0110E&t=7s
https://docs.couchbase.com/python-sdk/current/hello-world/start-using-sdk.html

