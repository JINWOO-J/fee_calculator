#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests, sys


def icx_to_wei(icx):
    return int(icx * 10 ** 18)


def hex_to_int(value):
    return int(value, 16)


def create_jsonrpc_request_content(_id, method, params=None):
    content = {
        'jsonrpc': '2.0',
        'method': method,
        'id': _id
    }
    if params is not None:
        content['params'] = params
    return content


def get_string_decimal(value, place):
    strValue = str(value)
    if value >= 10 ** place:
        strInt = strValue[:len(strValue) - place]
        strDecimal = strValue[len(strValue) - place:]
        result = f'{strInt}.{strDecimal}'
        return result
    else:
        zero = "0."
        valPoint = len(strValue)  # valPoint : 몇자릿수인지 계산
        pointDifference = place - valPoint
        strZero = "0" * pointDifference
        result = f'{zero}{strZero}{value}'
        return result


def print_amount(amount):
    """
    Args:
        amount(str): hexa string starting with '0x'
    """
    wei = int(amount, 16)
    icx = get_string_decimal(wei, 18)
    print(f' - ICX: {icx} / ' + f'wei: {amount} ({wei})')
    return icx


endpoint = "https://ctz.solidwallet.io"

icx_mount = float(sys.argv[1:][0])
icx_mount_hex = hex(icx_to_wei(icx_mount))
print_amount(icx_mount_hex)

step_payload = create_jsonrpc_request_content(
    _id=1234,
    method="icx_call",
    params={
        "to": "cx0000000000000000000000000000000000000001",
        "dataType": "call",
        "data": {
            "method": "getStepPrice",
            "params": {}
        }
    }
)

step_price_res = requests.post(f"{endpoint}/api/v3", json=step_payload)
step_price = step_price_res.json()['result']

estimate_payload = create_jsonrpc_request_content(
    _id=1234,
    method="debug_estimateStep",
    params={
        "version": "0x3",
        "from": "hxbe258ceb872e08851f1f59694dac2558708ece11",  # from address
        "to": "hx5bfdb090f43a808005ffc27c25b213145e80b7cd",  # to address
        "value": icx_mount_hex,  # icx amount
        "timestamp": "0x563a6cf330136",
        "nid": "0x1",
        "nonce": "0x1"
    }
)
estimate_step_res = requests.post(f"{endpoint}/api/debug/v3", json=estimate_payload)
estimate_step = estimate_step_res.json()['result']


print(f" - estimate_step : {estimate_step} ({hex_to_int(estimate_step)})")
print(f" - step_price : {step_price} ({hex_to_int(step_price)})")

print("-"*100)

fee = hex_to_int(estimate_step) * hex_to_int(step_price)
print(f"fee = {hex(fee)} = {estimate_step} (estimate_step) * {step_price} (step_price) ")

