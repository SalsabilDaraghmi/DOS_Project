from flask import Flask, json, jsonify ,render_template
from flask import request
import requests
from flask_sqlalchemy import SQLAlchemy
import html_to_json


#initial app
app = Flask(__name__)

#==============================================================================================
#============================ Catalog server requests ===========================================
#==============================================================================================


#============================= 1- search operation ====================================
#getting the books info which have the topic s_topic #request to catalogServer
@app.route('/search/<topic>', methods=['GET']) # wait for requist http://192.168.1.84:5000/search/ operation type Get
def search(topic): # this function for response
  result = requests.get("http://192.168.1.60:5000/search/"+str(topic)) #send request to catalog server which ip address is =http://192.168.1.60:5000
  return (result.content)


#============================== 2- info operation ====================================
#send request to the cataloge server to get information about id book
@app.route('/info/<int:bookID>', methods=['GET'])
def get_info(bookID):
  #this is the request to be sent to the catalog server
  result = requests.get("http://192.168.1.60:5000/info/"+str(bookID))
  return (result.content)

#============================= 3- update price ========================================

#update the price of a book 
@app.route('/update_price/<int:bookID>', methods=['PUT'])
def update_book_price(bookID):
  price = request.json['price']
  result = requests.put("http://192.168.1.60:5000/update_price/"+str(bookID),data={'price':price})
  return (result.content)

#============================= 4- update quantity ========================================

            #=================== increease quantity =================
 
@app.route('/increase_quantity/<int:bookID>', methods=['PUT'])
def increase_book_quantity(bookID):
  new_amount = request.json['new_amount']
  result = requests.put("http://192.168.1.60:5000/increase_quantity/"+str(bookID),data={'new_amount':new_amount})
  return (result.content)

            #=================== decreease quantity =================
 
@app.route('/decrease_quantity/<int:bookID>', methods=['PUT'])
def decrease_book_quantity(bookID):
  new_amount = request.json['new_amount']
  result = requests.put("http://192.168.1.60:5000/decrease_quantity/"+str(bookID),data={'new_amount':new_amount})
  return (result.content)


#==============================================================================================
#============================ Order server requests ===========================================
#==============================================================================================

#====================== purchase ====================================================
@app.route('/purchase/<int:bookID>', methods=['PUT'])
def purchase(bookID):
  r = requests.put("http://192.168.1.50:5000/purchase/"+str(bookID)) 
  return (r.content)


if __name__=="__main__":
    app.run(debug=True)