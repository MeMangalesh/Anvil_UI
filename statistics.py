import anvil.server
import base64
import mysql.connector
from mysql.connector import Error
from ultralytics import YOLO
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import io
import pymysql.cursors

#  Load the pre-trained YOLO model
model_path = r'C:\Users\Mangales\Desktop\App\fastapi-anvil\myenv\best.pt'
model = YOLO(model_path)

# Connect to Anvil Uplink
anvil.server.connect("server_IOWUOSI44HSF3N6E5SOYPSWC-I5OU23DJFFSG245Z")

@anvil.server.callable
##Code for testing passing values back to Anvil##

# def get_stats():
#     # Assuming you get these values from a database or calculations
#     total_images = 41  # Replace with your actual calculation
#     potholes_detected = 6  # Replace with your actual calculation
    
#     # Return the two values directly
#     return total_images, potholes_detected

#Code for testing passing values back to Anvil##

def get_statistics():
    connection = create_connection()
    if not connection:
        return {"status": "error", "message": "Database connection failed"}

    try:
        print("Inside get statistics try")
        # Use DictCursor specifically for this query
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            # Query to count total images
            query_total_images = """
            SELECT count(*) as total_images FROM image_data
            """
            cursor.execute(query_total_images)
            total_images_result = cursor.fetchone()

            # Query to count images with potholes detected
            query_potholes_detected = """
            SELECT count(*) as potholes_detected FROM image_data WHERE pothole_detected = 1
            """
            cursor.execute(query_potholes_detected)
            potholes_detected_result = cursor.fetchone()

            #####Check type
            
            print(f"type of total_images_result: {type(total_images_result)}, value: {total_images_result}")
            print(f"type of potholes_detected_result: {type(potholes_detected_result)}, value: {potholes_detected_result}")

            # Convert tuple results to integers
            if isinstance(total_images_result, tuple) and isinstance(potholes_detected_result, tuple):
                print("Inside isinstance")
                # Assign values to variables
                total_images = int(total_images_result[0])
                potholes_detected = int(potholes_detected_result[0])
                
                print(f"type of total_images: {total_images} and the type is: {type(total_images)}")

            #  # Extract values and convert to integers
                # total_images = int(total_images_result['total_images'])
                # potholes_detected = int(potholes_detected_result['potholes_detected'])
                # potholes_not_detected = total_images - potholes_detected

                return {#{"status": "error", "message": "Unexpected result format"}
                    "status": "success",
                    "data":(total_images, potholes_detected, )
                }

            else:
                # If results are not tuples
                print("Results are not in tuple format")
                # return {#{"status": "error", "message": "Unexpected result format"}
                #     "status": "success",
                #     "data":(total_images, potholes_detected, potholes_not_detected)
                # }
                # print(f"type of total_images_result after converting to int: {type(total_images)}, value: {total_images}")
                # print(f"type of potholes_detected_result after converting to int: {type(potholes_detected)}, value: {potholes_detected}")
                # print(f"potholes_not_detected : {type(potholes_not_detected)}, value: {potholes_not_detected}")


        return total_images, potholes_detected, potholes_not_detected
        
            #### end check type

            #     # Ensure results are tuples
            # if isinstance(total_images_result, tuple) and isinstance(potholes_detected_result, tuple):
            #     # Assign values to variables
            #     total_images = total_images_result[0]
            #     potholes_detected = potholes_detected_result[0]
            #     potholes_not_detected = total_images - potholes_detected

            #     print(f"total images processed: {total_images}")
            #     print(f"total potholes detected: {potholes_detected}")
            #     #print(f"total not potholes detected: {potholes_not_detected}")
                
            #     return total_images, potholes_detected #, potholes_not_detected
            # else:
            #     return {"status": "error", "message": "Unexpected result format"}

    except pymysql.Error as e:
        return {"status": "error", "message": f"Database error: {e}"}
    finally:
        if connection:
            connection.close()

######################
####  DATABASE    ####
######################

# Database connection function
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="dbpodv1",
            database="potholes"
        )
        return connection
    except Error as e:
        print(f"The error '{e}' occurred")
        return None

# Execute Query 
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

# Keep the script running
anvil.server.wait_forever()