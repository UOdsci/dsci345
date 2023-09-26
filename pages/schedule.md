---
layout: page
title: course schedule
description: schedule, with links to slides and homeworks
---

The source code for these lectures is available at
[the github repository](https://github.com/UOdsci/dsci345/).
The schedule (with slides and homeworks) from Spring 2023 is available [here](spring_2023_schedule.html),
and from Fall 2022 [here](fall_2022_schedule.html).

# Fall 2023

Week 1: Probability

: Overview of probability and statistics in data science -
    randomness, uncertainty, estimation, and prediction.
    Probability and expectation, conditional probabilities,
    and random variables.

    - Slides: Introduction, and probability [ipynb](../class_material/slides/Introduction.ipynb) [html](../class_material/slides/Introduction.slides.html)
    - Slides: Random variables [ipynb](../class_material/slides/Random_variables.ipynb) [html](../class_material/slides/Random_variables.slides.html)
    - Reading: [Adhikari & Pitman, chapters 1, 2, & 3](http://prob140.org/textbook/content/README.html)
    - *alternative reading:* [Wasserman, chapter 1, 2.1-2.4](https://www.stat.cmu.edu/~larry/all-of-statistics/index.html)
    - Short Homework: [ipynb](../class_material/homeworks/HW00.ipynb) [html](../class_material/homeworks/HW00.html)
    - Homework: [ipynb](../class_material/homeworks/HW01.ipynb) [html](../class_material/homeworks/HW01.html)

Week 2: The modeler's toolbox

: Simulation, random variables, properties of and relationships between
    some common probability distributions; computing means,
    variances, and expectations. Stochastic gradient descent.

    - Slides: Stochastic gradient descent [ipynb](../class_material/slides/Stochastic_gradient_descent.ipynb) [html](../class_material/slides/Stochastic_gradient_descent.slides.html)
    - Slides: Poisson counts [ipynb](../class_material/slides/Poisson.ipynb) [html](../class_material/slides/Poisson.slides.html)
    - Reading: [Adhikari & Pitman](http://prob140.org/textbook/content/README.html), chapters 4, 6.1-6.3, 6.5, 8, 15.1-15.4.
    - *alternative reading:* [Wasserman, chapters 2 & 3](https://www.stat.cmu.edu/~larry/all-of-statistics/index.html)
<!--    - Homework: [ipynb](../class_material/homeworks/HW02.ipynb) [html](../class_material/homeworks/HW02.html)
-->
Week 3: Simulation, moments, and overdispersion.

: How to pick "realistic" simulation parameters.
    Central limit theorem.
    Method-of-moments fitting; minimum-variance estimators.
    Outliers and overdispersion: scale mixtures, goodness-of-fit.

    - Slides: Poisson counts (continued) [ipynb](../class_material/slides/Poisson.ipynb) [html](../class_material/slides/Poisson.slides.html)
    - Slides: Method of moments [ipynb](../class_material/slides/Method_of_moments.ipynb) [html](../class_material/slides/Method_of_moments.slides.html)
    - Slides: The central limit theorem and the Normal distribution [ipynb](../class_material/slides/Central_limits.ipynb) [html](../class_material/slides/Central_limits.slides.html)
    - Reading: [Adhikari & Pitman, chapters 7, 12.1-2, 13.1-3, 14](http://prob140.org/textbook/content/README.html)
<!--    - Homework: [ipynb](../class_material/homeworks/HW03.ipynb) [html](../class_material/homeworks/HW03.html)
-->

Week 4: Model choice, categorical prediction, and likelihood.

: Likelihood, p-values, hypothesis testing, power and false positives,
    false discovery rates.

    - Slides: Likelihood [ipynb](../class_material/slides/Likelihood.ipynb) [html](../class_material/slides/Likelihood.slides.html)
    - Reading: [Adhikari & Pitman, chapter 20](http://prob140.org/textbook/content/Chapter_20/01_Maximum_Likelihood.html)
    - *alternative reading:* [Wasserman, chapter 9](https://www.stat.cmu.edu/~larry/all-of-statistics/index.html)
<!--    - Homework: [ipynb](../class_material/homeworks/HW04.ipynb) [html](../class_material/homeworks/HW04.html)
-->

Week 5: Quantifying uncertainty

: Calibration of estimates of uncertainty;
    asymptotics versus simulation. Review.

    - Slides: P-values, and hypotheses [ipynb](../class_material/slides/Pvalues.ipynb) [html](../class_material/slides/Pvalues.slides.html)
    - In-class exercise: Confidence intervals and uncertainty [ipynb](../class_material/slides/Uncertainty.ipynb) [html](../class_material/slides/Uncertainty.slides.html)
    - Slides: Power and false positives [ipynb](../class_material/slides/Power.ipynb) [html](../class_material/slides/Power.slides.html)
    - Reading:
        [Adhikari & Pitman, chapter 14](http://prob140.org/textbook/content/Chapter_14/06_Confidence_Intervals.html);
    - *alternative reading:* [Wasserman, chapters 8 & 11](https://www.stat.cmu.edu/~larry/all-of-statistics/index.html)
<!--    - Homework: [ipynb](../class_material/homeworks/HW05.ipynb) [html](../class_material/homeworks/HW05.html)
-->

<!--
    - Slides: Review [ipynb](../class_material/slides/Week_05_Review.ipynb) [html](../class_material/slides/Week_05_Review.slides.html)
-->

<!--
        [Adhikari & Pitman, chapter 20](http://prob140.org/textbook/content/Chapter_20/03_Prior_and_Posterior.html)
-->

Week 6: Multivariate data and latent structure

: The multivariate Gaussian distribution, autocorrelation, modeling correlated data,
    random walks. Principal components analysis.

    - Slides: Correlation and covariance [ipynb](../class_material/slides/Covariance.ipynb) [html](../class_material/slides/Covariance.slides.html)
    - Reading: [Adhikari & Pitman, chapter 17.1-17.3](http://prob140.org/textbook/content/Chapter_17/00_Joint_Densities.html)
        and [chapter 23](http://prob140.org/textbook/content/Chapter_23/00_Multivariate_Normal_RVs.html)
    - *alternative reading:* [Wasserman, chapter 14](https://www.stat.cmu.edu/~larry/all-of-statistics/index.html)
<!--    - Homework: [ipynb](../class_material/homeworks/HW06.ipynb) [html](../class_material/homeworks/HW06.html)
-->

Week 7: Linear models

: Introduction to linear models, and some history of modern statistics.
    Robust models, loss functions and likelihood.

    - Slides: Principal components analysis [ipynb](../class_material/slides/PCA.ipynb) [html](../class_material/slides/PCA.slides.html)
    - Slides: Introduction to linear models [ipynb](../class_material/slides/Linear_models.ipynb) [html](../class_material/slides/Linear_models.slides.html)
    - Slides: In-class exercise [ipynb](../class_material/slides/Exercise_Linear_models.ipynb) [html](../class_material/slides/Exercise_Linear_models.slides.html)
    - Reading: [Adhikari & Pitman, chapter 24 & 25](http://prob140.org/textbook/content/Chapter_24/00_Simple_Linear_Regression.html)
<!--    - Homework: [ipynb](../class_material/homeworks/HW07.ipynb) [html](../class_material/homeworks/HW07.html)
-->`
Week 8: Generalized linear models

: Response distributions, nonlinear relationships, transformations. <!-- Mixed models. -->

    - Slides: Some history [ipynb](../class_material/slides/History.ipynb) [html](../class_material/slides/History.slides.html)
    - Slides: Robust models [ipynb](../class_material/slides/Robust_models.ipynb) [html](../class_material/slides/Robust_models.slides.html)
    - Slides: Generalized linear models [ipynb](../class_material/slides/Generalized_Linear_Models.ipynb) [html](../class_material/slides/Generalized_Linear_Models.slides.html)
    - Slides: Nonlinear models [ipynb](../class_material/slides/Nonlinear_models.ipynb) [html](../class_material/slides/Nonlinear_models.slides.html)
<!--
- Homework: [ipynb](../class_material/homeworks/HW08.ipynb) [html](../class_material/homeworks/HW08.html)
-->

Week 9: Problems with linear models

: Too many variables, not enough linearity: regularization and diagnostics.

    - Slides: Transformations and diagnostics [ipynb](../class_material/slides/Transformations_and_diagnostics.ipynb) [html](../class_material/slides/Transformations_and_diagnostics.slides.html)
    - Slides: Regularization and crossvalidation [ipynb](../class_material/slides/Regularization.ipynb) [html](../class_material/slides/Regularization.slides.html)
<!--
- Homework: [ipynb](../class_material/homeworks/HW09.ipynb) [html](../class_material/homeworks/HW09.html)
-->

Week 10: Prediction and inference revisited

: The bootstrap; Identifiability, ill-posed inference, non-convex optimization.

    - Slides: Uncertainty and the bootstrap [ipynb](../class_material/slides/Bootstrap.ipynb) [html](../class_material/slides/Bootstrap.slides.html)
    - Slides: Interpolation and ill-posedness [ipynb](../class_material/slides/Ill_posedness.ipynb) [html](../class_material/slides/Ill_posedness.slides.html)
    - Slides: Review [ipynb](../class_material/slides/Review.ipynb) [html](../class_material/slides/Review.slides.html)
    - Reading: 
        [Adhikari DeNero & Wagner, chapter 13](https://inferentialthinking.com/chapters/13/2/Bootstrap.html)
    - *alternative reading:* [Wasserman, chapter 8](https://www.stat.cmu.edu/~larry/all-of-statistics/index.html)
<!--    - Final: [ipynb](../class_material/homeworks/HW10.ipynb) [html](../class_material/homeworks/HW10.html) -->
