from djongo import models as djmodels

class BoundingBoxes(djmodels.Model):
    id = djmodels.ObjectIdField()
    camera_id = djmodels.CharField(max_length=100)
    boxes = djmodels.TextField()