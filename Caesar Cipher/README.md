
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

|lat/long|0|1|2|3|4|5|6|7|8|9|
|-|-|-|-|-|-|-|-|-|-|-|
|0|*35.01455380292978, -106.68627789365152*|~~35.12566491303089, -106.68627789365152~~|
|1|~~35.01455380292978, -106.79738890476263~~|~~35.12566491303089, -106.79738890476263~~|
|2|~~35.01455380292978, -106.80849901587374~~|~~35.12566491303089, -106.80849901587374~~|
|3|~~35.01455380292978, -106.91950012698485~~|~~35.12566491303089, -106.91950012698485~~|
|4|~~35.01455380292978, -106.02061123709596~~|~~35.12566491303089, -106.02061123709596~~|
|5|~~35.01455380292978, -106.13172234810607~~|~~35.12566491303089, -106.13172234810607~~|
|6|~~35.01455380292978, -106.24283345921718~~|~~35.12566491303089, -106.24283345921718~~|
|7|~~35.01455380292978, -106.35394456032829~~|~~35.12566491303089, -106.35394456032829~~|
|8|~~35.01455380292978, -106.46405567143930~~|**35.12566491303089, -106.46405567143930**|
|9|~~35.01455380292978, -106.57516678254041~~|**35.12566491303089, -106.57516678254041**|



| s_lat \ s_long | 0                              | 1                              | 2                              | 3                              | 4                              | 5                              | 6                              | 7                              | 8                              | 9                              |
|----------------|--------------------------------|--------------------------------|--------------------------------|--------------------------------|--------------------------------|--------------------------------|--------------------------------|--------------------------------|--------------------------------|--------------------------------|
| **0**          | 35.01455380292978, -106.68627789365152 | 35.12566491303089, -106.68627789365152 | 35.23677502414190, -106.68627789365152 | 35.34788613525201, -106.68627789365152 | 35.45899724636312, -106.68627789365152 | 35.56900835747423, -106.68627789365152 | 35.67011946858534, -106.68627789365152 | 35.78122057969645, -106.68627789365152 | 35.89233168070756, -106.68627789365152 | 35.90344279181867, -106.68627789365152 |
| **1**          | 35.01455380292978, -106.79738890476263 | 35.12566491303089, -106.79738890476263 | 35.23677502414190, -106.79738890476263 | 35.34788613525201, -106.79738890476263 | 35.45899724636312, -106.79738890476263 | 35.56900835747423, -106.79738890476263 | 35.67011946858534, -106.79738890476263 | 35.78122057969645, -106.79738890476263 | 35.89233168070756, -106.79738890476263 | 35.90344279181867, -106.79738890476263 |
| **2**          | 35.01455380292978, -106.80849901587374 | 35.12566491303089, -106.80849901587374 | 35.23677502414190, -106.80849901587374 | 35.34788613525201, -106.80849901587374 | 35.45899724636312, -106.80849901587374 | 35.56900835747423, -106.80849901587374 | 35.67011946858534, -106.80849901587374 | 35.78122057969645, -106.80849901587374 | 35.89233168070756, -106.80849901587374 | 35.90344279181867, -106.80849901587374 |
| **3**          | 35.01455380292978, -106.91950012698485 | 35.12566491303089, -106.91950012698485 | 35.23677502414190, -106.91950012698485 | 35.34788613525201, -106.91950012698485 | 35.45899724636312, -106.91950012698485 | 35.56900835747423, -106.91950012698485 | 35.67011946858534, -106.91950012698485 | 35.78122057969645, -106.91950012698485 | 35.89233168070756, -106.91950012698485 | 35.90344279181867, -106.91950012698485 |
| **4**          | 35.01455380292978, -106.02061123709596 | 35.12566491303089, -106.02061123709596 | 35.23677502414190, -106.02061123709596 | 35.34788613525201, -106.02061123709596 | 35.45899724636312, -106.02061123709596 | 35.56900835747423, -106.02061123709596 | 35.67011946858534, -106.02061123709596 | 35.78122057969645, -106.02061123709596 | 35.89233168070756, -106.02061123709596 | 35.90344279181867, -106.02061123709596 |
| **5**          | 35.01455380292978, -106.13172234810607 | 35.12566491303089, -106.13172234810607 | 35.23677502414190, -106.13172234810607 | 35.34788613525201, -106.13172234810607 | 35.45899724636312, -106.13172234810607 | 35.56900835747423, -106.13172234810607 | 35.67011946858534, -106.13172234810607 | 35.78122057969645, -106.13172234810607 | 35.89233168070756, -106.13172234810607 | 35.90344279181867, -106.13172234810607 |
| **6**          | 35.01455380292978, -106.24283345921718 | 35.12566491303089, -106.24283345921718 | 35.23677502414190, -106.24283345921718 | 35.34788613525201, -106.24283345921718 | 35.45899724636312, -106.24283345921718 | 35.56900835747423, -106.24283345921718 | 35.67011946858534, -106.24283345921718 | 35.78122057969645, -106.24283345921718 | 35.89233168070756, -106.24283345921718 | 35.90344279181867, -106.24283345921718 |
| **7**          | 35.01455380292978, -106.35394456032829 | 35.12566491303089, -106.35394456032829 | 35.23677502414190, -106.35394456032829 | 35.34788613525201, -106.35394456032829 | 35.45899724636312, -106.35394456032829 | 35.56900835747423, -106.35394456032829 | 35.67011946858534, -106.35394456032829 | 35.78122057969645, -106.35394456032829 | 35.89233168070756, -106.35394456032829 | 35.90344279181867, -106.35394456032829 |
| **8**          | 35.01455380292978, -106.46405567143930 | 35.12566491303089, -106.46405567143930 | 35.23677502414190, -106.46405567143930 | 35.34788613525201, -106.46405567143930 | 35.45899724636312, -106.46405567143930 | 35.56900835747423, -106.46405567143930 | 35.67011946858534, -106.46405567143930 | 35.78122057969645, -106.46405567143930 | 35.89233168070756, -106.46405567143930 | 35.90344279181867, -106.46405567143930 |
| **9**          | 35.01455380292978, -106.57516678254041 | 35.12566491303089, -106.57516678254041 | 35.23677502414190, -106.57516678254041 | 35.34788613525201, -106.57516678254041 | 35.45899724636312, -106.57516678254041 | 35.56900835747423, -106.57516678254041 | 35.67011946858534, -106.57516678254041 | 35.78122057969645, -106.57516678254041 | 35.89233168070756, -106.57516678254041 | 35.90344279181867, -106.57516678254041 |