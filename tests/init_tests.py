from flask import request
import json


def hello():
    return 'Hello, World!'


def check_params():
    print('--- /check_params called ---')
    print('Method:', request.method)
    try:
        data_json = request.get_json(silent=True)
    except Exception:
        data_json = None
    print('json:', data_json)
    print('args:', request.args)
    print('form:', request.form)
    print('data:', request.data)

    params = {}
    # GET params
    params.update(request.args.to_dict(flat=True))
    # form data (POST with form-encoded)
    params.update(request.form.to_dict(flat=True))
    # JSON body (POST with application/json)
    if isinstance(data_json, dict):
        params.update(data_json)

    resp_str = json.dumps(params, ensure_ascii=False)
    return resp_str, 200, {'Content-Type': 'application/json'}
