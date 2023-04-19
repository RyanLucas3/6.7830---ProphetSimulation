We have started by creating a flexible simulation of the Prophet process; that is, a time series following exactly the properties of a correctly specified Prophet model. Here, we briefly describe our findings so far and provide a specification of the simulation. In short, a Prophet process of length $T$ can be expressed as follows:
\begin{align*}
y(t) &= g(t) + s(t) + h(t) + \epsilon_t, \quad t \in [T]
\end{align*}

\noindent where $y(t)$ is the observed value at time $t$ deriving from several additive components: $g(t)$ represents the trend or growth component of the process, $s(t)$ represents the seasonal component, $h(t)$ represents the effect of holidays, and $\epsilon_t$ is a noise term. Note that this term is referred to as an error term in \cite{taylor2018forecasting}, whereas we use $\epsilon_t$ to refer to the noise in the generated process. We assume for now that $\epsilon_t \sim \mathcal{N}(0, 0.001)$, indicating very small variance in the underlying noise process. This was done for an initial sanity-check of the simulation, but we plan to conduct a more thorough analysis of how the model performance in different signal-to-noise regimes. We now discuss each component and the effect of different parameter values.
