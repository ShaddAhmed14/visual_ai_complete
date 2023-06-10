from django.shortcuts import render, HttpResponse
import glob
import json 
from .models import BoundingBoxes
from rest_framework.views import APIView
from rest_framework.response import Response

from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://shadd:shadd@mycluster.w3vx3s0.mongodb.net/?retryWrites=true&w=majority"
uri = "mongodb://shadd:shadd@ac-b7d9om0-shard-00-00.w3vx3s0.mongodb.net:27017,ac-b7d9om0-shard-00-01.w3vx3s0.mongodb.net:27017,ac-b7d9om0-shard-00-02.w3vx3s0.mongodb.net:27017/?ssl=true&replicaSet=atlas-9ct80r-shard-0&authSource=admin&retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Create your views here.

def home(request):
    return HttpResponse("Hello, world. You're at the backend homepage")

def addBoundingBox(request):
    # for now i read this txt file and add it to the database
    for i in glob.glob("/boxes/*.txt"):
        with open(i, "r") as f:
            data = f.read()
            print(data)
            data = json.dumps(data)
            print(data)
            BoundingBoxes.objects.create(camera_id="1", bounding_boxes=data)
    return HttpResponse("Added bounding boxes to database")
            
def emptyDataset(request):
    BoundingBoxes.objects.all().delete()
    return HttpResponse("Emptied database")

class addToDb(APIView):
    def post(self, request):
        print(request.data)
        
        id = request.data.get('camera_id')
        print("id: ", id)
        boxes = request.data.get('bounding_boxes')
        print("boxes: ",boxes)
        item = BoundingBoxes.objects.create(camera_id=id, boxes=boxes)
        print(item)
        return Response({"message": "Item created successfully"})