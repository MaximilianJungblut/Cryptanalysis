
![Project Cover](assets/cover.gif)
# History
The **Caesar cipher** is one of the most primitive cryptographic algorithms.
It is essentially a **monoalphabetic substitution** that applies a fixed shift (rotation) to every letter in the alphabet.

Its earliest known use dates back to around **50 BC** by **Julius Caesar**, who reportedly used a shift of 3 to protect military messages.

Because it is a simple cyclic shift with only 26 possible keys (in the English alphabet), it can be broken very easily using:
- **brute force** (trying all 26 shifts),  
- **frequency analysis** (comparing letter frequencies in the ciphertext to those of natural language),  
- or a **known-plaintext attack** (if even a small fragment of the plaintext is known or can be assumed to appear in the message, the shift $k$ can be solved directly from the equation $c \equiv p + k \pmod{26}$).

For practical encryption and decryption by hand, people often use a **tabula recta** (a table with the plaintext alphabet in the top row and the shifted ciphertext alphabet below it, repeated for each possible shift).

## Example ($k = 23$)

Plain|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
Cipher|X|Y|Z|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|

FOOD TRUCK $=>$ CLLA QORZH \
CLLA QORZH $=>$ FOOD TRUCK


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


# Solving

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



# Obfuscational Usage

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
