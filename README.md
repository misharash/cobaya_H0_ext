# cobaya_H0_ext
Some extensions and examples of H0 likelihoods for [Cobaya sampler](https://github.com/CobayaSampler/cobaya).

## Python package contents (classes)
* _H0_nonsymmetric - simple generalization of Cobaya's gaussian likelihood for the latest `H0` measurements, allowing for different plus and minus errorbars. (This naturally means that the likelihood is not quite gaussian, but the actual form is rarely specified, so this is a workaround for such situation.)
* MCP - result of [Megamaser Cosmology Project](https://arxiv.org/abs/2001.09213) (MCP).
* H0LiCOW - result of [H0LiCOW](https://arxiv.org/abs/1907.04869), uses the nonsymmetric H0 class.

## External contents
* test.yaml - example config to run Cobaya with all the likelihoods (`cobaya-run test.yaml` in this directory) to make sure they work. The measurements are independent, so this combination can be used in production runs.