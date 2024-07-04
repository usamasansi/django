Error:
E:\Learning\python\my_tennis_club>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

Exception in thread django-main-thread:
Traceback (most recent call last):
  File "C:\Users\DELL\AppData\Local\Programs\Python\Python312\Lib\threading.py", line 1073, in _bootstrap_inner
    self.run()
  File "C:\Users\DELL\AppData\Local\Programs\Python\Python312\Lib\threading.py", line 1010, in run
    self._target(*self._args, **self._kwargs)
  File "C:\Users\DELL\AppData\Local\Programs\Python\Python312\Lib\site-packages\django\utils\autoreload.py", line 64, in wrapper
    fn(*args, **kwargs)
  File "C:\Users\DELL\AppData\Local\Programs\Python\Python312\Lib\site-packages\django\core\management\commands\runserver.py", line 133, in inner_run
    self.check(display_num_errors=True)
  File "C:\Users\DELL\AppData\Local\Programs\Python\Python312\Lib\site-packages\django\core\management\base.py", line 486, in check
    all_issues = checks.run_checks(
                 ^^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\AppData\Local\Programs\Python\Python312\Lib\site-packages\django\core\checks\registry.py", line 88, in run_checks
    new_errors = check(app_configs=app_configs, databases=databases)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\AppData\Local\Programs\Python\Python312\Lib\site-packages\django\core\checks\urls.py", line 14, in check_url_config
    return check_resolver(resolver)
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\AppData\Local\Programs\Python\Python312\Lib\site-packages\django\core\checks\urls.py", line 24, in check_resolver
    return check_method()
           ^^^^^^^^^^^^^^
  File "C:\Users\DELL\AppData\Local\Programs\Python\Python312\Lib\site-packages\django\urls\resolvers.py", line 520, in check
    messages.extend(check_resolver(pattern

    
Solution of error:
**you just need to check your directory**

    urls.py
same name files in your both main directories of your project so check your project directory and created app directory.

 

    from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('members.urls')),
    path('admin/', admin.site.urls),
]

Put this code in the **urls.py** file located in the settings.py,urls.py directory. 

and add this code:

    from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
]

in the **urls.py** file located in the settings.py,urls.py directory.
