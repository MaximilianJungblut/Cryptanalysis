
![Project Cover](assets/cover.gif)
# Definition
sfsdfsdfsdfsd


# Calculation
## Constants

Let

```math
\begin{alignedat}{1}
A = \{ \mathrm{A}, \mathrm{B}, \dots, \mathrm{Z} \}
\end{alignedat}
```

be the alphabet,

```math
\varphi \colon A \xrightarrow{\sim} \mathbb{N}/25\mathbb{N},\\
\begin{alignedat}{2}
&\varphi(\mathrm{A}) &&= 0, \\
&\varphi(\mathrm{B}) &&= 1, \\
& &&\vdots \\
&\varphi(\mathrm{Z}) &&= 25.
\end{alignedat}
```

be the bijection and

```math
\begin{alignedat}{1}
b = |\varphi(A)|
\end{alignedat}
```

be the cardinality of the bijection $$\varphi$$.

## Encryption
### General

To encrypt a plaintext letter to a ciphertext letter, we use the rule

$$
c \equiv p + k \pmod{b}
$$

or equivalently

$$
c = (p + k) \bmod b
$$

where

- $p$ is the **plaintext letter index** (i.e. $$\varphi(\text{plaintext letter})$$),
- $k$ is the **secret shift** (an integer, required to be $$0 < k \ne b$$),
- $c$ is the **ciphertext letter index** (the result after encryption).

> [!IMPORTANT]  
> Including $0$ in the range of $\varphi$ avoids unnecessary conditional logic in the modular arithmetic. If we had instead defined $\varphi(\mathrm{A}) = 1$ and $\varphi(\mathrm{Z}) = 26$, the computation $c = p + k \bmod b$ could produce $c = 0$ when $p + k = b$. $0$ would **not** correspond to any letter (since letters start at 1), requiring extra logic.

### Theoretical Implementation

Let the plaintext be a string of uppercase English letters (possibly with spaces or punctuation, which are left unchanged):

$$
x = x_1 x_2 \dots x_n \in A^* \quad \text{(or extended alphabet with unchanged symbols)}
$$


The number $0$ is included in the bijetion $\varphi$ to prevent unessary computational logic like
$$if \varphi(Z) = 26 = k and p = 0, then (0+26) \mod 26 = 0 if 0, then 0 + 1 = 1$$






Its inverse satisfies $\varphi^{-1}(n) =$ the $(n+1)$-th letter of the alphabet (with A being the first).



**Encryption**\
dfgfdgfdgfdgfdgfd fdgfdgd
$$\left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)$$

**Decryption**\
dfgfdgfdgfdgfdgfd fdgfdgd
$$\left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)$$

**P Sovling**\
dfgfdgfdgfdgfdgfd fdgfdgd
$$\left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)$$

# P Sovling Algorithm

## Mathematical Procedure

## Psydocode

## Rust Implementation

# Obfuscation Matrix
![Obfuscated Locations](assets/locations.png)