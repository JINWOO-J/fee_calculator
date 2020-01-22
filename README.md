

## fee calculator


How to calculate the fee correctly from ICON.


```bash
$ ./fee_calculator.py {ICX_MOUNT}
```


```bash

$ ./fee_calculator.py 100
 - ICX: 100.000000000000000000 / wei: 0x56bc75e2d63100000 (100000000000000000000)
 - estimate_step : 0x186a0 (100000)
 - step_price : 0x2540be400 (10000000000)
----------------------------------------------------------------------------------------------------
fee = 0x38d7ea4c68000 = 0x186a0 (estimate_step) * 0x2540be400 (step_price)


$ ./fee_calculator.py 10000
 - ICX: 10000.000000000000000000 / wei: 0x21e19e0c9bab2400000 (10000000000000000000000)
 - estimate_step : 0x186a0 (100000)
 - step_price : 0x2540be400 (10000000000)
----------------------------------------------------------------------------------------------------
fee = 0x38d7ea4c68000 = 0x186a0 (estimate_step) * 0x2540be400 (step_price)


```

