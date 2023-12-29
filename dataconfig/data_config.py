class global_var:
    ID = '0'
    Mode = '1'
    Url = '2'
    Run = '3'
    Method = '4'
    Header = '5'
    Depend_Case = '6'
    Depend_Data = '7'
    Depend_Field = '8'
    Request_Data = '9'
    Expect = '10'
    Result = '11'

def get_id():
    return global_var.ID

def get_mode():
    return global_var.Mode

def get_url():
    return global_var.Url

def get_is_run():
    return global_var.Run

def get_method():
    return global_var.Method

def get_is_header():
    return global_var.Header

def get_depend_case():
    return global_var.Depend_Case

def get_depend_data():
    return global_var.Depend_Data

def get_depend_field():
    return global_var.Depend_Field

def get_request_data():
    return global_var.Request_Data

def get_expect():
    return global_var.Expect

def get_result():
    return global_var.Result



