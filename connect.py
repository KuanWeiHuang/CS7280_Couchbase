# these modules are used to access and authenticate with your database cluster:
from couchbase.cluster import Cluster, ClusterOptions
from couchbase_core.cluster import PasswordAuthenticator
import data 

# specify the cluster and specify an authenticator containing a username and password to be passed to the cluster.

cluster = Cluster('couchbase://localhost', ClusterOptions(PasswordAuthenticator('cs7280_user', 'test1234')))

# following a successful authentication, a bucket can be opened.
# access a bucket in that cluster

bucket = cluster.bucket('travel-sample') # get a reference to the travel-sample bucket
coll = bucket.default_collection() # get a reference to the default collection

# CRUD operations
# Create: upsert a document into travel-sample bucket
def upsert_document(doc):
  print("\nUpsert")
  try:
    # key will equal: "airline_8091"
    key = doc["type"] + "_" + str(doc["id"])
    result = coll.upsert(key, doc)
    print("CAS: ", result.cas) # The CAS is a value representing the current state of an item
  except Exception as e:
    print(e)

for airline in data.airlines:
  upsert_document(airline)

# Retrieve: get a document from travel-sample bucket by the doc id
# get document function
def get_airline_by_key(key):
  print("\nGet Result: ")
  try:
    result = coll.get(key)
    print(result.content_as[str])
  except Exception as e:
    print(e)

get_airline_by_key("airline_8091")

# Query with N1QL
print("\nQuery with N1QL:")
query_result = cluster.query('SELECT * FROM `travel-sample` WHERE name=$1', "Couchbase Airways")
for row in query_result:
  print(row)

# Update: update an existing doc
airline = data.airlines[0]
airline["alliance"] = "Star Alliance"
upsert_document(airline)
get_airline_by_key("airline_8091")


# Remove: delete an existing doc
def delete_airline_by_key(key):
  ok = coll.remove(key).success
  if ok:
    print("\nremove", key, "successfully!")
  else:
    print("warning: cannot remove doc id:", key)
  

delete_airline_by_key("airline_8091") 


for airline in data.airlines:
  upsert_document(airline)