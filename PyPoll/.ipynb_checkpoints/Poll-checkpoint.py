{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "file = \"election.csv\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [],
   "source": [
    "election = pd.read_csv(file)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
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
       "      <th>Voter ID</th>\n",
       "      <th>County</th>\n",
       "      <th>Candidate</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>12864552</td>\n",
       "      <td>Marsh</td>\n",
       "      <td>Khan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>17444633</td>\n",
       "      <td>Marsh</td>\n",
       "      <td>Correy</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>19330107</td>\n",
       "      <td>Marsh</td>\n",
       "      <td>Khan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>19865775</td>\n",
       "      <td>Queen</td>\n",
       "      <td>Khan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>11927875</td>\n",
       "      <td>Marsh</td>\n",
       "      <td>Khan</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Voter ID County Candidate\n",
       "0  12864552  Marsh      Khan\n",
       "1  17444633  Marsh    Correy\n",
       "2  19330107  Marsh      Khan\n",
       "3  19865775  Queen      Khan\n",
       "4  11927875  Marsh      Khan"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "election.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3521001\n"
     ]
    }
   ],
   "source": [
    "#counts of all unique voter ID\n",
    "total_voters=(int(election[\"Voter ID\"].nunique()))\n",
    "print(total_voters)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Khan' 'Correy' 'Li' \"O'Tooley\"]\n",
      "2218231\n"
     ]
    }
   ],
   "source": [
    "# Array of all candidates\n",
    "candidates = election[\"Candidate\"].unique()\n",
    "print(candidates)\n",
    "print(len(election[election[\"Candidate\"] == \"Khan\"]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [],
   "source": [
    "#   Election Results\n",
    "#   -------------------------\n",
    "#   Total Votes: 3521001\n",
    "#   -------------------------\n",
    "#   Khan: 63.000% (2218231)\n",
    "#   Correy: 20.000% (704200)\n",
    "#   Li: 14.000% (492940)\n",
    "#   O'Tooley: 3.000% (105630)\n",
    "#   -------------------------\n",
    "#   Winner: Khan\n",
    "#   -------------------------\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2218231, 704200, 492940, 105630]\n"
     ]
    }
   ],
   "source": [
    "#created a new blank list\n",
    "candidate_votes = []\n",
    "\n",
    "#looped through the candidates to add their total votes in the list \"candidate_votes\"\n",
    "for i in range(len(candidates)):\n",
    "    candidate_votes.append(len(election[election[\"Candidate\"] == str(candidates[i])]))\n",
    "    \n",
    "print(candidate_votes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['63.000', '20.000', '14.000', '3.000']\n"
     ]
    }
   ],
   "source": [
    "percentlist = []\n",
    "for k in range(len(candidate_votes)):\n",
    "    percentlist.append(\"{0:.3f}\".format(candidate_votes[k]*100/total_voters))\n",
    "    \n",
    "print(percentlist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 181,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Khan': '63.000', 'Correy': '20.000', 'Li': '14.000', \"O'Tooley\": '3.000'}\n"
     ]
    }
   ],
   "source": [
    "# Created dictionary with candidate's name and their votes percentage\n",
    "candidate_dict = dict(zip(candidates, percentlist))\n",
    "print(candidate_dict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 161,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Election Results\n",
      "-------------------------\n",
      "Total Votes:      3521001\n",
      "-------------------------\n",
      "Khan 63.000% (2218231)\n",
      "Correy 20.000% (704200)\n",
      "Li 14.000% (492940)\n",
      "O'Tooley 3.000% (105630)\n",
      "-------------------------\n"
     ]
    }
   ],
   "source": [
    "print(\"Election Results\")\n",
    "print((\"-\")*25)\n",
    "print(\"Total Votes:      \"+ str(total_voters))\n",
    "print((\"-\")*25)\n",
    "i = 0\n",
    "for key in candidate_dict:\n",
    "    print(key, candidate_dict[key]+\"% (\"+str(candidate_votes[i])+\")\")\n",
    "    i = i+1\n",
    "print((\"-\")*25)\n",
    "# print(\"Winner :   \")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 162,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2218231\n"
     ]
    }
   ],
   "source": [
    "print(max(candidate_votes))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
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
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
