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
