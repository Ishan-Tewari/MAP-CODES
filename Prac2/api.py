from operator import ge
from movies import *

# read 
@app.route('/movies', methods=['GET'])
def get_all_movies():
    return jsonify({'Movies': Movie.get_all_movies()})

# read
@app.route('/movies/<int:id>', methods=['GET'])
def get_movie(id):
    query_result = Movie.get_movie(id)
    return jsonify(query_result)

# create
@app.route('/movies', methods=['POST'])
def add_movie():

    # request data of movie to be added from the client
    request_data = request.get_json()

    # add the movie with data given by client
    Movie.add_movie(
        request_data['title'],
        request_data['year'],
        request_data['genre']
    )

    # give response on successfull addition
    reponse = Response("Movie Added",201, mimetype="application/json")
    return reponse

# update
@app.route('/movies/<int:id>', methods=['PUT'])
def update_movie(id):

    # request data of movie to be added from the client
    request_data = request.get_json()

    # update the movie with data given by client
    Movie.update_movie(
        id,
        request_data['title'],
        request_data['year'],
        request_data['genre']
    )

    # give response on successfull updation
    reponse = Response("Movie Updated",200, mimetype="application/json")
    return reponse

# delete
@app.route('/movies/<int:id>', methods=['DELETE'])
def delete_movie(id):
    Movie.delete_movie(id)

    # give response on successfull deletion
    reponse = Response("Movie Deleted",200, mimetype="application/json")
    return reponse


if __name__ == "__main__":
    app.run(port=1234, debug=True)



