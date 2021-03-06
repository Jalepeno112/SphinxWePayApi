WePay Sphinx Directive
========================
This is a plugin for `Sphinx <http://www.sphinx-doc.org/en/stable/>`_ documentation that allows you to create a link to the WePay API documentation without needing to write out the URL each time.

All you need is the base endpoint (i.e. /account, /user, /account/kyc) and then the action (i.e. find, create, etc.).  This extension will take that info and then build out the rest of the URL.  This also means that your documentation is safe if WePay changes their URL.  You just have to update one variable in the extension (which contains the base of the documentation URL) instead of combing through pages and pages of documentation looking for every place that you reference the WePay docs.

How to Use
-------------
Using the extension is very simple:
    >>> When creating accounts, we use :wepay:`account create`.

This would render into:
    When creating accounts, we use `/account/create <https://developer.wepay.com/api-calls/account#create>`_

This also works with endpoints like the */account/kyc* endpoint:
    >>> When using the KYC APi, we use :wepay:`account/kyc create`

If you want to document one of the lookup endpoints (i.e. */account*, */user*, */account/kyc*) you don't have to include the second argument:
    >>> When looking up an account, we use :wepay:`account`

Installation
-------------
There are two ways to install the extension.  One way is to use pip to install from the GitHub repo (recommended) and the other is to clone the repository and add to a `sphinxext` folder in your documentation.

Using pip
~~~~~~~~~~~~
To install the documentation using pip:
    >>> pip install git+https://github.com/Jalepeno112/SphinxWePayApi.git#egg=sphinxwepayapi

This will install the package. 

After this, you need to add it to your Sphinx extension list.

Open your ``conf.py`` page and modify the ``extensions`` variable so it looks like:
    >>> extensions = [..., "sphinxwepayapi.wepay_docs"]

Where the "..." is the list of all other extensions you have.

pip freeze Behavior
^^^^^^^^^^^^^^^^^^^^
Running ``pip freeze`` will incorrectly document that the package was installed from PyPi instead of GitHub.  
You can use the ``-e`` flag to install the package in editable mode, which will cause ``pip freeze`` to show that the package was downloaded from GitHub.  
However, this will create a ``src`` directory to store the downloaded package (you can use ``--src`` followed by a different directory name to change the location).

You should use the ``-e`` option if you feel it is important to remember that this package came from a GitHub repo instead of PyPi.

For Source Using `sphinxext`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1) Create a directory in the same directory where your ``conf.py`` file lives to hold the extension (most tutorials say to call it *sphinxext*)
2) Create a *__init__.py* file so that the modules can be imported from the directory 
   >>> touch __init__.py
3) Download the repository and place the folder into the directory you created in step 1
4) Open your ``conf.py`` file and:
   
   a) add the following line in order to add the directory to your path
       >>> sys.path.insert(0,os.path.abspath('sphinxext'))
   
   b) add this extension into the list of existing extensions
        >>> extensions  = ["SphinxWePayApi.wepay_docs"]

You can also copy the *wepay_docs* file out of the cloned directory and place it directly in your *sphinxext* directory

License
-----------
Copyright 2016 Giovanni Briggs

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
