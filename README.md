########### how can i install and run django ########
1. Make sure Python is installed

Check:

python --version


or

python3 --version


If it shows a version (3.8+ is good), continue.

2. Create a virtual environment (recommended)

In your project folder:

Windows
python -m venv venv
venv\Scripts\activate

macOS / Linux
python3 -m venv venv
source venv/bin/activate


You’ll see (venv) in your terminal.

3. Install Django
pip install django


Check:

django-admin --version

4. Create a Django project
django-admin startproject myproject
cd myproject


Folder now looks like:

myproject/
  manage.py
  myproject/
    settings.py
    urls.py

5. Run the server
python manage.py runserver


or on macOS/Linux:

python3 manage.py runserver


Open in browser:

http://127.0.0.1:8000/


You should see the Django welcome page.

6. Create your first app (optional)
python manage.py startapp myapp


Then add "myapp" to INSTALLED_APPS in settings.py.
############### End ###############