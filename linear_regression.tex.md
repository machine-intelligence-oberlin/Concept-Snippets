### Linear Regression
> Explanation and Multiple Codings of Linear Regression
---

__Explanation__ <br/>

\begin{equation}E\textsubscript{train}(\textit{h}(\textbf{x},\textbf{w})) &= \frac{1}{N}\\\sum_{i=0}^{d}(\textbf{w}^\textbf{T}\textbf{x}_n - y_n)^2\end{equation}

\begin{equation}E\textsubscript{train}(\textbf{w}) &= \frac{1}{N}\\\left\|(\textbf{X}\textbf{w} - \textbf{y})^2\right\|\end{equation}


\begin{equation}E\textsubscript{train}(\textbf{w}) &= \frac{1}{N}\\(\textbf{w}^\textbf{T}\textbf{X}^\textbf{T}\textbf{X}\textbf{w} - 2\textbf{w}^\textbf{T}\textbf{X}^\textbf{T}\textbf{y} + \textbf{y}^\textbf{T}\textbf{y} )^2\end{equation}


\begin{equation}\nabla E\textsubscript{train}(\textbf{w}) &= \frac{2}{N}\\(\textbf{X}^\textbf{T}\textbf{X}\textbf{w} - \textbf{X}^\textbf{T}\textbf{y}) &= 0\end{equation}


\begin{equation}\textbf{X}^\textbf{T}\textbf{X}\textbf{w} &= \textbf{X}^\textbf{T}\textbf{y}\end{equation}


\begin{equation}\textbf{w}\textsubscript{opt} &= (\textbf{X}^\textbf{T}\textbf{X}\textbf{w})^-1\textbf{X}^\textbf{T}\textbf{y}\end{equation}


