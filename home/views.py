from django.shortcuts import render
from home.forms import CommentForm

#ml logic
import pickle
import tensorflow as tf
from keras.preprocessing.sequence import pad_sequences
import numpy as np 
max_features = 20000
maxlen = 100
with open('static/my_model/tokenizer.pickle', 'rb') as handle:
              tokenizer = pickle.load(handle)
new_model = tf.keras.models.load_model("static/my_model")  

def predict(commentlist):
    comment=commentlist[0]
    list_tokenized_test = tokenizer.texts_to_sequences([comment])
    X_te = pad_sequences(list_tokenized_test,maxlen=maxlen)
    y_test = new_model.predict([X_te], batch_size=1024, verbose=0)
    f = lambda x:np.round((x*100),4)
    Y_test = f(y_test)
    my_dict={
    
    'comment':comment,
    "toxic":Y_test[0][0],
    "severe_toxic":Y_test[0][1],
    "obscene":Y_test[0][2],
    "threat":Y_test[0][3],
    "insult":Y_test[0][4],
    "identity_hate":Y_test[0][5]
    }
    return my_dict

# Create your views here.
user_comments=[]
def index(request):
    commentform=CommentForm()
    user_comments.clear()
    if request.method == 'POST':
        commentform=CommentForm(request.POST)
        if commentform.is_valid():
            print ("valid")
            user_comments.append(commentform.cleaned_data['comment'])
            my_dict=predict(user_comments)
            return render(request,'home/result.html',context=my_dict) 
        else:
             print("error,form invalid")
    return render(request,'home/index.html',{'Commentform':commentform})



def result(request):
    return render(request,'home/result.html')