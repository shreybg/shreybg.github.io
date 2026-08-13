Title: A first post, with theorems
Date: 2026-08-12 09:00
Category: expository
Tags: analysis, worked examples
Author: Your Name
Slug: a-first-post

Inline math works the way you'd expect: the map $f(x) = x^2 - \varepsilon$
has a fixed point whenever $\varepsilon$ is small. Note that $a_{i,j}$ and
$x_1 \cdot x_2$ survive Markdown intact, which is the whole reason for
using arithmatex rather than raw KaTeX delimiters.

Displayed equations use double dollars:

$$\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s} = \prod_{p} \left(1 - p^{-s}\right)^{-1}.$$

## Boxed environments

This is the piece that needs custom CSS on WordPress.com and is free here:

<div class="theorem" markdown="1">
**Theorem 1 (Euclid)** There are infinitely many primes.
</div>

<div class="proof" markdown="1">
Suppose $p_1, \dots, p_n$ were all of them. Then $N = p_1 \cdots p_n + 1$ is
divisible by no $p_i$, yet has some prime factor.
</div>

The available classes are `theorem`, `lemma`, `proposition`, `corollary`,
`definition`, `conjecture`, `remark`, `example`, `exercise`, and `proof`.

<div class="remark" markdown="1">
**Remark.** The `markdown="1"` attribute is what lets Markdown syntax work
*inside* the `div`. It needs the `md_in_html` extension, which is already
switched on in `pelicanconf.py`.
</div>
