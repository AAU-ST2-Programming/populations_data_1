# Lineær regression med populationsdata

- **Lecture specific files**: files/* - `En mappe som indeholder filer I skal bruge i forbindelse med forlæsningen.`

---

## Forberedelse til lektionen

Følg denne guide nøje for at være klar til undervisningen:

### 1. Literatur

**Primær litteratur:**
- [Data Wrangling with Python af Jacek Gołębiewski (PDF)](https://datawranglingpy.gagolewski.com/datawranglingpy.pdf)
  - Kapitel 9.2.2 From data to (linear) models 
  - Kapitel 5.1.1 Sample quantiles
  - Kapitel 15.1 15.4 Missing Data and Outliers 

**Supplerende litteratur:**
- [GeeksforGeeks: ML | Linear Regression](https://www.geeksforgeeks.org/machine-learning/ml-linear-regression/)
- [TutorialsPoint: SciPy - Linear Curve Fitting](https://www.tutorialspoint.com/scipy/scipy_linear_curve_fitting.htm)
- [scikit-learn: LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)


**Formål:** Forstå hvordan regression bruges til at modellere og validere sammenhænge i populationsdata.

---

### 2. Installationer og opsætning
- Følg denne guide for at installere Python:  
  [Install Python Guide](https://github.com/AAU-Python-Guides/install_python_guide)
- Følg denne guide for at sætte VS Code op til Python:  
  [VS Code for Python Guide](https://github.com/AAU-Python-Guides/visual_studio_code_for_python)
- Installer følgende extensions i Visual Studio Code:
  - `Python`
  - `jupyter`

### 3. Download materialet
> ```zsh
> cd ~
> git clone https://github.com/AAU-ST2-Programming/populations_data_1.git
> cd populations_data_1
> git pull
> ```

---

## Lektionens fokus

- Simpel lineær regression: hældning, skæring og fortolkning
- OLS-udledning og praktisk implementering i NumPy/sklearn
- Modelevaluering med R², RMSE og residualplots
- Multiple lineær regression med flere features
- Håndtering af manglende data og outliers
- Reproducerbar dokumentation og etiske overvejelser i helbredsdata

---

## Forventninger til forberedelse og undervisning

- **Før/efter kursusgang:**
  - Gennemgå tidligere kursusgange (vi bygger videre hver gang)
  - Læs nyt materiale som beskrevet ovenfor
- **Tidsforbrug:**
  - 4 timers forberedelse (hjemme, før undervisning)
  - 4 timers undervisning og gruppeopgaver
  - 4 timers individuel opgaveregning (hjemme, efter undervisning)

---

## Spørgsmål og opgaver

- Til hver opgave i undervisningen vil der være:
  - En opgavebeskrivelse
  - En guide til hvordan opgaven løses
  - Svar på opgaven
- Opgaverne bliver gradvist sværere og bygger på tidligere lektioner.
- Til eksamen vil der kun være en opgavebeskrivelse – du skal selv kunne vurdere, hvordan opgaven løses.
