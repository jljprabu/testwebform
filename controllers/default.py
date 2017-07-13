# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------

def index():
    import ipaddress
    #id = request.args(0,cast=int)
#    output = list(ipaddress.ip_network('172.16.0.2/16', strict=False).hosts())
#    ip_lst = []
#    for i in output:
#        ip_lst.append(str(i))
    form = FORM(DIV('VM Name: ', INPUT(_name='name', requires=IS_NOT_EMPTY())),
                DIV('IP Address: ', INPUT(_name='ipadd', requires=IS_NOT_EMPTY())),
                DIV('Business Type: ', SELECT(OPTION('Investments', _value='inv'), OPTION('Member Services', _value='ms'),value=2)),
                DIV('Environment Type: ', SELECT(OPTION('PROD', _value='prod'), OPTION('DEV', _value='dev'), OPTION('DMZ', _value='dmz'))),
                DIV(INPUT(_type='submit'), _action=URL('page_two')))
    form.add_button("Cancel",URL(r=request,f='index'))
    return locals()


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
