from docutils import nodes, utils
from docutils.parsers.rst.roles import set_classes


# https://bitbucket.org/dhellmann/sphinxcontrib-bitbucket/src/36be4abe62e594ad7d6673d62983c23c541d401d/sphinxcontrib/bitbucket.py?at=default&fileviewer=file-view-default


def setup(app):
    """
    Setup the directive.  It tells the directive what to use as the base URL for WePay documentation, and what the name of the directive is.
    """
    app.add_config_value("wepay_docs_home", "https://developer.wepay.com/api-calls/", 'html')

    app.add_role("wepay", wepay_docs_role)

    return {'version': '0.1'}   # identifies the version of our extension

def make_wepay_link(app, rawtext, endpoint, function, name_override, options):
    """
    Create link to WePay docs

    :param app:             the Sphinx application instance that is currently running
    :param endpoint:        name of the endpoint you want to point to (i.e. user, account, account/membership, etc.)
    :param function:        the function within that endpoint that we want to point to (ex: if endpoint is user, the function could be register)
    :param name_override:   URL to use to override the link.  Not all documentation follows the exact same pattern.  For example, /account/kyc is documented under the /kyc URL in the docs.  So we can pass -/account/kyc in the directive to override the name of the link

    """
    try:
        # get the documentation URL
        base = app.config.wepay_docs_home
        if not base:
            raise AttributeError
    except AttributeError, err:
        raise ValueError('wepay_docs_home configuration value is not set (%s)' % str(err))

    # if the URL doesn't include a trailing slash, add one
    slash = '/' if base[-1] != '/' else ''

    # build external url
    # if no function is given, then it is the main endpoint, which is accessed by #lookup on the page
    ref = "{0}{1}#{2}"

    ref = ref.format(base,endpoint,function) if function else ref.format(base,endpoint,"lookup")

    # build the text that we will display instead of :wepay:`endpoint function`
    insert_text = "/" + endpoint + "/" + function if function else "/" + endpoint
    if name_override:
        insert_text = name_override
    set_classes(options)

    # make the node
    node = nodes.reference(rawtext, insert_text, refuri=ref,
                           **options)
    return node

def wepay_docs_role(name, rawtext, text, lineno, inliner,
            options={}, content=[]):
    """
    Process the WePay docs role.
    """

    # get the application
    app = inliner.document.settings.env.app

    # parse the text entered in the role.
    # here, we simply split on space to define the two parts of our url
    # if a function parameter is not given, then we don't use one
    # example: /account is the account lookup call but it doesn't have a function attached.
    # We can also use _-/some/string to override the name of the link because not all of the documentation follows this pattern
    endpoint, name_override = text.split(" -") if ' -' in text else (text, None)
    endpoint, function = endpoint.split(" ") if ' ' in endpoint else (endpoint, None)

    # make the node
    node = make_wepay_link(app, rawtext, endpoint, function, name_override, options)
    return ([node], [])

    
