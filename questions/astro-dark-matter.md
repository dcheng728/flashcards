<!-- Questions on dark-matter evidence, astrophysical probes, detection methods, and candidate models. -->

### galaxy rotation curves
difficulty: basic
labels: dark-matter, rotation-curves, galaxies

How do galaxy rotation curves provide evidence for dark matter?

---

For circular orbits in a spherical mass distribution,
$$v_c^2(r)=\frac{GM(<r)}{r}.$$
Visible matter predicts Keplerian decline $v_c\propto r^{-1/2}$ beyond the disk, but observed curves stay roughly flat, so $M(<r)\propto r$: an extended dark halo, $\rho\propto r^{-2}$.

---

Equating gravity to centripetal force, $GM(<r)m/r^2=mv_c^2/r$, gives the formula (shell theorem: only interior mass matters).
Velocities come from Doppler shifts: the 21 cm H I line out to large radii, and optical emission lines ($\mathrm{H}\alpha$) in the inner disk.

===

### axion misalignment and relic abundance
difficulty: advanced
labels: dark-matter, axion, misalignment, cosmology

How can the axion misalignment mechanism produce cold dark matter, and what sets the relic abundance?

---

The field $\theta=a/f_a$ obeys $\ddot a+3H\dot a+m_a^2a=0$. It is frozen at $\theta_i$ while $H\gg m_a$, and starts oscillating at $H\sim m_a$. Oscillations redshift as $\rho_a\propto a_{\rm scale}^{-3}$ (cold matter), with
$$\rho_a\sim\tfrac12 m_a^2f_a^2\theta_i^2\left(\frac{a_{\rm osc}}{a_{\rm scale}}\right)^3,\qquad \Omega_a h^2\propto f_a^{7/6}\theta_i^2\ (\propto m_a^{-7/6}\theta_i^2).$$

---

Friction $3H\dot a$ pins the field when $H\gg m_a$; once $H\lesssim m_a$ it is an underdamped oscillator, and the oscillating coherent field averages to pressureless matter ($\langle p\rangle=0$).
The exponent $7/6$ (rather than the naive $3/2$) comes from the temperature dependence of the QCD axion mass, $m_a(T)\propto T^{-4}$ above $\sim$GeV.
Requiring $\Omega_a\le\Omega_{\rm DM}$ with $\theta_i\sim1$ gives $f_a\lesssim10^{12}$ GeV, i.e. $m_a\gtrsim\mu$eV.

===

### axion isocurvature constraint
difficulty: advanced
labels: dark-matter, axion, inflation, cmb, isocurvature

If the Peccei-Quinn symmetry is broken before inflation, how do CMB isocurvature limits constrain the axion?

---

Inflation gives $\delta a\simeq H_I/2\pi$, so $\delta\theta=H_I/(2\pi f_a)$ and
$$\frac{\delta\rho_a}{\rho_a}\simeq\frac{2\,\delta\theta}{\theta_i}\;\Rightarrow\;\mathcal P_S\simeq\frac{H_I^2}{\pi^2f_a^2\theta_i^2}.$$
Planck bounds the isocurvature fraction ($\beta_{\rm iso}\lesssim0.04$) giving $H_I\lesssim10^{7}\,\text{GeV}\,(f_a\theta_i/10^{11}\,\text{GeV})$: an upper limit on $H_I$, hence on $r\propto H_I^2$.

---

Axion fluctuations are uncorrelated with the radiation (adiabatic) perturbations, so they show up as isocurvature in the CMB temperature spectrum.
Since $\rho_a\propto\theta^2$, $\delta\rho/\rho=2\delta\theta/\theta_i$ at linear order.
Large $f_a$ with $\theta_i\sim1$ is therefore in tension with high-scale inflation, unless $\theta_i$ is tuned small or PQ is broken after inflation.

===

### KSVZ vs DFSZ axion models
difficulty: advanced
labels: dark-matter, axion, particle-physics

How do the KSVZ and DFSZ axion models differ, and how do experiments tell them apart?

---

- **KSVZ**: heavy new quarks carry PQ charge; SM fermions are uncharged, so no tree-level axion-fermion couplings (hadronic axion).
- **DFSZ**: two Higgs doublets, and SM fermions carry PQ charge, so the axion couples to electrons and quarks at tree level.

Photon coupling $g_{a\gamma\gamma}=\frac{\alpha}{2\pi f_a}\left(\frac EN-1.92\right)$: $E/N=0$ (minimal KSVZ) vs $8/3$ (DFSZ).

---

The bracket is $|E/N-1.92|\approx0.75$ (DFSZ) vs $1.92$ (KSVZ), so DFSZ photon coupling is about $2.5\times$ weaker and haloscopes (e.g. ADMX) need DFSZ sensitivity to exclude the QCD axion band.
Electron and nucleon couplings, which only DFSZ has at tree level, are probed by stellar cooling (white dwarfs, red giants) and spin-sensitive experiments, so combining them discriminates the models.

===

### axion haloscope sensitivity
difficulty: advanced
labels: dark-matter, axion, detection, haloscope

How does an axion haloscope's signal power depend on its parameters, and what limits the noise?

---

$$P\sim g_{a\gamma\gamma}^2\,\frac{\rho_a}{m_a}\,B^2\,V\,C\,\min(Q_L,Q_a)$$
with $Q_a\sim10^6$ the axion linewidth quality factor and $C$ a mode form factor. The cavity must be tuned to $\omega=m_a$. The scan rate $df/dt\propto g^4B^4V^2Q/T_{\rm sys}^2$.

---

The axion in a static field $B$ sources an effective current, driving the cavity mode on resonance; power grows with $Q_L$ until the cavity linewidth is narrower than the axion linewidth, after which it saturates ($Q_L>Q_a$ gives no gain).
Noise is $T_{\rm sys}=T_{\rm phys}+T_{\rm amp}$ with Johnson noise $k_BT$ and amplifier noise bounded by the standard quantum limit for phase-preserving amplification, $T_{\rm SQL}\approx hf/k_B$ (the noise a high frequency ultimately sets).
Hence the push to quantum-limited amplifiers (JPAs), or photon counting, which evades the SQL at high frequencies where $hf\gg k_BT$.

===
