#__init__.py file so that this directory can be imported
try:
    import wepay_docs
except SystemError:
    from . import wepay_docs
