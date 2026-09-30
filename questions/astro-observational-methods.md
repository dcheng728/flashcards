<!-- Questions on survey design, observing strategy, photometry, imaging, catalogs, and Rubin data. -->

### photometric redshift
difficulty: intermediate
labels: photometric-redshift, galaxies, survey-methods

How is a photometric redshift estimated from multiband photometry, and why is it uncertain?

---

A photometric redshift, or photo-$z$, estimates a galaxy's redshift by fitting its measured fluxes in several filters to redshifted spectral-energy-distribution templates or a trained model. A template fit can minimize

$$\chi^2(z,\theta)=\sum_i\frac{\left[F_i^{\mathrm{obs}}-aF_i^{\mathrm{model}}(z,\theta)\right]^2}{\sigma_i^2},$$

where $i$ labels filters, $\theta$ describes the galaxy template, and $a$ is its overall normalization.

---

Spectral features like the 4000-Å break and Lyman break shift between filters with redshift, driving the fit. 
Because different galaxy types and redshifts can produce similar colors, the result is a probability distribution $p(z)$, not a single value — its bias and scatter matter for weak-lensing and clustering.

===

### astrophysical filters
difficulty: basic
labels: photometry, filters, colors

What are photometric filters, and why are they useful?

---

A filter transmits light over a selected wavelength band, so a measurement gives the source's flux in that band.

---

For the common $UBVRIJHK$ notation, typical broad-band ranges are approximately:

- $U$ (ultraviolet): $300$–$400$ nm
- $B$ (blue): $400$–$500$ nm
- $V$ (visual): $500$–$600$ nm
- $R$ (red): $600$–$750$ nm
- $I$ (near-infrared): $750$–$900$ nm
- $J$, $H$, $K$ (near-infrared): roughly $1.1$–$1.4$, $1.5$–$1.8$, and $2.0$–$2.4$ μm

Comparing fluxes in different bands gives colors that constrain temperature, dust, galaxy type, and redshift. Exact passbands depend on the instrument.

===

### astronomical unit (AU)
difficulty: basic
labels: units, distance-scale

What is an astronomical unit, and what scale is it used for?

---

1 AU $\approx 1.496\times10^{11}$ m, the mean Earth-Sun distance. Used for solar-system scales.

---

===

### stellar parallax
difficulty: basic
labels: parallax, distance-ladder

What is stellar parallax, and how does it give a distance?

---

The apparent angular shift $p$ of a nearby star against distant background stars, measured from two points on Earth's orbit (a 1 AU baseline, usually 6 months apart). 
Distance follows from $d[\mathrm{pc}] = 1/p[\mathrm{arcsec}]$.

---

The direct, geometric rung of the cosmic distance ladder — no assumptions about the star's physics are needed, only trigonometry. 
Ground-based parallax is limited by atmospheric blurring to $d\lesssim100$ pc; space missions like Gaia reach much further by avoiding atmospheric seeing.

===

### parsec
difficulty: basic
labels: units, distance-scale, parallax

What is a parsec, and how is it defined observationally?

---

A parsec (pc) is the distance at which 1 AU subtends a parallax angle of $1$ arcsecond: $d[\mathrm{pc}] = 1/p[\mathrm{arcsec}]$. 1 pc $\approx 3.086\times10^{16}$ m $\approx 3.26$ light-years.

---

Used for stellar and galactic scales; kpc for galaxies, Mpc–Gpc for cosmology. 
Preferred over light-years in research because it comes directly from an observable (parallax angle).

===

### light-year
difficulty: basic
labels: units, distance-scale

What is a light-year?

---

The distance light travels in one Julian year: 1 ly $\approx 9.461\times10^{15}$ m $\approx 0.307$ pc.

---


===

### cosmic distance ladder
difficulty: basic
labels: distance-ladder, parallax, standard-candles

What is the cosmic distance ladder?

---

A sequence of overlapping distance methods, each calibrated using distances from the rung below: parallax (direct geometry, $\lesssim$ kpc) $\to$ standard candles like Cepheids (calibrated via parallax, $\lesssim$ tens of Mpc) $\to$ Type Ia supernovae (calibrated via Cepheids in their host galaxies, out to Gpc) $\to$ Hubble's law (calibrated via supernovae, largest scales).

---

No single method spans all scales, so each rung's calibration uncertainty propagates to the ones above it. This is a main reason local ($H_0$ ladder) and early-Universe (CMB) measurements of $H_0$ are in tension.

===
