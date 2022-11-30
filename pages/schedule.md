---
layout: page
title: course schedule
description: schedule, with links to slides and homeworks
---

The source code for these lectures is available at
[the github repository](https://github.com/UOdsci/dsci345/).

# Fall 2022

Week 1 (*9/28*): Probability

: Overview of probability and statistics in data science -
    randomness, uncertainty, estimation, and prediction.
    Probability and expectation, conditional probabilities,
    and random variables.

    - Slides: Introduction, and probability [ipynb](../class_material/slides/Week_01_Introduction.ipynb) [html](../class_material/slides/Week_01_Introduction.slides.html)
    - Reading: [Adhikari & Pitman, chapters 1, 2, & 3](http://prob140.org/textbook/content/README.html)
    - *alternative reading:* [Wasserman, chapter 1, 2.1-2.4](https://www.stat.cmu.edu/~larry/all-of-statistics/index.html)
    - Homework (due 10/6): [ipynb](../class_material/homeworks/HW01.ipynb) [html](../class_material/homeworks/HW01.html)

Week 2 (*10/3*): The modeler's toolbox

: Simulation, random variables, properties of and relationships between
    some common probability distributions; computing means,
    variances, and expectations. Stochastic gradient descent.

    - Slides: Random variables [ipynb](../class_material/slides/Week_02_Random_variables.ipynb) [html](../class_material/slides/Week_02_Random_variables.slides.html)
    - Slides: Stochastic gradient descent [ipynb](../class_material/slides/Week_02_Stochastic_gradient_descent.ipynb) [html](../class_material/slides/Week_02_Stochastic_gradient_descent.slides.html)
    - Reading: [Adhikari & Pitman](http://prob140.org/textbook/content/README.html), chapters 4, 6.1-6.3, 6.5, 8, 15.1-15.4.
    - *alternative reading:* [Wasserman, chapters 2 & 3](https://www.stat.cmu.edu/~larry/all-of-statistics/index.html)
    - Homework (due 10/13): [ipynb](../class_material/homeworks/HW02.ipynb) [html](../class_material/homeworks/HW02.html)

Week 3 (*10/10*): Simulation, moments, and overdispersion.

: How to pick "realistic" simulation parameters.
    Central limit theorem.
    Method-of-moments fitting; minimum-variance estimators.
    Outliers and overdispersion: scale mixtures, goodness-of-fit.

    - Slides: Poisson counts [ipynb](../class_material/slides/Week_03_Poisson.ipynb) [html](../class_material/slides/Week_03_Poisson.slides.html)
    - Slides: The central limit theorem and the Normal distribution [ipynb](../class_material/slides/Week_03_Central_limits.ipynb) [html](../class_material/slides/Week_03_Central_limits.slides.html)
    - Slides: Method of moments [ipynb](../class_material/slides/Week_03_Method_of_moments.ipynb) [html](../class_material/slides/Week_03_Method_of_moments.slides.html)
    - Reading: [Adhikari & Pitman, chapters 7, 12.1-2, 13.1-3, 14](http://prob140.org/textbook/content/README.html)
    - Homework (due 10/20): [ipynb](../class_material/homeworks/HW03.ipynb) [html](../class_material/homeworks/HW03.html)

Week 4 (*10/17*): Model choice, categorical prediction, and likelihood.

: Likelihood, p-values, hypothesis testing, power and false positives,
    false discovery rates.

    - Slides: Likelihood [ipynb](../class_material/slides/Week_04_Likelihood.ipynb) [html](../class_material/slides/Week_04_Likelihood.slides.html)
    - Slides: P-values, and hypotheses [ipynb](../class_material/slides/Week_04_Pvalues.ipynb) [html](../class_material/slides/Week_04_Pvalues.slides.html)
    - Reading: [Adhikari & Pitman, chapter 20](http://prob140.org/textbook/content/Chapter_20/01_Maximum_Likelihood.html)
    - *alternative reading:* [Wasserman, chapter 9](https://www.stat.cmu.edu/~larry/all-of-statistics/index.html)
    - Homework (due 10/27): [ipynb](../class_material/homeworks/HW04.ipynb) [html](../class_material/homeworks/HW04.html)

Week 5 (*10/24*): Quantifying uncertainty

: Calibration of estimates of uncertainty;
    asymptotics versus simulation. Review.

    - Slides: Review [ipynb](../class_material/slides/Week_05_Review.ipynb) [html](../class_material/slides/Week_05_Review.slides.html)
    - In-class exercise: Confidence intervals and uncertainty [ipynb](../class_material/slides/Week_05_Exercise_Uncertainty.ipynb) [html](../class_material/slides/Week_05_Exercise_Uncertainty.slides.html)
    - Reading:
        [Adhikari & Pitman, chapter 14](http://prob140.org/textbook/content/Chapter_14/06_Confidence_Intervals.html);
        <!-- [Adhikari & Pitman, chapter 20](http://prob140.org/textbook/content/Chapter_20/03_Prior_and_Posterior.html) -->
    - *alternative reading:* [Wasserman, chapters 8 & 11](https://www.stat.cmu.edu/~larry/all-of-statistics/index.html)
    - Homework (due 11/3): [ipynb](../class_material/homeworks/HW05.ipynb) [html](../class_material/homeworks/HW05.html)

<!--
    - Slides: Power and false positives [ipynb](../class_material/slides/Week_05_Power.ipynb) [html](../class_material/slides/Week_05_Power.slides.html)
    - Slides: The bootstrap [ipynb](../class_material/slides/Week_05_Bootstrap.ipynb) [html](../class_material/slides/Week_05_Bootstrap.slides.html)
-->

Week 6 (*10/31*): Multivariate data and latent structure

: The multivariate Gaussian distribution, autocorrelation, modeling correlated data,
    random walks. Principal components analysis.
    
    - Slides: Correlation and covariance [ipynb](../class_material/slides/Week_06_Covariance.ipynb) [html](../class_material/slides/Week_06_Covariance.slides.html)
    - Slides: Principal components analysis [ipynb](../class_material/slides/Week_06_PCA.ipynb) [html](../class_material/slides/Week_06_PCA.slides.html)
    - Reading: [Adhikari & Pitman, chapter 17.1-17.3](http://prob140.org/textbook/content/Chapter_17/00_Joint_Densities.html)
        and [chapter 23](http://prob140.org/textbook/content/Chapter_23/00_Multivariate_Normal_RVs.html)
    - *alternative reading:* [Wasserman, chapter 14](https://www.stat.cmu.edu/~larry/all-of-statistics/index.html)
    - Homework (due 11/10): [ipynb](../class_material/homeworks/HW06.ipynb) [html](../class_material/homeworks/HW06.html)

Week 7 (*11/7*): Linear models

: Introduction to linear models, and some history of modern statistics.
    Robust models, loss functions and likelihood.

    - Slides: Introduction to linear models [ipynb](../class_material/slides/Week_07_Linear_models.ipynb) [html](../class_material/slides/Week_07_Linear_models.slides.html)
    - Slides: In-class exercise [ipynb](../class_material/slides/Week_07_Exercise_Linear_models.ipynb) [html](../class_material/slides/Week_07_Exercise_Linear_models.slides.html)
    - Slides: Robust models [ipynb](../class_material/slides/Week_07_Robust_models.ipynb) [html](../class_material/slides/Week_07_Robust_models.slides.html)
    - Reading: [Adhikari & Pitman, chapter 24 & 25](http://prob140.org/textbook/content/Chapter_24/00_Simple_Linear_Regression.html)
    - Homework (due 11/17): [ipynb](../class_material/homeworks/HW07.ipynb) [html](../class_material/homeworks/HW07.html)

Week 8 (*11/14*): Generalized linear models

: Response distributions, nonlinear relationships, transformations. <!-- Mixed models. -->

    - Slides: Generalized linear models [ipynb](../class_material/slides/Week_08_Generalized_Linear_Models.ipynb) [html](../class_material/slides/Week_08_Generalized_Linear_Models.slides.html)
    - Slides: Some history [ipynb](../class_material/slides/Week_08_History.ipynb) [html](../class_material/slides/Week_08_History.slides.html)
    - Slides: Nonlinear models [ipynb](../class_material/slides/Week_08_Nonlinear_models.ipynb) [html](../class_material/slides/Week_08_Nonlinear_models.slides.html)
    - Homework (due 11/22): [ipynb](../class_material/homeworks/HW08.ipynb) [html](../class_material/homeworks/HW08.html)

Week 9 (*11/21*): Problems with linear models

: Too many variables, not enough linearity: regularization and diagnostics.

    - Slides: Regularization and crossvalidation [ipynb](../class_material/slides/Week_09_Regularization.ipynb) [html](../class_material/slides/Week_09_Regularization.slides.html)
    - Slides: Transformations and diagnostics [ipynb](../class_material/slides/Week_09_Transformations_and_diagnostics.ipynb) [html](../class_material/slides/Week_09_Transformations_and_diagnostics.slides.html)
    - Homework (due 12/1): [ipynb](../class_material/homeworks/HW09.ipynb) [html](../class_material/homeworks/HW09.html)

Week 10 (*11/28*): Prediction and inference revisited

: The bootstrap; Identifiability, ill-posed inference, non-convex optimization.

    - Slides: Uncertainty and the bootstrap [ipynb](../class_material/slides/Week_10_Uncertainty.ipynb) [html](../class_material/slides/Week_10_Uncertainty.slides.html)
    - Slides: Interpolation and ill-posedness [ipynb](../class_material/slides/Week_10_Ill_posedness.ipynb) [html](../class_material/slides/Week_10_Ill_posedness.slides.html)
    - Slides: Review [ipynb](../class_material/slides/Week_10_Review.ipynb) [html](../class_material/slides/Week_10_Review.slides.html)
    - Reading: 
        [Adhikari DeNero & Wagner, chapter 13](https://inferentialthinking.com/chapters/13/2/Bootstrap.html)
    - *alternative reading:* [Wasserman, chapter 8](https://www.stat.cmu.edu/~larry/all-of-statistics/index.html)
    - Final (due 12/8): [ipynb](../class_material/homeworks/HW10.ipynb) [html](../class_material/homeworks/HW10.html)

