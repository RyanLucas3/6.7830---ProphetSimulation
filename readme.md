This repo is a flexible simulation of the Prophet process; that is, a time series following exactly the properties of a correctly specified [Facebook Prophet model](https://facebook.github.io/prophet/). In short, a Prophet process of length $T$ can be expressed as follows:

$$y(t) = g(t) + s(t) + h(t) + \epsilon_t, \quad t \in [T]$$

where $y(t)$ is the observed value at time $t$ deriving from several additive components: $g(t)$ represents the trend or growth component of the process, $s(t)$ represents the seasonal component, $h(t)$ represents the effect of holidays, and $\epsilon_t$ is a noise term. 

<div style="text-align:center;">
  <img src="https://user-images.githubusercontent.com/55145311/232958164-64ff849f-6480-4420-a749-47ddafceac61.png" alt="Predictions" width="500"/> 
</div> 

We make it easy to modify the parameters of the simulation, and to observe the effect on the time series generated and forecasts produced by Prophet. We briefly describe these parameters here, which fall into four main categories:


Growth parameters controlling $g(t)$:
- $C(t)$: the asssumed "carrying capacity"; effectively the assumed maximum $g(t)$ that the simulation can reach, as is often assumed in a logistic growth model.
- $k$: the trend of the underlying growth rate. Higher $k$ means the series will trend upwards more and be less affected by change-points.
- $\tau$: scale of the Laplace prior on the change-points $\delta_j \sim \text{Laplace}(0, \tau)$. Higher $\tau$ means the change-points will on average have a larger magnitude.
- $m$: the offset parameter determining where the mid-point in the growth curve should occur. A very large $m > T$ will mean the simulation never reaches its carrying capacity.
- $\bar{S}$: the change-point frequency. Can alternatively be calculated from the number of changepoints (referred to as $S$ in the Prophet paper).

Seasonality parameters controlling $s(t)$:
- $P^Y$: The yearly period of the seasonality component in the model, which is set to 365 days.
- $P^W$: The weekly period of the seasonality component in the model, which is set to 7 days.
- $\sigma^Y$: The standard deviation of the normal distribution for the yearly seasonality component. 
- $\sigma^W$: The standard deviation of the normal distribution for the weekly seasonality component.

Holiday parameters controlling $h(t)$
- $Z(t)$: the days of holidays. In our simulation, holidays occur on New Years, The Fourth of July, Haloween and Christmas, hence $Z(t) =  \langle\mathbb{1}[t = \mathbb{1}], \mathbb{1}[t = 185], \mathbb{1}[t = 304], \mathbb{1}[t \in (356, ..., 363)]\rangle.$
- $\nu$: controls the variance of the holiday effect. The final holiday component is given as $h(t) = Z(t)\boldsymbol{\kappa}$, where as with the paper we simulate $\kappa_i \sim \mathcal{N}(0, \nu^2)$
