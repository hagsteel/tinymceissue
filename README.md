tinymceissue
============

Demonstrate issue with tinymce

# Installation
1.  git clone git@github.com:jonashagstedt/tinymceissue.git
2.  mkvirtualenv tinyissue
3.  pip install -r requirements.txt
4.  ./manage.py syncdb
5.  ./manage.py runserver

# Seeing the issue
1.  Browse to http://localhost:8000/admin
2.  Login
3.  Browse to http://localhost:8000/admin/app/foo/add/
4.  Click on "Add another Bar" at the bottom

A plain text area is displayed
