# NLP-SQL
Natural language query system

Quick Setups

1. Create and activate virtual Environment :
   $ pip install virtualenv

   $ virtualenv nlps
   
   $ source /bin/activate
 
2. Download required packages in virtual Environment :
   $ pip install -r requirements.txt 
  
3. Download NLTK packages : 
   $ python 
   >>> import nltk
   
   >>> nltk.download()

4. Create MySql DB Server :
   name DB: nlpproj
   password: root

   $ python CreateTab.py

   $ python connection.py
  
5. Run Server :
   $ python nlp-sql.py


