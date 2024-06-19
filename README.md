# aqgc

UFO model implementation of the dimension-eight electroweak SMEFT operators generating anomalous quartic gauge couplings

The model itself is in `aqgc_ufo` ([zip](https://download-directory.github.io/?url=https%3A%2F%2Fgithub.com%2Fgdurieux%2Faqgc%2Ftree%2Fmain%2Faqgc_ufo)). The other files can be used to generate it with `FeynRules`.

A simple test run of triple boson production
```
import model aqgc_ufo-FS0
generate u u~ > w+ w- z NP=1
output
launch
```
with the `FS0` parameter set to `1e-9` should give a cross section of the order of `0.02623 +- 6.09e-05 pb` while `FS0` set to `0` should give about `0.02058 +- 7.657e-05 pb`.
