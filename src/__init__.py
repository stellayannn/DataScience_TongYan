{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# T81-577 Applied Data Science Individual Project\n",
    "# Mobile Strategy Games User Rating Prediction\n",
    "# Tong Yan"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Table of Contents:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Project Overview\n",
    "\n",
    "\n",
    "- Data Exploration\n",
    "\n",
    "\n",
    "- Data Preprocessing\n",
    "\n",
    "\n",
    "- Predictive Modelling\n",
    "\n",
    "  4.1 Split dataset into train/test\n",
    "\n",
    "  4.2 Create pipelines\n",
    "\n",
    "  4.3 Model fitting & Making prediction\n",
    "  \n",
    "        4.3.1 Linear Regression\n",
    "\n",
    "        4.3.2 Random Forest\n",
    "\n",
    "        4.3.3 Gradient Boosting\n",
    "\n",
    "- Model Comparasion & Selection\n",
    "\n",
    "\n",
    "- Conclusion\n",
    "\n",
    "\n",
    "- Business applications & limitations\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1. Project Overview"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "For this project, I will be using the 'appstore_games.csv' dataset (https://www.kaggle.com/tristan581/17k-apple-app-store-strategy-games) to predict the average user ratings of mobile strategy games using features including game genres, app price, in-app purchases, app size, etc. Game descriptions and text mining will not be involved in this project. \n",
    "\n",
    "I will primarily focus on data exploration, data preprocessing and predictive modelling. I will try 3 different regression models, and use Hyperparameter Tuning methods to try to improve model performance. Then I will decide a final model with the lowest ROOT MEAN SQURE ERROR (RMSE) and output the predicting result for the testing dataset. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 2. Data Exploration"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Help on package seaborn:\n",
      "\n",
      "NAME\n",
      "    seaborn - # Capture the original matplotlib rcParams\n",
      "\n",
      "PACKAGE CONTENTS\n",
      "    algorithms\n",
      "    apionly\n",
      "    axisgrid\n",
      "    categorical\n",
      "    cm\n",
      "    colors (package)\n",
      "    conftest\n",
      "    distributions\n",
      "    external (package)\n",
      "    linearmodels\n",
      "    matrix\n",
      "    miscplot\n",
      "    palettes\n",
      "    rcmod\n",
      "    regression\n",
      "    relational\n",
      "    tests (package)\n",
      "    timeseries\n",
      "    utils\n",
      "    widgets\n",
      "\n",
      "DATA\n",
      "    crayons = {'Almond': '#EFDECD', 'Antique Brass': '#CD9575', 'Apricot':...\n",
      "    xkcd_rgb = {'acid green': '#8ffe09', 'adobe': '#bd6c48', 'algae': '#54...\n",
      "\n",
      "VERSION\n",
      "    0.10.0\n",
      "\n",
      "FILE\n",
      "    /opt/anaconda3/envs/tensorflow/lib/python3.7/site-packages/seaborn/__init__.py\n",
      "\n",
      "\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import warnings\n",
    "\n",
    "help(sns)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 17007 entries, 0 to 17006\n",
      "Data columns (total 18 columns):\n",
      "URL                             17007 non-null object\n",
      "ID                              17007 non-null int64\n",
      "Name                            17007 non-null object\n",
      "Subtitle                        5261 non-null object\n",
      "Icon URL                        17007 non-null object\n",
      "Average User Rating             7561 non-null float64\n",
      "User Rating Count               7561 non-null float64\n",
      "Price                           16983 non-null float64\n",
      "In-app Purchases                7683 non-null object\n",
      "Description                     17007 non-null object\n",
      "Developer                       17007 non-null object\n",
      "Age Rating                      17007 non-null object\n",
      "Languages                       16947 non-null object\n",
      "Size                            17006 non-null float64\n",
      "Primary Genre                   17007 non-null object\n",
      "Genres                          17007 non-null object\n",
      "Original Release Date           17007 non-null object\n",
      "Current Version Release Date    17007 non-null object\n",
      "dtypes: float64(4), int64(1), object(13)\n",
      "memory usage: 2.3+ MB\n"
     ]
    }
   ],
   "source": [
    "# Have a primary look at the dataset\n",
    "df = pd.read_csv('https://raw.githubusercontent.com/stellayannn/DataScience_TongYan/master/data/appstore_games.csv', na_values = ['NA', '?'])\n",
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "URL                                 0\n",
       "ID                                  0\n",
       "Name                                0\n",
       "Subtitle                        11746\n",
       "Icon URL                            0\n",
       "Average User Rating              9446\n",
       "User Rating Count                9446\n",
       "Price                              24\n",
       "In-app Purchases                 9324\n",
       "Description                         0\n",
       "Developer                           0\n",
       "Age Rating                          0\n",
       "Languages                          60\n",
       "Size                                1\n",
       "Primary Genre                       0\n",
       "Genres                              0\n",
       "Original Release Date               0\n",
       "Current Version Release Date        0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Look at the summary of null value\n",
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>URL</th>\n",
       "      <th>ID</th>\n",
       "      <th>Name</th>\n",
       "      <th>Subtitle</th>\n",
       "      <th>Icon URL</th>\n",
       "      <th>Average User Rating</th>\n",
       "      <th>User Rating Count</th>\n",
       "      <th>Price</th>\n",
       "      <th>In-app Purchases</th>\n",
       "      <th>Description</th>\n",
       "      <th>Developer</th>\n",
       "      <th>Age Rating</th>\n",
       "      <th>Languages</th>\n",
       "      <th>Size</th>\n",
       "      <th>Primary Genre</th>\n",
       "      <th>Genres</th>\n",
       "      <th>Original Release Date</th>\n",
       "      <th>Current Version Release Date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>https://apps.apple.com/us/app/sudoku/id284921427</td>\n",
       "      <td>284921427</td>\n",
       "      <td>Sudoku</td>\n",
       "      <td>NaN</td>\n",
       "      <td>https://is2-ssl.mzstatic.com/image/thumb/Purpl...</td>\n",
       "      <td>4.0</td>\n",
       "      <td>3553.0</td>\n",
       "      <td>2.99</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Join over 21,000,000 of our fans and download ...</td>\n",
       "      <td>Mighty Mighty Good Games</td>\n",
       "      <td>4+</td>\n",
       "      <td>DA, NL, EN, FI, FR, DE, IT, JA, KO, NB, PL, PT...</td>\n",
       "      <td>15853568.0</td>\n",
       "      <td>Games</td>\n",
       "      <td>Games, Strategy, Puzzle</td>\n",
       "      <td>11/07/2008</td>\n",
       "      <td>30/05/2017</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>https://apps.apple.com/us/app/reversi/id284926400</td>\n",
       "      <td>284926400</td>\n",
       "      <td>Reversi</td>\n",
       "      <td>NaN</td>\n",
       "      <td>https://is4-ssl.mzstatic.com/image/thumb/Purpl...</td>\n",
       "      <td>3.5</td>\n",
       "      <td>284.0</td>\n",
       "      <td>1.99</td>\n",
       "      <td>NaN</td>\n",
       "      <td>The classic game of Reversi, also known as Oth...</td>\n",
       "      <td>Kiss The Machine</td>\n",
       "      <td>4+</td>\n",
       "      <td>EN</td>\n",
       "      <td>12328960.0</td>\n",
       "      <td>Games</td>\n",
       "      <td>Games, Strategy, Board</td>\n",
       "      <td>11/07/2008</td>\n",
       "      <td>17/05/2018</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>https://apps.apple.com/us/app/morocco/id284946595</td>\n",
       "      <td>284946595</td>\n",
       "      <td>Morocco</td>\n",
       "      <td>NaN</td>\n",
       "      <td>https://is5-ssl.mzstatic.com/image/thumb/Purpl...</td>\n",
       "      <td>3.0</td>\n",
       "      <td>8376.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Play the classic strategy game Othello (also k...</td>\n",
       "      <td>Bayou Games</td>\n",
       "      <td>4+</td>\n",
       "      <td>EN</td>\n",
       "      <td>674816.0</td>\n",
       "      <td>Games</td>\n",
       "      <td>Games, Board, Strategy</td>\n",
       "      <td>11/07/2008</td>\n",
       "      <td>5/09/2017</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>https://apps.apple.com/us/app/sudoku-free/id28...</td>\n",
       "      <td>285755462</td>\n",
       "      <td>Sudoku (Free)</td>\n",
       "      <td>NaN</td>\n",
       "      <td>https://is3-ssl.mzstatic.com/image/thumb/Purpl...</td>\n",
       "      <td>3.5</td>\n",
       "      <td>190394.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Top 100 free app for over a year.\\nRated \"Best...</td>\n",
       "      <td>Mighty Mighty Good Games</td>\n",
       "      <td>4+</td>\n",
       "      <td>DA, NL, EN, FI, FR, DE, IT, JA, KO, NB, PL, PT...</td>\n",
       "      <td>21552128.0</td>\n",
       "      <td>Games</td>\n",
       "      <td>Games, Strategy, Puzzle</td>\n",
       "      <td>23/07/2008</td>\n",
       "      <td>30/05/2017</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>https://apps.apple.com/us/app/senet-deluxe/id2...</td>\n",
       "      <td>285831220</td>\n",
       "      <td>Senet Deluxe</td>\n",
       "      <td>NaN</td>\n",
       "      <td>https://is1-ssl.mzstatic.com/image/thumb/Purpl...</td>\n",
       "      <td>3.5</td>\n",
       "      <td>28.0</td>\n",
       "      <td>2.99</td>\n",
       "      <td>NaN</td>\n",
       "      <td>\"Senet Deluxe - The Ancient Game of Life and A...</td>\n",
       "      <td>RoGame Software</td>\n",
       "      <td>4+</td>\n",
       "      <td>DA, NL, EN, FR, DE, EL, IT, JA, KO, NO, PT, RU...</td>\n",
       "      <td>34689024.0</td>\n",
       "      <td>Games</td>\n",
       "      <td>Games, Strategy, Board, Education</td>\n",
       "      <td>18/07/2008</td>\n",
       "      <td>22/07/2018</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                                 URL         ID  \\\n",
       "0   https://apps.apple.com/us/app/sudoku/id284921427  284921427   \n",
       "1  https://apps.apple.com/us/app/reversi/id284926400  284926400   \n",
       "2  https://apps.apple.com/us/app/morocco/id284946595  284946595   \n",
       "3  https://apps.apple.com/us/app/sudoku-free/id28...  285755462   \n",
       "4  https://apps.apple.com/us/app/senet-deluxe/id2...  285831220   \n",
       "\n",
       "            Name Subtitle                                           Icon URL  \\\n",
       "0         Sudoku      NaN  https://is2-ssl.mzstatic.com/image/thumb/Purpl...   \n",
       "1        Reversi      NaN  https://is4-ssl.mzstatic.com/image/thumb/Purpl...   \n",
       "2        Morocco      NaN  https://is5-ssl.mzstatic.com/image/thumb/Purpl...   \n",
       "3  Sudoku (Free)      NaN  https://is3-ssl.mzstatic.com/image/thumb/Purpl...   \n",
       "4   Senet Deluxe      NaN  https://is1-ssl.mzstatic.com/image/thumb/Purpl...   \n",
       "\n",
       "   Average User Rating  User Rating Count  Price In-app Purchases  \\\n",
       "0                  4.0             3553.0   2.99              NaN   \n",
       "1                  3.5              284.0   1.99              NaN   \n",
       "2                  3.0             8376.0   0.00              NaN   \n",
       "3                  3.5           190394.0   0.00              NaN   \n",
       "4                  3.5               28.0   2.99              NaN   \n",
       "\n",
       "                                         Description  \\\n",
       "0  Join over 21,000,000 of our fans and download ...   \n",
       "1  The classic game of Reversi, also known as Oth...   \n",
       "2  Play the classic strategy game Othello (also k...   \n",
       "3  Top 100 free app for over a year.\\nRated \"Best...   \n",
       "4  \"Senet Deluxe - The Ancient Game of Life and A...   \n",
       "\n",
       "                  Developer Age Rating  \\\n",
       "0  Mighty Mighty Good Games         4+   \n",
       "1          Kiss The Machine         4+   \n",
       "2               Bayou Games         4+   \n",
       "3  Mighty Mighty Good Games         4+   \n",
       "4           RoGame Software         4+   \n",
       "\n",
       "                                           Languages        Size  \\\n",
       "0  DA, NL, EN, FI, FR, DE, IT, JA, KO, NB, PL, PT...  15853568.0   \n",
       "1                                                 EN  12328960.0   \n",
       "2                                                 EN    674816.0   \n",
       "3  DA, NL, EN, FI, FR, DE, IT, JA, KO, NB, PL, PT...  21552128.0   \n",
       "4  DA, NL, EN, FR, DE, EL, IT, JA, KO, NO, PT, RU...  34689024.0   \n",
       "\n",
       "  Primary Genre                             Genres Original Release Date  \\\n",
       "0         Games            Games, Strategy, Puzzle            11/07/2008   \n",
       "1         Games             Games, Strategy, Board            11/07/2008   \n",
       "2         Games             Games, Board, Strategy            11/07/2008   \n",
       "3         Games            Games, Strategy, Puzzle            23/07/2008   \n",
       "4         Games  Games, Strategy, Board, Education            18/07/2008   \n",
       "\n",
       "  Current Version Release Date  \n",
       "0                   30/05/2017  \n",
       "1                   17/05/2018  \n",
       "2                    5/09/2017  \n",
       "3                   30/05/2017  \n",
       "4                   22/07/2018  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Get familiar with the dataframe structure\n",
    "df.head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Drop useless columns\n",
    "df = df.drop(['URL','ID','Name','Icon URL', 'Primary Genre', 'Subtitle', \n",
    "              'Description', 'Developer', 'Languages','Original Release Date',\n",
    "              'Current Version Release Date'], axis = 1)\n",
    "\n",
    "# Rename columns\n",
    "df.columns = ['ave_rating', 'rating_count', 'price', 'inapp_purchase', \n",
    "              'age_rating', 'size', 'genre']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>ave_rating</th>\n",
       "      <th>rating_count</th>\n",
       "      <th>price</th>\n",
       "      <th>inapp_purchase</th>\n",
       "      <th>age_rating</th>\n",
       "      <th>size</th>\n",
       "      <th>genre</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>4.0</td>\n",
       "      <td>3553.0</td>\n",
       "      <td>2.99</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4+</td>\n",
       "      <td>15853568.0</td>\n",
       "      <td>Games, Strategy, Puzzle</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>3.5</td>\n",
       "      <td>284.0</td>\n",
       "      <td>1.99</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4+</td>\n",
       "      <td>12328960.0</td>\n",
       "      <td>Games, Strategy, Board</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3.0</td>\n",
       "      <td>8376.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4+</td>\n",
       "      <td>674816.0</td>\n",
       "      <td>Games, Board, Strategy</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3.5</td>\n",
       "      <td>190394.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4+</td>\n",
       "      <td>21552128.0</td>\n",
       "      <td>Games, Strategy, Puzzle</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>3.5</td>\n",
       "      <td>28.0</td>\n",
       "      <td>2.99</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4+</td>\n",
       "      <td>34689024.0</td>\n",
       "      <td>Games, Strategy, Board, Education</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>3.0</td>\n",
       "      <td>47.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>1.99</td>\n",
       "      <td>4+</td>\n",
       "      <td>48672768.0</td>\n",
       "      <td>Games, Entertainment, Strategy, Puzzle</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>2.5</td>\n",
       "      <td>35.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4+</td>\n",
       "      <td>6328320.0</td>\n",
       "      <td>Games, Entertainment, Puzzle, Strategy</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>2.5</td>\n",
       "      <td>125.0</td>\n",
       "      <td>0.99</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4+</td>\n",
       "      <td>64333824.0</td>\n",
       "      <td>Games, Strategy, Board</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>2.5</td>\n",
       "      <td>44.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4+</td>\n",
       "      <td>2657280.0</td>\n",
       "      <td>Games, Strategy, Board, Entertainment</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>2.5</td>\n",
       "      <td>184.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4+</td>\n",
       "      <td>1466515.0</td>\n",
       "      <td>Games, Casual, Strategy</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   ave_rating  rating_count  price inapp_purchase age_rating        size  \\\n",
       "0         4.0        3553.0   2.99            NaN         4+  15853568.0   \n",
       "1         3.5         284.0   1.99            NaN         4+  12328960.0   \n",
       "2         3.0        8376.0   0.00            NaN         4+    674816.0   \n",
       "3         3.5      190394.0   0.00            NaN         4+  21552128.0   \n",
       "4         3.5          28.0   2.99            NaN         4+  34689024.0   \n",
       "5         3.0          47.0   0.00           1.99         4+  48672768.0   \n",
       "6         2.5          35.0   0.00            NaN         4+   6328320.0   \n",
       "7         2.5         125.0   0.99            NaN         4+  64333824.0   \n",
       "8         2.5          44.0   0.00            NaN         4+   2657280.0   \n",
       "9         2.5         184.0   0.00            NaN         4+   1466515.0   \n",
       "\n",
       "                                    genre  \n",
       "0                 Games, Strategy, Puzzle  \n",
       "1                  Games, Strategy, Board  \n",
       "2                  Games, Board, Strategy  \n",
       "3                 Games, Strategy, Puzzle  \n",
       "4       Games, Strategy, Board, Education  \n",
       "5  Games, Entertainment, Strategy, Puzzle  \n",
       "6  Games, Entertainment, Puzzle, Strategy  \n",
       "7                  Games, Strategy, Board  \n",
       "8   Games, Strategy, Board, Entertainment  \n",
       "9                 Games, Casual, Strategy  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 720x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Have a look at the distribuiton of average rating\n",
    "plt.figure(figsize = (10,6))\n",
    "img1 = sns.countplot(x = df['ave_rating'])\n",
    "img1.set(xlabel = 'average rating', ylabel = 'count')\n",
    "img1.plot()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1440x720 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Have a look at the distribuiton of price\n",
    "plt.figure(figsize = (20,10))\n",
    "img2 = sns.countplot(x = df['price'])\n",
    "img2.set(xlabel = 'price', ylabel = 'count')\n",
    "img2.plot()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 720x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Have a look at the distribuiton of age ratings\n",
    "plt.figure(figsize = (10,6))\n",
    "img3 = sns.countplot(x = df['age_rating'])\n",
    "img3.set(xlabel = 'age rating', ylabel = 'count')\n",
    "img3.plot()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a list of genres\n",
    "list = []\n",
    "for i in range(len(df)):\n",
    "    for j in df['genre'][i].split(','):\n",
    "        list.append(j)\n",
    "\n",
    "# Select the top20 most common genres from the list\n",
    "from collections import Counter\n",
    "c = Counter(list)\n",
    "top_genre = pd.DataFrame(c.most_common(20))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1800x720 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Have a look at the distribuiton of gneres\n",
    "plt.figure(figsize = (25,10))\n",
    "img4 = sns.barplot(x = top_genre[0], y = top_genre[1])\n",
    "img4.set(xlabel = 'genre', ylabel = 'count')\n",
    "img4.plot()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1152x576 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Have a look at the distribuiton of app sizes\n",
    "plt.figure(figsize = (16,8))\n",
    "img5 = sns.distplot(df['size'])\n",
    "img5.set(xlabel = 'size', ylabel = 'count')\n",
    "img5.plot()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 3. Data Preprocessing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Drop the rows wihtout 'ave_rating' value\n",
    "df1 = df.drop(df[np.isnan(df['ave_rating'])].index)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Drop the rows wihtout 'size' value\n",
    "df1.drop(df1[np.isnan(df1['size'])].index, inplace = True)\n",
    "\n",
    "# Drop the rows with 'rating_count' less than 5\n",
    "df1.drop(df1[df1['rating_count'] < 5].index, inplace = True)\n",
    "\n",
    "df1.reset_index(inplace = True, drop = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>ave_rating</th>\n",
       "      <th>rating_count</th>\n",
       "      <th>price</th>\n",
       "      <th>inapp_purchase</th>\n",
       "      <th>age_rating</th>\n",
       "      <th>size</th>\n",
       "      <th>genre</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>4.0</td>\n",
       "      <td>3553.0</td>\n",
       "      <td>2.99</td>\n",
       "      <td>0</td>\n",
       "      <td>4+</td>\n",
       "      <td>15853568.0</td>\n",
       "      <td>Games, Strategy, Puzzle</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>3.5</td>\n",
       "      <td>284.0</td>\n",
       "      <td>1.99</td>\n",
       "      <td>0</td>\n",
       "      <td>4+</td>\n",
       "      <td>12328960.0</td>\n",
       "      <td>Games, Strategy, Board</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3.0</td>\n",
       "      <td>8376.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0</td>\n",
       "      <td>4+</td>\n",
       "      <td>674816.0</td>\n",
       "      <td>Games, Board, Strategy</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3.5</td>\n",
       "      <td>190394.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0</td>\n",
       "      <td>4+</td>\n",
       "      <td>21552128.0</td>\n",
       "      <td>Games, Strategy, Puzzle</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>3.5</td>\n",
       "      <td>28.0</td>\n",
       "      <td>2.99</td>\n",
       "      <td>0</td>\n",
       "      <td>4+</td>\n",
       "      <td>34689024.0</td>\n",
       "      <td>Games, Strategy, Board, Education</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7556</th>\n",
       "      <td>3.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0</td>\n",
       "      <td>12+</td>\n",
       "      <td>151308288.0</td>\n",
       "      <td>Games, Strategy, Entertainment, Puzzle</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7557</th>\n",
       "      <td>5.0</td>\n",
       "      <td>30.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0</td>\n",
       "      <td>4+</td>\n",
       "      <td>79646720.0</td>\n",
       "      <td>Games, Entertainment, Action, Strategy</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7558</th>\n",
       "      <td>5.0</td>\n",
       "      <td>51.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0</td>\n",
       "      <td>9+</td>\n",
       "      <td>125348864.0</td>\n",
       "      <td>Games, Simulation, Strategy</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7559</th>\n",
       "      <td>5.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0</td>\n",
       "      <td>4+</td>\n",
       "      <td>128687104.0</td>\n",
       "      <td>Games, Simulation, Strategy</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7560</th>\n",
       "      <td>5.0</td>\n",
       "      <td>33.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0</td>\n",
       "      <td>4+</td>\n",
       "      <td>8845312.0</td>\n",
       "      <td>Games, Strategy, Board, Utilities</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>7561 rows × 7 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      ave_rating  rating_count  price inapp_purchase age_rating         size  \\\n",
       "0            4.0        3553.0   2.99              0         4+   15853568.0   \n",
       "1            3.5         284.0   1.99              0         4+   12328960.0   \n",
       "2            3.0        8376.0   0.00              0         4+     674816.0   \n",
       "3            3.5      190394.0   0.00              0         4+   21552128.0   \n",
       "4            3.5          28.0   2.99              0         4+   34689024.0   \n",
       "...          ...           ...    ...            ...        ...          ...   \n",
       "7556         3.0           6.0   0.00              0        12+  151308288.0   \n",
       "7557         5.0          30.0   0.00              0         4+   79646720.0   \n",
       "7558         5.0          51.0   0.00              0         9+  125348864.0   \n",
       "7559         5.0           5.0   0.00              0         4+  128687104.0   \n",
       "7560         5.0          33.0   0.00              0         4+    8845312.0   \n",
       "\n",
       "                                       genre  \n",
       "0                    Games, Strategy, Puzzle  \n",
       "1                     Games, Strategy, Board  \n",
       "2                     Games, Board, Strategy  \n",
       "3                    Games, Strategy, Puzzle  \n",
       "4          Games, Strategy, Board, Education  \n",
       "...                                      ...  \n",
       "7556  Games, Strategy, Entertainment, Puzzle  \n",
       "7557  Games, Entertainment, Action, Strategy  \n",
       "7558             Games, Simulation, Strategy  \n",
       "7559             Games, Simulation, Strategy  \n",
       "7560       Games, Strategy, Board, Utilities  \n",
       "\n",
       "[7561 rows x 7 columns]"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Impute values for column 'inapp_purchase' \n",
    "df1['inapp_purchase'].fillna(int(0), inplace = True)\n",
    "df1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Replace objects in 'inapp_purchase' with mean of in-app purchase prices of that game\n",
    "for i in range(len(df1)): \n",
    "    # Assign non-null object to a variable and replace the cell with 0\n",
    "    if df1.loc[i, 'inapp_purchase'] != 0:\n",
    "        inapp = df1.loc[i, 'inapp_purchase'].split(',')\n",
    "        df1.loc[i, 'inapp_purchase'] = 0\n",
    "        # Calculate mean of values and assign back to dataframe\n",
    "        c = 0\n",
    "        for j in inapp:\n",
    "            df1.loc[i, 'inapp_purchase'] = float(df1.loc[i, 'inapp_purchase']) + float(j)\n",
    "            c += 1\n",
    "        df1.loc[i, 'inapp_purchase'] = df1.loc[i, 'inapp_purchase']/c\n",
    "\n",
    "# Convert to numeric variable\n",
    "df1['inapp_purchase'] = pd.to_numeric(df1['inapp_purchase'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Remove '+' in 'age_rating' and convert to integer\n",
    "for i in range(len(df1)):\n",
    "    for j in (4,9,12,17):\n",
    "        if ('{}+'.format(j)) == str(df1.loc[i, 'age_rating']):\n",
    "            df1.loc[i, 'age_rating'] = j\n",
    "\n",
    "# Convert to numeric variable\n",
    "df1['age_rating'] = pd.to_numeric(df1['age_rating'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Action',\n",
       " 'Adventure',\n",
       " 'Animals & Nature',\n",
       " 'Art',\n",
       " 'Board',\n",
       " 'Books',\n",
       " 'Business',\n",
       " 'Card',\n",
       " 'Casino',\n",
       " 'Casual',\n",
       " 'Comics & Cartoons',\n",
       " 'Education',\n",
       " 'Emoji & Expressions',\n",
       " 'Entertainment',\n",
       " 'Family',\n",
       " 'Finance',\n",
       " 'Food & Drink',\n",
       " 'Games',\n",
       " 'Gaming',\n",
       " 'Health & Fitness',\n",
       " 'Kids & Family',\n",
       " 'Lifestyle',\n",
       " 'Magazines & Newspapers',\n",
       " 'Medical',\n",
       " 'Music',\n",
       " 'Navigation',\n",
       " 'News',\n",
       " 'People',\n",
       " 'Photo & Video',\n",
       " 'Places & Objects',\n",
       " 'Productivity',\n",
       " 'Puzzle',\n",
       " 'Racing',\n",
       " 'Reference',\n",
       " 'Role Playing',\n",
       " 'Shopping',\n",
       " 'Simulation',\n",
       " 'Social Networking',\n",
       " 'Sports',\n",
       " 'Sports & Activities',\n",
       " 'Stickers',\n",
       " 'Strategy',\n",
       " 'Travel',\n",
       " 'Trivia',\n",
       " 'Utilities',\n",
       " 'Weather',\n",
       " 'Word',\n",
       " 'Books',\n",
       " 'Business',\n",
       " 'Education',\n",
       " 'Entertainment',\n",
       " 'Finance',\n",
       " 'Food & Drink',\n",
       " 'Games',\n",
       " 'Health & Fitness',\n",
       " 'Lifestyle',\n",
       " 'Medical',\n",
       " 'Music',\n",
       " 'Navigation',\n",
       " 'News',\n",
       " 'Productivity',\n",
       " 'Reference',\n",
       " 'Shopping',\n",
       " 'Social Networking',\n",
       " 'Sports',\n",
       " 'Stickers',\n",
       " 'Travel',\n",
       " 'Utilities']"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Convert 'genre' to dummy variables\n",
    "genre = np.unique(list).tolist()\n",
    "\n",
    "# Remove space before some genres\n",
    "genres = []\n",
    "for i in range(len(genre)):\n",
    "    genres.append(genre[i].strip())\n",
    "genres"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Convert 'genre' to dummy variables\n",
    "# As there are multiple elements in one cell, I convert 'genre' to dummy variables manually\n",
    "# Create columns for dummy variables and assign 0s\n",
    "for g in genres:\n",
    "    df1['genre_{}'.format(g)] = 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>ave_rating</th>\n",
       "      <th>rating_count</th>\n",
       "      <th>price</th>\n",
       "      <th>inapp_purchase</th>\n",
       "      <th>age_rating</th>\n",
       "      <th>size</th>\n",
       "      <th>genre_Action</th>\n",
       "      <th>genre_Adventure</th>\n",
       "      <th>genre_Animals &amp; Nature</th>\n",
       "      <th>genre_Art</th>\n",
       "      <th>...</th>\n",
       "      <th>genre_Social Networking</th>\n",
       "      <th>genre_Sports</th>\n",
       "      <th>genre_Sports &amp; Activities</th>\n",
       "      <th>genre_Stickers</th>\n",
       "      <th>genre_Strategy</th>\n",
       "      <th>genre_Travel</th>\n",
       "      <th>genre_Trivia</th>\n",
       "      <th>genre_Utilities</th>\n",
       "      <th>genre_Weather</th>\n",
       "      <th>genre_Word</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>4.0</td>\n",
       "      <td>3553.0</td>\n",
       "      <td>2.99</td>\n",
       "      <td>0.0</td>\n",
       "      <td>4</td>\n",
       "      <td>15853568.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>3.5</td>\n",
       "      <td>284.0</td>\n",
       "      <td>1.99</td>\n",
       "      <td>0.0</td>\n",
       "      <td>4</td>\n",
       "      <td>12328960.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3.0</td>\n",
       "      <td>8376.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.0</td>\n",
       "      <td>4</td>\n",
       "      <td>674816.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3.5</td>\n",
       "      <td>190394.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.0</td>\n",
       "      <td>4</td>\n",
       "      <td>21552128.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>3.5</td>\n",
       "      <td>28.0</td>\n",
       "      <td>2.99</td>\n",
       "      <td>0.0</td>\n",
       "      <td>4</td>\n",
       "      <td>34689024.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7556</th>\n",
       "      <td>3.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.0</td>\n",
       "      <td>12</td>\n",
       "      <td>151308288.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7557</th>\n",
       "      <td>5.0</td>\n",
       "      <td>30.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.0</td>\n",
       "      <td>4</td>\n",
       "      <td>79646720.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7558</th>\n",
       "      <td>5.0</td>\n",
       "      <td>51.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.0</td>\n",
       "      <td>9</td>\n",
       "      <td>125348864.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7559</th>\n",
       "      <td>5.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.0</td>\n",
       "      <td>4</td>\n",
       "      <td>128687104.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7560</th>\n",
       "      <td>5.0</td>\n",
       "      <td>33.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.0</td>\n",
       "      <td>4</td>\n",
       "      <td>8845312.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>7561 rows × 53 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      ave_rating  rating_count  price  inapp_purchase  age_rating  \\\n",
       "0            4.0        3553.0   2.99             0.0           4   \n",
       "1            3.5         284.0   1.99             0.0           4   \n",
       "2            3.0        8376.0   0.00             0.0           4   \n",
       "3            3.5      190394.0   0.00             0.0           4   \n",
       "4            3.5          28.0   2.99             0.0           4   \n",
       "...          ...           ...    ...             ...         ...   \n",
       "7556         3.0           6.0   0.00             0.0          12   \n",
       "7557         5.0          30.0   0.00             0.0           4   \n",
       "7558         5.0          51.0   0.00             0.0           9   \n",
       "7559         5.0           5.0   0.00             0.0           4   \n",
       "7560         5.0          33.0   0.00             0.0           4   \n",
       "\n",
       "             size  genre_Action  genre_Adventure  genre_Animals & Nature  \\\n",
       "0      15853568.0             0                0                       0   \n",
       "1      12328960.0             0                0                       0   \n",
       "2        674816.0             0                0                       0   \n",
       "3      21552128.0             0                0                       0   \n",
       "4      34689024.0             0                0                       0   \n",
       "...           ...           ...              ...                     ...   \n",
       "7556  151308288.0             0                0                       0   \n",
       "7557   79646720.0             1                0                       0   \n",
       "7558  125348864.0             0                0                       0   \n",
       "7559  128687104.0             0                0                       0   \n",
       "7560    8845312.0             0                0                       0   \n",
       "\n",
       "      genre_Art  ...  genre_Social Networking  genre_Sports  \\\n",
       "0             0  ...                        0             0   \n",
       "1             0  ...                        0             0   \n",
       "2             0  ...                        0             0   \n",
       "3             0  ...                        0             0   \n",
       "4             0  ...                        0             0   \n",
       "...         ...  ...                      ...           ...   \n",
       "7556          0  ...                        0             0   \n",
       "7557          0  ...                        0             0   \n",
       "7558          0  ...                        0             0   \n",
       "7559          0  ...                        0             0   \n",
       "7560          0  ...                        0             0   \n",
       "\n",
       "      genre_Sports & Activities  genre_Stickers  genre_Strategy  genre_Travel  \\\n",
       "0                             0               0               1             0   \n",
       "1                             0               0               1             0   \n",
       "2                             0               0               1             0   \n",
       "3                             0               0               1             0   \n",
       "4                             0               0               1             0   \n",
       "...                         ...             ...             ...           ...   \n",
       "7556                          0               0               1             0   \n",
       "7557                          0               0               1             0   \n",
       "7558                          0               0               1             0   \n",
       "7559                          0               0               1             0   \n",
       "7560                          0               0               1             0   \n",
       "\n",
       "      genre_Trivia  genre_Utilities  genre_Weather  genre_Word  \n",
       "0                0                0              0           0  \n",
       "1                0                0              0           0  \n",
       "2                0                0              0           0  \n",
       "3                0                0              0           0  \n",
       "4                0                0              0           0  \n",
       "...            ...              ...            ...         ...  \n",
       "7556             0                0              0           0  \n",
       "7557             0                0              0           0  \n",
       "7558             0                0              0           0  \n",
       "7559             0                0              0           0  \n",
       "7560             0                1              0           0  \n",
       "\n",
       "[7561 rows x 53 columns]"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Change cells to 1 if corresponding genres appear in same row\n",
    "for i in genres:\n",
    "    for j in range(len(df1)):\n",
    "        if i in df1.loc[j, 'genre']:\n",
    "            df1.loc[j, 'genre_{}'.format(i)] = 1\n",
    "\n",
    "# Drop the original 'genre' column\n",
    "df1.drop(['genre'], axis = 1, inplace = True)\n",
    "df1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 4. Predictive Modelling"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4.1 Split dataset into train/test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "\n",
    "# Split the datasets into training and testing data\n",
    "df_x = df1.drop(['ave_rating'], axis = 1)\n",
    "X = df_x\n",
    "y = df1['ave_rating']\n",
    "\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4.2 Create pipelines"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a pipeline of imputing empty values, creating polynomial features and feature scaling\n",
    "from sklearn.compose import ColumnTransformer\n",
    "from sklearn.impute import SimpleImputer\n",
    "from sklearn.preprocessing import PolynomialFeatures\n",
    "from sklearn.pipeline import Pipeline\n",
    "from sklearn.preprocessing import MinMaxScaler\n",
    "\n",
    "from sklearn.linear_model import LinearRegression\n",
    "from sklearn.ensemble import RandomForestRegressor\n",
    "from sklearn.ensemble import GradientBoostingRegressor\n",
    "\n",
    "from sklearn.model_selection import GridSearchCV\n",
    "from sklearn.model_selection import RandomizedSearchCV\n",
    "\n",
    "# Create a transformer\n",
    "transformer = ColumnTransformer([(\"norm1\", SimpleImputer(missing_values = np.nan, strategy = 'mean'),[2]),\n",
    "                                 ('poly', PolynomialFeatures(3),[2,3])])\n",
    "\n",
    "# Create pipelines of three different regression algorithms\n",
    "# Linear Regression pipeline\n",
    "ln_model = Pipeline(steps=([('transformer', transformer),\n",
    "                            ('scaler',MinMaxScaler()),\n",
    "                            ('LR1', LinearRegression())]))\n",
    "\n",
    "# Random Forest pipeline\n",
    "rf_model = Pipeline(steps=([('transformer', transformer),\n",
    "                            ('scaler',MinMaxScaler()),\n",
    "                            ('LR2', RandomForestRegressor())]))\n",
    "\n",
    "# Gradient Boosting pipeline\n",
    "gb_model = Pipeline(steps=([('transformer', transformer),\n",
    "                            ('scaler',MinMaxScaler()),\n",
    "                            ('LR3', GradientBoostingRegressor())]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Verify the number of missing value\n",
    "df1.isnull().sum().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4.3 Model fitting & Making prediction"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import GridSearchCV\n",
    "from sklearn.model_selection import RandomizedSearchCV\n",
    "from sklearn import metrics\n",
    "\n",
    "# Create an empty dataframe for RMSE scores\n",
    "df_rmse = pd.DataFrame(columns = ['model', 'RMSE'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Define a function to evaluate and record model accuracy\n",
    "def rmse_score(pred, model_name):\n",
    "    \"\"\"Print out RMSE score of a model and add the score to dataframe\"\"\"\n",
    "    rmse = metrics.mean_squared_error(y_test, pred)\n",
    "    to_append = [model_name, rmse]\n",
    "    df_rmse.loc[len(df_rmse)] = to_append\n",
    "    return ('RMSE for this model is: {}'.format(rmse))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4.3.1 Linear Regression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Have a look at the parameters\n",
    "LinearRegression()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Fit linear model into the training data and make prediction\n",
    "ln = ln_model.fit(X_train,y_train)\n",
    "y_pred1 = ln_model.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'RMSE for this model is: 0.5465356666411711'"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Call the rmse_score function to get rmse score\n",
    "rmse_score(y_pred1, 'Linear')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4.3.2  Random Forest"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "RandomForestRegressor(bootstrap=True, ccp_alpha=0.0, criterion='mse',\n",
       "                      max_depth=None, max_features='auto', max_leaf_nodes=None,\n",
       "                      max_samples=None, min_impurity_decrease=0.0,\n",
       "                      min_impurity_split=None, min_samples_leaf=1,\n",
       "                      min_samples_split=2, min_weight_fraction_leaf=0.0,\n",
       "                      n_estimators=100, n_jobs=None, oob_score=False,\n",
       "                      random_state=None, verbose=0, warm_start=False)"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Have a look at the parameters\n",
    "RandomForestRegressor()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Fit Random Forest model into the training data and make prediction\n",
    "rf = rf_model.fit(X_train,y_train)\n",
    "y_pred2 = rf_model.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'RMSE for this model is: 0.5733858329265725'"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Call the rmse_score function to get rmse score\n",
    "rmse_score(y_pred2, 'RandomForest')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Grid Search"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Fitting 3 folds for each of 45 candidates, totalling 135 fits\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[Parallel(n_jobs=-1)]: Using backend LokyBackend with 8 concurrent workers.\n",
      "[Parallel(n_jobs=-1)]: Done  25 tasks      | elapsed:    3.8s\n",
      "[Parallel(n_jobs=-1)]: Done 135 out of 135 | elapsed:   23.2s finished\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "Pipeline(memory=None,\n",
       "         steps=[('transformer',\n",
       "                 ColumnTransformer(n_jobs=None, remainder='drop',\n",
       "                                   sparse_threshold=0.3,\n",
       "                                   transformer_weights=None,\n",
       "                                   transformers=[('norm1',\n",
       "                                                  SimpleImputer(add_indicator=False,\n",
       "                                                                copy=True,\n",
       "                                                                fill_value=None,\n",
       "                                                                missing_values=nan,\n",
       "                                                                strategy='mean',\n",
       "                                                                verbose=0),\n",
       "                                                  [2]),\n",
       "                                                 ('poly',\n",
       "                                                  PolynomialFeatures(degree=3,\n",
       "                                                                     include_bias=True,\n",
       "                                                                     interaction_only=False,\n",
       "                                                                     ord...\n",
       "                 RandomForestRegressor(bootstrap=True, ccp_alpha=0.0,\n",
       "                                       criterion='mse', max_depth=None,\n",
       "                                       max_features='auto', max_leaf_nodes=None,\n",
       "                                       max_samples=None,\n",
       "                                       min_impurity_decrease=0.0,\n",
       "                                       min_impurity_split=None,\n",
       "                                       min_samples_leaf=3, min_samples_split=3,\n",
       "                                       min_weight_fraction_leaf=0.0,\n",
       "                                       n_estimators=300, n_jobs=None,\n",
       "                                       oob_score=False, random_state=None,\n",
       "                                       verbose=0, warm_start=False))],\n",
       "         verbose=False)"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Try Grid Search for hyperparameter tuning\n",
    "\n",
    "# Set up a dictionary with hyperparameters to test\n",
    "param_grid = {\n",
    "               'LR2__min_samples_split': [1, 2, 3],\n",
    "               'LR2__min_samples_leaf': [1, 2, 3],\n",
    "               'LR2__n_estimators': [20, 50, 100, 200, 300]\n",
    "}\n",
    "\n",
    "# Initialize Grid Rearch and fit data into the model\n",
    "grid_search = GridSearchCV(estimator = rf_model, param_grid = param_grid, cv = 3, n_jobs = -1, verbose = 2)\n",
    "grid_search.fit(X_train, y_train)\n",
    "\n",
    "# Check out the parameters that return the highest accuracy\n",
    "best_grid = grid_search.best_estimator_\n",
    "best_grid"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'RMSE for this model is: 0.5578576767244616'"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Make prediction\n",
    "y_pred3 = best_grid.predict(X_test)\n",
    "\n",
    "# Call the rmse_score function to get rmse score\n",
    "rmse_score(y_pred3, 'RandomForest_grid')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Randomized Search"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Fitting 3 folds for each of 10 candidates, totalling 30 fits\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[Parallel(n_jobs=-1)]: Using backend LokyBackend with 8 concurrent workers.\n",
      "[Parallel(n_jobs=-1)]: Done  30 out of  30 | elapsed:    9.2s finished\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "Pipeline(memory=None,\n",
       "         steps=[('transformer',\n",
       "                 ColumnTransformer(n_jobs=None, remainder='drop',\n",
       "                                   sparse_threshold=0.3,\n",
       "                                   transformer_weights=None,\n",
       "                                   transformers=[('norm1',\n",
       "                                                  SimpleImputer(add_indicator=False,\n",
       "                                                                copy=True,\n",
       "                                                                fill_value=None,\n",
       "                                                                missing_values=nan,\n",
       "                                                                strategy='mean',\n",
       "                                                                verbose=0),\n",
       "                                                  [2]),\n",
       "                                                 ('poly',\n",
       "                                                  PolynomialFeatures(degree=3,\n",
       "                                                                     include_bias=True,\n",
       "                                                                     interaction_only=False,\n",
       "                                                                     ord...\n",
       "                 RandomForestRegressor(bootstrap=True, ccp_alpha=0.0,\n",
       "                                       criterion='mse', max_depth=None,\n",
       "                                       max_features='auto', max_leaf_nodes=None,\n",
       "                                       max_samples=None,\n",
       "                                       min_impurity_decrease=0.0,\n",
       "                                       min_impurity_split=None,\n",
       "                                       min_samples_leaf=10, min_samples_split=4,\n",
       "                                       min_weight_fraction_leaf=0.0,\n",
       "                                       n_estimators=180, n_jobs=None,\n",
       "                                       oob_score=False, random_state=None,\n",
       "                                       verbose=0, warm_start=False))],\n",
       "         verbose=False)"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Try Randomized Search for hyperparameter tuning\n",
    "\n",
    "# Set up a dictionary with hyperparameters to test\n",
    "param_dist = {\n",
    "               'LR2__min_samples_split': np.linspace(1, 10, 8, dtype = int),\n",
    "               'LR2__min_samples_leaf': np.linspace(1, 10, 8, dtype = int),\n",
    "               'LR2__n_estimators': np.linspace(20, 500, 10, dtype = int)}\n",
    "\n",
    "# Initialize Randomized Rearch and fit data into the model\n",
    "random_search = RandomizedSearchCV(estimator = rf_model, param_distributions = param_dist, \n",
    "                                   cv = 3, n_jobs = -1, verbose = 2,n_iter = 10)\n",
    "random_search.fit(X_train, y_train)\n",
    "\n",
    "# Check out the parameters that return the highest accuracy\n",
    "best_random= random_search.best_estimator_\n",
    "best_random"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'RMSE for this model is: 0.5452759117068344'"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Make prediction\n",
    "y_pred4 = best_random.predict(X_test)\n",
    "\n",
    "# Call the rmse_score function to get rmse score\n",
    "rmse_score(y_pred4, 'RandomForest_randomized')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4.3.3 Gradient Boosting Regression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "GradientBoostingRegressor(alpha=0.9, ccp_alpha=0.0, criterion='friedman_mse',\n",
       "                          init=None, learning_rate=0.1, loss='ls', max_depth=3,\n",
       "                          max_features=None, max_leaf_nodes=None,\n",
       "                          min_impurity_decrease=0.0, min_impurity_split=None,\n",
       "                          min_samples_leaf=1, min_samples_split=2,\n",
       "                          min_weight_fraction_leaf=0.0, n_estimators=100,\n",
       "                          n_iter_no_change=None, presort='deprecated',\n",
       "                          random_state=None, subsample=1.0, tol=0.0001,\n",
       "                          validation_fraction=0.1, verbose=0, warm_start=False)"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Have a look at the parameters\n",
    "GradientBoostingRegressor()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Fit Gradient Boosting model into the training data and make prediction\n",
    "gb = gb_model.fit(X_train,y_train)\n",
    "y_pred5 = gb_model.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'RMSE for this model is: 0.5449212700477173'"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Make prediction\n",
    "y_pred5 = gb_model.predict(X_test)\n",
    "\n",
    "# Call the rmse_score function to get rmse score\n",
    "rmse_score(y_pred5, 'GradientBoosting')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Grid Search"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Fitting 3 folds for each of 300 candidates, totalling 900 fits\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[Parallel(n_jobs=-1)]: Using backend LokyBackend with 8 concurrent workers.\n",
      "[Parallel(n_jobs=-1)]: Done  34 tasks      | elapsed:    1.5s\n",
      "[Parallel(n_jobs=-1)]: Done 194 tasks      | elapsed:   15.0s\n",
      "[Parallel(n_jobs=-1)]: Done 397 tasks      | elapsed:   33.8s\n",
      "[Parallel(n_jobs=-1)]: Done 680 tasks      | elapsed:   58.3s\n",
      "[Parallel(n_jobs=-1)]: Done 900 out of 900 | elapsed:  1.4min finished\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "Pipeline(memory=None,\n",
       "         steps=[('transformer',\n",
       "                 ColumnTransformer(n_jobs=None, remainder='drop',\n",
       "                                   sparse_threshold=0.3,\n",
       "                                   transformer_weights=None,\n",
       "                                   transformers=[('norm1',\n",
       "                                                  SimpleImputer(add_indicator=False,\n",
       "                                                                copy=True,\n",
       "                                                                fill_value=None,\n",
       "                                                                missing_values=nan,\n",
       "                                                                strategy='mean',\n",
       "                                                                verbose=0),\n",
       "                                                  [2]),\n",
       "                                                 ('poly',\n",
       "                                                  PolynomialFeatures(degree=3,\n",
       "                                                                     include_bias=True,\n",
       "                                                                     interaction_only=False,\n",
       "                                                                     ord...\n",
       "                                           learning_rate=0.1, loss='ls',\n",
       "                                           max_depth=2, max_features=None,\n",
       "                                           max_leaf_nodes=None,\n",
       "                                           min_impurity_decrease=0.0,\n",
       "                                           min_impurity_split=None,\n",
       "                                           min_samples_leaf=1,\n",
       "                                           min_samples_split=3,\n",
       "                                           min_weight_fraction_leaf=0.0,\n",
       "                                           n_estimators=50,\n",
       "                                           n_iter_no_change=None,\n",
       "                                           presort='deprecated',\n",
       "                                           random_state=None, subsample=1.0,\n",
       "                                           tol=0.0001, validation_fraction=0.1,\n",
       "                                           verbose=0, warm_start=False))],\n",
       "         verbose=False)"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Try Grid Search for hyperparameter tuning\n",
    "\n",
    "# Set up a dictionary with hyperparameters to test\n",
    "param_grid = {\n",
    "               'LR3__max_depth': [2, 3, 4, 5],\n",
    "               'LR3__learning_rate': [0.03, 0.05, 0.1, 0.15, 0.2],\n",
    "               'LR3__n_estimators': [30, 50, 100, 200, 400],\n",
    "               'LR3__min_samples_split': [1, 2, 3]\n",
    "}\n",
    "\n",
    "# Initialize Grid Rearch and fit data into the model\n",
    "grid_search = GridSearchCV(estimator = gb_model, param_grid = param_grid, cv = 3, n_jobs = -1, verbose = 2)\n",
    "grid_search.fit(X_train, y_train)\n",
    "\n",
    "# Check out the parameters that return the highest accuracy\n",
    "best_grid = grid_search.best_estimator_\n",
    "best_grid"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'RMSE for this model is: 0.5426091040225021'"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Make prediction\n",
    "y_pred6 = best_grid.predict(X_test)\n",
    "\n",
    "# Call the rmse_score function to get rmse score\n",
    "rmse_score(y_pred6, 'GradientBoosting_grid')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Randomized Search"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[Parallel(n_jobs=-1)]: Using backend LokyBackend with 8 concurrent workers.\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Fitting 3 folds for each of 10 candidates, totalling 30 fits\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[Parallel(n_jobs=-1)]: Done  30 out of  30 | elapsed:    7.9s finished\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "Pipeline(memory=None,\n",
       "         steps=[('transformer',\n",
       "                 ColumnTransformer(n_jobs=None, remainder='drop',\n",
       "                                   sparse_threshold=0.3,\n",
       "                                   transformer_weights=None,\n",
       "                                   transformers=[('norm1',\n",
       "                                                  SimpleImputer(add_indicator=False,\n",
       "                                                                copy=True,\n",
       "                                                                fill_value=None,\n",
       "                                                                missing_values=nan,\n",
       "                                                                strategy='mean',\n",
       "                                                                verbose=0),\n",
       "                                                  [2]),\n",
       "                                                 ('poly',\n",
       "                                                  PolynomialFeatures(degree=3,\n",
       "                                                                     include_bias=True,\n",
       "                                                                     interaction_only=False,\n",
       "                                                                     ord...\n",
       "                                           learning_rate=0.42428571428571427,\n",
       "                                           loss='ls', max_depth=1,\n",
       "                                           max_features=None,\n",
       "                                           max_leaf_nodes=None,\n",
       "                                           min_impurity_decrease=0.0,\n",
       "                                           min_impurity_split=None,\n",
       "                                           min_samples_leaf=1,\n",
       "                                           min_samples_split=5,\n",
       "                                           min_weight_fraction_leaf=0.0,\n",
       "                                           n_estimators=437,\n",
       "                                           n_iter_no_change=None,\n",
       "                                           presort='deprecated',\n",
       "                                           random_state=None, subsample=1.0,\n",
       "                                           tol=0.0001, validation_fraction=0.1,\n",
       "                                           verbose=0, warm_start=False))],\n",
       "         verbose=False)"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Try Randomized Search for hyperparameter tuning\n",
    "\n",
    "# Set up a dictionary with hyperparameters to test\n",
    "param_dist = {\n",
    "               'LR3__max_depth': np.linspace(1, 10, 5, dtype = int),\n",
    "               'LR3__learning_rate': np.linspace(0.03, 0.95, 8, dtype = float),\n",
    "               'LR3__n_estimators': np.linspace(30, 600, 8, dtype = int),\n",
    "               'LR3__min_samples_split': np.linspace(1, 5, 3, dtype = int)}\n",
    "\n",
    "# Initialize Randomized Rearch and fit data into the model\n",
    "random_search = RandomizedSearchCV(estimator = gb_model, param_distributions = param_dist, \n",
    "                                   cv = 3, n_jobs = -1, verbose = 2,n_iter = 10)\n",
    "random_search.fit(X_train, y_train)\n",
    "\n",
    "# Check out the parameters that return the highest accuracy\n",
    "best_random= random_search.best_estimator_\n",
    "best_random"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'RMSE for this model is: 0.5421493089772156'"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Make prediction\n",
    "y_pred7 = best_random.predict(X_test)\n",
    "\n",
    "# Call the rmse_score function to get rmse score\n",
    "rmse_score(y_pred7, 'GradientBoosting_randomized')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 5. Model Comparasion & Selection"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>model</th>\n",
       "      <th>RMSE</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>GradientBoosting_randomized</td>\n",
       "      <td>0.542149</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>GradientBoosting_grid</td>\n",
       "      <td>0.542609</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>GradientBoosting</td>\n",
       "      <td>0.544921</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>RandomForest_randomized</td>\n",
       "      <td>0.545276</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Linear</td>\n",
       "      <td>0.546536</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>RandomForest_grid</td>\n",
       "      <td>0.557858</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>RandomForest</td>\n",
       "      <td>0.573386</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                         model      RMSE\n",
       "0  GradientBoosting_randomized  0.542149\n",
       "1        GradientBoosting_grid  0.542609\n",
       "2             GradientBoosting  0.544921\n",
       "3      RandomForest_randomized  0.545276\n",
       "4                       Linear  0.546536\n",
       "5            RandomForest_grid  0.557858\n",
       "6                 RandomForest  0.573386"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Sort df_rmse in acsending order and display the dataframe\n",
    "df_rmse.sort_values(['RMSE'], ascending = True, inplace = True)\n",
    "df_rmse.reset_index(inplace = True, drop = True)\n",
    "display(df_rmse)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Plot the dataframe in a line chart\n",
    "df_rmse.plot(x = 'model',\n",
    "             y = 'RMSE',\n",
    "             title = 'RMSE of models')\n",
    "plt.xticks(range(len(df_rmse['model'])),\n",
    "           df_rmse['model'],\n",
    "           fontsize = 9,\n",
    "           rotation = 35)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 6. Conclusion"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As we can see from the above results, although the differences in RMSE scores are not obvious, Gradient Boosting Methods have best predictions with lowest RMSE scores. Linear Regression performs better than basic Random Forest, which is beyond my expectations. The overall accuracy of models on this dataset is: Gradient Boosting > Linear > Random Forest.\n",
    "\n",
    "As for Hyperparameter Tuning methods, I tried Grid Search and Randomized Search. The result suggests that Randomized Research performs better on both Gradient Boosting and Random Forest model (Linear model does not need a hyperparameter tuning). Thus, the effectiveness of Hyperparameter Tuning methods here is: Randomized Research > Grid Research. This result could be influenced by the parameters I choose. \n",
    "\n",
    "Thus, I choose the Gradient Boosting Model with Randomized Research hyperparameter tuning method as my final model to make prediction. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>pred</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>4.212687</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>4.227069</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>4.140384</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4.188696</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4.055876</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1508</th>\n",
       "      <td>4.252918</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1509</th>\n",
       "      <td>4.048134</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1510</th>\n",
       "      <td>4.161111</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1511</th>\n",
       "      <td>3.911187</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1512</th>\n",
       "      <td>3.947735</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1513 rows × 1 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "          pred\n",
       "0     4.212687\n",
       "1     4.227069\n",
       "2     4.140384\n",
       "3     4.188696\n",
       "4     4.055876\n",
       "...        ...\n",
       "1508  4.252918\n",
       "1509  4.048134\n",
       "1510  4.161111\n",
       "1511  3.911187\n",
       "1512  3.947735\n",
       "\n",
       "[1513 rows x 1 columns]"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Create a dataframe of the final testing prediction\n",
    "df_test_result = pd.DataFrame(y_pred7, columns = ['pred'])\n",
    "# Export the dataframe to a csv file\n",
    "df_test_result.to_csv('game_pred.csv', index = False)\n",
    "df_test_result"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 7. Business applications & limitations"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This program can be used to predict the average user ratings of mobile stratrgy games, and provide some useful instructions to mobile strategy game developers on the features of a more popular mobile game. App developers can use this model to predict whether their product would be rated a higher or lower score (only for reference).\n",
    "\n",
    "However, the model has a lot of limitations. Firstly, the largest limitaiton is from the dataset itself. There are only limited number of features that can be used to train the model, many of which do not have strong connections to the target variable. This implies that its reference value is very limited. Besides, I dropped all the columns with descriptive words since I did not intend to include any text mining technique in my model. What I did is to convert 'genres' into dummy variables so that the model can be more persuasive and meaningful. If the 'Name', 'Subtitle' and 'Description' features are explored using text mining, the result might be much better. Since text mining is not covered in this course, I may try this in the future. Moreover, I only tried 3 different regression models and used limited number of hyperparameters in order to control the total runtime. I think the results could be slightly better if I have more time to try different parameter combos and models. \n",
    "\n",
    "Thank you!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "# pip freeze > requirement.txt"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.7 (tensorflow)",
   "language": "python",
   "name": "tensorflow"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
