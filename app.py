import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

# Function to summarize the text
def summarize():

    # Summarization and sentimental analysis
    url = utext.get('1.0', 'end').strip()

    article = Article(url) # Creating an article object

    article.download() # Download data
    article.parse() # Parse data

    article.nlp()

    # Passing the data to the boxes
    # Setting the state of all boxes to normal
    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    title.delete('1.0', 'end') # Deleting anything that is already inside it
    title.insert('1.0', article.title) # Inserting data into it

    author.delete('1.0', 'end')
    author.insert('1.0', article.authors)

    publication.delete('1.0', 'end')
    publication.insert('1.0', article.publish_date)

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    # Turn the article into textblob version, to get the polarity
    analysis = TextBlob(article.text)
    sentiment.delete('1.0', 'end')
    sentiment.insert('1.0', f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

    # Changing the state to disabled, so the user can't mess with it
    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')


# Creating the user interface with tkinter
root = tk.Tk()
root.title("News Summarizer")
root.geometry('1200x600')

# Creating indivudial buttons and text boxes
# Title
tlabel = tk.Label(root, text='Title')
tlabel.pack()
title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg='#dddddd') # User won't be able to put things on the boxes
title.pack()

# Author
alabel = tk.Label(root, text='Author')
alabel.pack()
author = tk.Text(root, height=1, width=140)
author.config(state='disabled', bg='#dddddd') 
author.pack()

# Publication Date
plabel = tk.Label(root, text='Publishing Date')
plabel.pack()
publication = tk.Text(root, height=1, width=140)
publication.config(state='disabled', bg='#dddddd')
publication.pack()

# Summary
slabel = tk.Label(root, text='Summary')
slabel.pack()
summary = tk.Text(root, height=20, width=140)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

# Sentiment analysis
selabel = tk.Label(root, text='Publishing Date')
selabel.pack()
sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state='disabled', bg='#dddddd')
sentiment.pack()

# URL
ulabel = tk.Label(root, text='URL')
ulabel.pack()
utext = tk.Text(root, height=1, width=140)
utext.pack()

# Button
btn = tk.Button(root, text='Summarize', command=summarize)
btn.pack()

root.mainloop()


