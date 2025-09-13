# AB Testing: Website Background Color Impact on Session Duration

This project demonstrates an **A/B testing analysis** for a website, measuring whether changing the background color affects **average session duration**. It implements a **right-tailed t-test** for two independent samples with Python and NumPy.

## Features
- Compute basic statistics: mean, standard deviation, and sample size.
- Calculate t-value and degrees of freedom for a two-sample t-test.
- Compute p-value and make a decision on the null hypothesis.
- Modular and reusable Python functions for A/B testing.

## Dataset
`background_color_experiment.csv` contains user session durations for:
- `control`: users who saw the original website.
- `variation`: users who saw the updated background color.

## Usage
```bash
python ab_testing.py

## Structure
ab_testing_session_duration/
│
├── background_color_experiment.csv   # your dataset
├── ab_testing.py                     # main Python module
├── utils.py                          # helper functions
├── tests.py                          # optional: basic unit tests
└── README.md
