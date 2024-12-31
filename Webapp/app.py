from flask import Flask,render_template,request
import numpy as np
import pickle
import gzip

# finalpopularity = pickle.load(open('Model/finalpopularity.pkl', "rb"))

with gzip.open('Model/finaldf_compressed.gz', 'rb') as f:
    finaldf = pickle.load(f)

with gzip.open('Model/book_compressed.gz', 'rb') as f:
    book = pickle.load(f)
with gzip.open('Model/finalpopularitycompressed.gz', 'rb') as f:
    finalpopularity = pickle.load(f)
with gzip.open('Model/similarity_score_compressed.gz', 'rb') as f:
    similarityScore = pickle.load(f)
# book = pickle.load(open('Model/book.pkl', "rb"))

# similarityScore = pickle.load(open('Model/similarityScore.pkl', "rb"))

app = Flask(__name__,template_folder='templates',static_folder='static',static_url_path='/')
@app.route("/")
def start():
    return render_template("home.html",
                           bookName = list(finalpopularity["Book-Title"].values),
                           Image = list(finalpopularity["Image-URL-M"].values),
                           Isbn = list(finalpopularity["ISBN"].values),
                           bookauthor = list(finalpopularity["Book-Author"].values),
                           NoRating = list(finalpopularity["Book-Rating"].values),)
@app.route("/recommend")
def recommend():
    return render_template("recommend.html")

@app.route("/Userrecommend",methods = ["post"])
def Userrecommend():
    Userinput = request.form.get("Userinput")
    index = np.where(finaldf.index == Userinput)[0][0]
    similarBook = sorted(list(enumerate(similarityScore[index])),key = lambda x:x[1],reverse=True)[1:6]

    data = []
    for i in similarBook:
        item = []
        # print(finaldf.index[i[0]])
        tempdf = book[book["Book-Title"] == finaldf.index[i[0]]]
        item.extend(list(tempdf.drop_duplicates("Book-Title")["Book-Title"].values))
        item.extend(list(tempdf.drop_duplicates("Book-Title")["Image-URL-M"].values))
        item.extend(list(tempdf.drop_duplicates("Book-Title")["Book-Author"].values))
        item.extend(list(tempdf.drop_duplicates("Book-Title")["ISBN"].values))        
        data.append(item)
    print(data)
    return render_template("recommend.html", data=data,user_input=Userinput)





