from flask import Flask, jsonify, request
import json
import os

file_path = os.path.join(os.path.dirname(__file__), 'C:/PythonProject/config/equipment.json')
with open(file_path, 'r') as f:
     equipment = json.load(f)

app=Flask(__name__)

@app.get("/api/equipment")
def get_equipment():
    return jsonify(list(equipment.values())), 200

@app.get("/api/equipment/<int:equipment_id>")
def get_equipment_by_id(equipment_id):
    equipment_item = equipment.get(str(equipment_id))
    if equipment_item:
        return jsonify([equipment_item]), 200
    else:
        return jsonify({"error": "Equipment not found"}), 404
    
if __name__=="__main__":
    app.run(port=5001,debug=False)