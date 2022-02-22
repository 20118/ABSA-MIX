import pandas as pd

def get_tuple_data(test_file):
    df=pd.read_csv(test_file)
    df=df.head(5)
    
    sent=[]; at=[]; lbl=[]
    for i in range(len(df)):
        aspect_terms=str(df['aspect_terms'].loc[i]).split("', '")
        aspect_terms_sentiment=str(df['at_polarity'].loc[i]).split(",")
        text=str(df['sentence'].loc[i]).lower()

        for t in range(len(aspect_terms)):
            if(aspect_terms[t]!=""):
                term=aspect_terms[t].lower().replace("['","")
                term= term.replace("']","").strip()
                if(term not in text):             
                    continue                
                term_senti=aspect_terms_sentiment[t].replace("[", "").replace("]","").lower().strip()
                term_senti=term_senti[1:-1]
             
                sent.append(text);at.append(term);lbl.append(term_senti)
   

    return sent,at,lbl

if __name__ == "__main__":
	labels2Idx = {'positive':0, 'negative':1, 'neutral':2, 'conflict':3}

	train_sentence, train_aspect, train_label=get_tuple_data("restaurant.csv")

	print(train_sentence[0])
	
