r"""
.. module:: _H0_nonsymmetric
:Synopsis: Generalized prototype class for local Hubble parameter measurements
:Author: Michael Rashkovetskyi
This is a simple generalization of Cobaya's gaussian likelihood for the latest
:math:`H_0` measurements, allowing for different plus and minus errorbars.
"""

from cobaya.likelihoods.base_classes import H0


class H0_nonsymmetric(H0):
    # additional variables from yaml
    H0_std_p: float
    H0_std_m: float

    def initialize(self):
        pass

    def logp(self, **params_values):
        H0_theory = self.provider.get_param("H0")
        H0_std = self.H0_std_m if H0_theory < self.H0_mean else self.H0_std_p
        return -((H0_theory - self.H0_mean)/H0_std)**2/2
