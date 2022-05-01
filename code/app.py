from flask import Flask,request
from flask_restful import Resource,Api



app = Flask(__name__)
api=Api(app)

records = []

class Entitle(Resource):
    
    def get(self , id):
        # for record in records:
        #     if record['id'] == id:
        #         return record
        
          record = next(filter(lambda x: x['id']==id, records), None)
          return {'record': Entitle}, 200 if record  else 404
    
    
    def post(self, id):
         if next(filter(lambda x: x['id']==id, records), None):
             return {'message':"An item with name '{}' already exists".format(id)},400
             return {'record': Entitle}, 200 if record  else 404
             
         
         data = request.get_json()
         record ={'id':id, 'group_no':data['group_no'], 'allowed':data['allowed'], 'remaining':data['remaining'],'change':data['change'],'changed_on':data['changed_on']}
         records.append(record) 
         return record, 201

        
    # def delete(self, id):
    #     global records
    #     records = list(filter(lambda x:x['id'] != id, records))   
    #     return {'message':'Item deleted'} 
    
    
    # def put(self ,id):
    #     data = request.get_json()
    #     record = next(filter(lambda x:x['id'] == id , records), None)
    #     if record is None:
    #         record = {'id':id, 'group_no':data['group_no'], 'allowed':data['allowed'], 'remaining':data['remaining'],'change':data['change'],'changed_on':data['changed_on']}
    #         records.append(record)
    #     else:
    #         record.update(data)    
    
    #     return record
        
        
class EntitleList(Resource):
    def get(self):
        return {'records':records}
        


api.add_resource(Entitle, '/entitlement/<string:id>')
api.add_resource(EntitleList, '/records')
app.run(port=5000, debug=True)