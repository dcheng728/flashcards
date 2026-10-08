<!-- Questions on how astronomers measure the sky:
- units and scales, brightness and magnitudes,
- filters and colors, spectra and redshift
- image quality (PSF and seeing)
- distance measurement from parallax to the distance ladder. -->

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

### Milky Way reddening
difficulty: basic
labels: dust, extinction, reddening, photometry

What effect does dust in the Milky Way have on light from an astrophysical object before it reaches Earth?

---

Dust causes extinction: it absorbs and scatters some of the light, making the object appear dimmer. Shorter-wavelength (bluer) light is generally attenuated more than longer-wavelength (redder) light, so the observed light is reddened.

---

The wavelength dependence is set by the interstellar grain-size distribution and composition, rather than by pure Rayleigh scattering alone. Extinction is often described by $A_\lambda$ in magnitudes; the color excess $E(B-V)=A_B-A_V$ measures the amount of reddening and can be used to correct photometry.

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

<pre>
  Earth (Jan) o
               \
                \  p
                 \
      Sun  S------* nearby star ----- (fixed background stars)
                 /
                /  p
               /
  Earth (Jul) o

        |&lt;-- 1 AU --&gt;|&lt;------- d = 1/p -------&gt;|
</pre>

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

<pre>
  Gpc      Hubble's law (v = H0 d)
             ^
             | calibrates
  Mpc-Gpc  Type Ia supernovae
             ^
             | calibrates
  ~Mpc     Cepheid standard candles
             ^
             | calibrates
  ~kpc     stellar parallax (direct geometry)
</pre>

---

No single method spans all scales, so each rung's calibration uncertainty propagates to the ones above it. This is a main reason local ($H_0$ ladder) and early-Universe (CMB) measurements of $H_0$ are in tension.

===

### standard candles and intrinsic luminosity
difficulty: basic
labels: standard-candles, luminosity-distance, photometry

What is a standard candle, and how does intrinsic luminosity determine a source's distance?

---

A standard candle is an object with known intrinsic luminosity $L$. Comparing $L$ with the observed flux $F$ gives the luminosity distance through

$$F = \frac{L}{4\pi d_L^2}.$$

---

Intrinsic luminosity is the power emitted by the source; apparent brightness depends on both luminosity and distance. Type Ia supernovae are standardizable candles because their light curves and colors allow $L$ to be calibrated.

===

### types of standard candles
difficulty: basic
labels: standard-candles, distance-ladder

What are the main types of standard candles used in the distance ladder?

---

- **Type Ia supernovae**: white-dwarf disruptions, standardized via light-curve shape and color; reach cosmological distances.
- **Cepheid variables**: pulsating stars with a period-luminosity relation.
- **Tip of the red giant branch (TRGB)**: evolved red giants ignite helium fusion at a nearly fixed luminosity, giving a sharp, standardizable brightness cutoff.

---

Each type is calibrated against a more direct method (ultimately parallax) and used over a different distance range, which is why they chain together into the cosmic distance ladder.

===

### astronomical magnitude
difficulty: basic
labels: magnitude, photometry, distance-modulus

What is the magnitude system, and how do apparent and absolute magnitude differ?

---

$$m=-2.5\log_{10}(F/F_0)$$

- a logarithmic flux scale (larger $m$ = fainter). 
- Apparent magnitude $m$ is how bright an object looks from Earth; absolute magnitude $M$ is its apparent magnitude if placed at $10$ pc (pc means parsec), i.e. its intrinsic luminosity.

---

They're related by the distance modulus, $m-M=5\log_{10}(d/10\,\mathrm{pc})$, for the nearby (non-cosmological) case. The reference flux $F_0$ depends on the photometric system — e.g. the AB system sets $F_0=3631$ Jy — but the $-2.5\log_{10}$ form is universal.

===

### point spread function (PSF)
difficulty: intermediate
labels: imaging, psf, resolution

What is the point spread function (PSF), and how does it relate an observed image to the true sky?

---

The PSF is the image a telescope forms of a point source. The observed image is the true sky convolved with the PSF, $I_{\mathrm{obs}} = I_{\mathrm{true}} \ast \mathrm{PSF}$, usually plus noise. Its width, usually quoted as the FWHM (the full width at half of the peak), sets the angular resolution.

---

The PSF combines diffraction, optical aberrations, the detector, and, from the ground, atmospheric seeing. The diffraction limit alone gives $\theta \approx 1.22\lambda/D$ for a telescope of aperture $D$. PSF knowledge matters for photometry (aperture or PSF fitting), for separating blended sources, and for weak lensing, where PSF errors mimic shear.

===

### atmospheric seeing
difficulty: intermediate
labels: imaging, seeing, atmosphere

What is atmospheric seeing, how is it measured, and what do typical values mean?

---

Seeing is the blurring of a point source by atmospheric turbulence, measured as the FWHM (full width at half-maximum) of the PSF, in arcseconds. Smaller seeing means a smaller FWHM and a sharper image.

---

- $0.5''$: very good seeing
- $1.0''$: blurrier
- $2.0''$: much blurrier

Turbulence varies the refractive index of the air and distorts the wavefront. For apertures larger than the Fried parameter $r_0$ (about $10$–$20$ cm at visible wavelengths), the image size is set by the atmosphere, $\theta \sim \lambda/r_0$, not by the telescope. Space telescopes avoid seeing, and adaptive optics partly corrects it on the ground.

===
