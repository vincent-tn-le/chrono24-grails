from astrapy.db import AstraDB

# Initialize the client
if __name__ == "__main__":
  db = AstraDB(
    token="AstraCS:BhaYzXhGWZSikiZEBOkXirKn:10076e0d3f8a61307016bc885e4eac436bd0799d33304d629ce3471f8ce7643e",
    api_endpoint="https://9e447e5f-dbe1-4564-b478-da00e00931ff-us-east-1.apps.astra.datastax.com")

  print(f"Connected to Astra DB: {db.get_collections()}")