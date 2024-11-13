#!/usr/bin/env python3
from flask import request, make_response, jsonify
from flask_restful import Resource
from config import app, api
import re

image_store = []

class Images(Resource):
    def get(self):
        global image_store
        if not image_store:
            image_data = [
                {
                    "image_id": "001",
                    "timestamp": "2024-09-24 14:31:05",
                    "latitude": "44.4280° N",
                    "longitude": "110.5885° W",
                    "altitude_m": 50,
                    "heading_deg": 270,
                    "file_name": "YNP_001.jpg",
                    "camera_tilt_deg": -15,
                    "focal_length_mm": 24,
                    "iso": 100,
                    "shutter_speed": "1/500",
                    "aperture": "f/2.8",
                    "color_temp_k": 5600,
                    "image_format": "RAW+JPEG",
                    "file_size_mb": 25.4,
                    "drone_speed_mps": 5.2,
                    "battery_level_pct": 98,
                    "gps_accuracy_m": 0.5,
                    "gimbal_mode": "Follow",
                    "subject_detection": "Yes",
                    "image_tags": ["Geyser", "Steam"],
                    "id": "b298"
                },
                {
                    "image_id": "002",
                    "timestamp": "2024-09-24 14:33:22",
                    "latitude": "44.4279° N",
                    "longitude": "110.5890° W",
                    "altitude_m": 75,
                    "heading_deg": 180,
                    "file_name": "YNP_002.jpg",
                    "camera_tilt_deg": -30,
                    "focal_length_mm": 35,
                    "iso": 200,
                    "shutter_speed": "1/1000",
                    "aperture": "f/4",
                    "color_temp_k": 5200,
                    "image_format": "RAW+JPEG",
                    "file_size_mb": 27.1,
                    "drone_speed_mps": 3.8,
                    "battery_level_pct": 95,
                    "gps_accuracy_m": 0.6,
                    "gimbal_mode": "Free",
                    "subject_detection": "No",
                    "image_tags": ["Forest", "River"],
                    "id": "434b"
                },
                {
                    "image_id": "003",
                    "timestamp": "2024-09-24 14:36:47",
                    "latitude": "44.4275° N",
                    "longitude": "110.5888° W",
                    "altitude_m": 100,
                    "heading_deg": 90,
                    "file_name": "YNP_003.jpg",
                    "camera_tilt_deg": 0,
                    "focal_length_mm": 50,
                    "iso": 400,
                    "shutter_speed": "1/2000",
                    "aperture": "f/5.6",
                    "color_temp_k": 5800,
                    "image_format": "RAW+JPEG",
                    "file_size_mb": 26.8,
                    "drone_speed_mps": 2.5,
                    "battery_level_pct": 91,
                    "gps_accuracy_m": 0.4,
                    "gimbal_mode": "Tripod",
                    "subject_detection": "Yes",
                    "image_tags": [
                        "Wildlife",
                        "Elk"
                    ],
                    "id": "b624"
                },
                {
                    "image_id": "004",
                    "timestamp": "2024-09-24 14:40:13",
                    "latitude": "44.4277° N",
                    "longitude": "110.5882° W",
                    "altitude_m": 120,
                    "heading_deg": 0,
                    "file_name": "YNP_004.jpg",
                    "camera_tilt_deg": -45,
                    "focal_length_mm": 70,
                    "iso": 800,
                    "shutter_speed": "1/4000",
                    "aperture": "f/8",
                    "color_temp_k": 6000,
                    "image_format": "RAW+JPEG",
                    "file_size_mb": 28.3,
                    "drone_speed_mps": 1.2,
                    "battery_level_pct": 87,
                    "gps_accuracy_m": 0.7,
                    "gimbal_mode": "Follow",
                    "subject_detection": "No",
                    "image_tags": [
                        "Canyon",
                        "Waterfall"
                    ],
                    "id": "f17b"
                },
                {
                    "image_id": "005",
                    "timestamp": "2024-09-24 14:44:56",
                    "latitude": "44.4282° N",
                    "longitude": "110.5879° W",
                    "altitude_m": 80,
                    "heading_deg": 315,
                    "file_name": "YNP_005.jpg",
                    "camera_tilt_deg": -10,
                    "focal_length_mm": 24,
                    "iso": 100,
                    "shutter_speed": "1/250",
                    "aperture": "f/2.8",
                    "color_temp_k": 5400,
                    "image_format": "RAW+JPEG",
                    "file_size_mb": 24.9,
                    "drone_speed_mps": 6.7,
                    "battery_level_pct": 82,
                    "gps_accuracy_m": 0.5,
                    "gimbal_mode": "Free",
                    "subject_detection": "Yes",
                    "image_tags": [
                        "Thermal Pool",
                        "Bacteria"
                    ],
                    "id": "7f92"
                },
            ]
            
            for img_data in image_data:
                image_store.append(img_data)
        return make_response(jsonify(image_store), 200)
    
class ImageInfo(Resource):
    def get(self, image_id):
        global image_store
        image = next((img for img in image_store if img["image_id"] == image_id), None)
        if image:
            return make_response(jsonify(image), 200)
        else:
            return make_response(jsonify({'error': 'Image not found'}), 404)

    def post(self):
        global image_store
        data = request.get_json()
        query = data.get('query').lower()
        
        response_data = {}
        
        # Extract the first integer found in the query
        image_id_match = re.search(r'\d+', query)
        if image_id_match:
            image_id = int(image_id_match.group(0))  # Extracts the integer from the query
            # Compare image_id without leading zeros
            image = next((img for img in image_store if int(img["image_id"].lstrip('0')) == image_id), None)
            if image:
                attribute_keywords = {
                    'timestamp': 'timestamp',
                    'latitude': 'latitude',
                    'longitude': 'longitude',
                    'altitude': 'altitude_m',
                    'heading': 'heading_deg',
                    'file name': 'file_name',
                    'camera tilt': 'camera_tilt_deg',
                    'focal length': 'focal_length_mm',
                    'iso': 'iso',
                    'shutter speed': 'shutter_speed',
                    'aperture': 'aperture',
                    'color temperature': 'color_temp_k',
                    'image format': 'image_format',
                    'file size': 'file_size_mb',
                    'drone speed': 'drone_speed_mps',
                    'battery level': 'battery_level_pct',
                    'gps accuracy': 'gps_accuracy_m',
                    'gimbal mode': 'gimbal_mode',
                    'subject detection': 'subject_detection',
                    'tags': 'image_tags'
                }
                
                attribute = next((attribute_keywords[key] for key in attribute_keywords if key in query), None)
                
                if attribute and attribute in image:
                    response_data = {'message': f'The {attribute} of image {image_id:03d} is {image[attribute]}.'}
                else:
                    response_data = {'message': f'Attribute not found or supported in image {image_id:03d}.'}
            else:
                response_data = {'message': f'Image with ID {image_id:03d} not found.'}
        else:
            response_data = {'message': 'Image ID not recognized or supported.'}
        
        return make_response(jsonify(response_data), 200)



api.add_resource(Images, '/images')
api.add_resource(ImageInfo, '/images/query')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
