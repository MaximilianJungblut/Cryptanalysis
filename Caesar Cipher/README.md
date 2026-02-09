
![Project Cover](assets/cover.gif)
# History
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
### Formula

To encrypt a plaintext letter to a ciphertext letter, we use the rule

```math
\begin{alignedat}{1}
c \equiv p + k \pmod{b}
\end{alignedat}
```

or equivalently

```math
\begin{alignedat}{1}
c = (p + k) \bmod b
\end{alignedat}
```

where

- $$p$$ is the **plaintext letter index** (i.e. $$\varphi(\text{plaintext letter})$$),
- $$k$$ is the **secret shift** (an integer, required to be $$0 < k \ne b$$),
- $$c$$ is the **ciphertext letter index** (the result after encryption).

> [!IMPORTANT]
> Including $0$ in the range of $\varphi$ avoids unnecessary conditional logic in the modular arithmetic. If we had instead defined $\varphi(\mathrm{A}) = 1$ and $\varphi(\mathrm{Z}) = 26$, the computation $c = p + k \bmod b$ would produce $c = 0$ when $p + k = b$. $0$ **doesn't** correspond to any letter (since letters start at 1), requiring extra logic.

### Algorithmic Implementation
#### Mathematical

Let the plaintext be a string of uppercase English letters (possibly with spaces or punctuation, which are left unchanged):

```math
\begin{alignedat}{1}
x = x_1 x_2 \dots x_n \in A^* \quad \text{(or extended alphabet with unchanged symbols)}
\end{alignedat}
```


## Decryption
### Formula

...

### Algorithmic Implementation
#### Mathematical

...


# P Sovling Algorithm

## Algorithmic Implementation
#### Mathematical

...

#### Psydocode

...

#### Pratical (using rust)

```rust
static ALPHABETICAL_NUMERICAL_BIJECION: LazyLock<HashMap<char, usize>> = LazyLock::new(|| {
    HashMap::from([
        ('A', 0),
        ('B', 1),
        ('C', 2),
        ('D', 3),
        ('E', 4),
        ('F', 5),
        ('G', 6),
        ('H', 7),
        ('I', 8),
        ('J', 9),
        ('K', 10),
        ('L', 11),
        ('M', 12),
        ('N', 13),
        ('O', 14),
        ('P', 15),
        ('Q', 16),
        ('R', 17),
        ('S', 18),
        ('T', 19),
        ('U', 20),
        ('V', 21),
        ('W', 22),
        ('X', 23),
        ('Y', 24),
        ('Z', 25),
    ])
});

fn get_alphabetical_numerical_bijection(alphabetical_series: &str) -> Vec<usize> {
    let numerical_series: Vec<usize> = alphabetical_series
        .chars()
        .filter_map(|c| ALPHABETICAL_NUMERICAL_BIJECION.get(&c).copied())
        .collect();
    return numerical_series;
}
```

```rust
fn check_plaintext_fragment_requirements(k: &[usize]) {
    if k.len() < 2 {
        panic!(
            "Assumed plaintext fragment too short - every possible shift would match.\n\
            The length of the fragment needs to be greater than one.",
        );
    }

    let min_val = *k.iter().min().unwrap();
    let max_val = *k.iter().max().unwrap();

    if min_val == max_val {
        panic!(
            "Assumed plaintext fragment is constant (all letters identical).\n\
             This causes false positives if ciphertext includes also constants.\n\
             Use a fragment with at least two different letters.",
        );
    }
}
```


```rust
fn p_solving(assumed_plaintext_fragment: &str, ciphertext: &str) {

    let k: Vec<usize> = get_alphabetical_numerical_bijection(assumed_plaintext_fragment);
    check_plaintext_fragment_requirements(&k);
    let c: Vec<usize> = get_alphabetical_numerical_bijection(ciphertext);

    let b: isize = ALPHABETICAL_NUMERICAL_BIJECION.len() as isize;
    let w: usize = k.len();

    for i in 0..=c.len().saturating_sub(w) {

        let c_i_to_i_plus_w: &[usize] = &c[i..i + w];

        let p_series: Vec<isize> = calculate_p_series(c_i_to_i_plus_w, &k, b);

        let (p_series_variance, p) = calculate_p_series_variance(p_series);

        if p_series_variance == 0 {
            println!("pos {:3} | shift {:2} | window {:?}", i, p, c_i_to_i_plus_w);
        }
    }
}
```

```rust
fn calculate_p_series(c: &[usize], k: &[usize], b: isize) -> Vec<isize> {
    let p_series: Vec<isize> = c
        .iter()
        .zip(k)
        .map(|(&c_i, &k_i)| {

            let a: isize = c_i as isize - k_i as isize;

            let q: isize = if a >= 0 {

                a / b

            } else {

                a / b - 1

            };

            a - b * q

        })
        .collect();
    return p_series;
}
```

```rust
fn calculate_p_series_variance(p_series: Vec<isize>) -> (isize, isize) {
    let p_0: isize = p_series[0];
    let p_series_variance: isize = p_series
        .iter()
        .map(|&p_i| {

            let delta = p_i - p_0;

            delta * delta

        })
        .sum();
    return (p_series_variance, p_0);
}
```



# Obfuscation Matrix
![Obfuscated Locations](assets/locations.png)