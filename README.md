

## fee calculator


How to calculate the fee correctly from ICON.


```bash
$ ./fee_calculator.py {ICX_MOUNT}
```


```bash

$ ./fee_calculator.py 100
 - ICX: 100.000000000000000000 / wei: 0x56bc75e2d63100000 (100000000000000000000)
 - estimate_step : 0x186a0 (100000)
 - step_price : 0x2e90edd00 (12500000000)
----------------------------------------------------------------------------------------------------
fee = 0x470de4df82000(1250000000000000) = 0x186a0 (estimate_step) * 0x2e90edd00 (step_price)

$ ./fee_calculator.py 10000
  - ICX: 1000.000000000000000000 / wei: 0x3635c9adc5dea00000 (1000000000000000000000)
  - estimate_step : 0x186a0 (100000)
  - step_price : 0x2e90edd00 (12500000000)
 ----------------------------------------------------------------------------------------------------
 fee = 0x470de4df82000(1250000000000000) = 0x186a0 (estimate_step) * 0x2e90edd00 (step_price)

```

