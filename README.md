# statsbombpy <picture><source media="(prefers-color-scheme: dark)" srcset="https://github.com/statsbomb/logos/blob/main/HudlStatsbomb_Python_Dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://github.com/statsbomb/logos/blob/main/HudlStatsbomb_Python.svg"><img alt="StatsBombPython_Lock" src="https://github.com/statsbomb/logos/blob/main/HudlStatsbomb_Python.svg" align="right" height="40"></picture>

[![PyPI version](https://badge.fury.io/py/statsbombpy.svg?)](https://badge.fury.io/py/statsbombpy)

Brought to you by StatsBomb, this repository is a Python package that allows users to easily stream StatsBomb data into Python using your log in credentials for the API or free data from our GitHub page. **API access is for paying customers only**

**Support: [Hudl Support Form](https://support.hudl.com/s/contactsupport?language=en_US&Category=m0HVY000002iydd)**


## Installation Instructions

`pip install statsbombpy`


## Running the tests

`nose2 -v --pretty-assert`


## Configuration

### Authentication

#### Environment Variables
Authentication can be done by setting environment variables named `SB_USERNAME` and `SB_PASSWORD` to your login credentials.

#### Manual Calls
Alternatively, if you don't want to use environment variables, all functions accept an argument `creds` to pass your login credentials in the format `{"user": "", "passwd": ""}`

### Concurrency
You can specify how many of your computer's cores to use when running the `sb.competition_events()` and `sb.competition_frames()` functions by setting the environment variable `SB_CORES` to the number you want to use. Allowing statsbombpy to use more cores will speed up those functions.

If you don't have an environment variable set we will try to detect the number of cores in your system and use 2 less than that number. If we cannot detect the number of cores we set the number to 4.

## Open Data
StatsBomb's open data can be accessed without the need of authentication.

StatsBomb are committed to sharing new data and research publicly to enhance understanding of the game of Football. We want to actively encourage new research and analysis at all levels. Therefore we have made certain leagues of StatsBomb Data freely available for public use for research projects and genuine interest in football analytics.

StatsBomb are hoping that by making data freely available, we will extend the wider football analytics community and attract new talent to the industry. We would like to collect some basic personal information about users of our data. By [giving us your email address](https://statsbomb.com/resource-centre/), it means we will let you know when we make more data, tutorials and research available. We will store the information in accordance with our Privacy Policy and the GDPR.

#### Terms & Conditions
Whilst we are keen to share data and facilitate research, we also urge you to be responsible with the data. Please register your details on https://www.statsbomb.com/resource-centre and read our [User Agreement](doc/LICENSE.pdf) carefully.
By using this repository, you are agreeing to the user agreement. If you publish, share or distribute any research, analysis or insights based on this data, please state the data source as StatsBomb and use our logo.


## Usage

```
from statsbombpy import sb
```


### Competitions

```
sb.competitions()
```
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>competition_id</th>
      <th>season_id</th>
      <th>country_name</th>
      <th>competition_name</th>
      <th>competition_gender</th>
      <th>season_name</th>
      <th>match_updated</th>
      <th>match_available</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>9</td>
      <td>42</td>
      <td>Germany</td>
      <td>1. Bundesliga</td>
      <td>male</td>
      <td>2019/2020</td>
      <td>2019-12-29T07:47:45.981</td>
      <td>2019-12-29T07:47:45.981</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9</td>
      <td>4</td>
      <td>Germany</td>
      <td>1. Bundesliga</td>
      <td>male</td>
      <td>2018/2019</td>
      <td>2019-12-16T23:09:16.168756</td>
      <td>2019-12-16T23:09:16.168756</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9</td>
      <td>1</td>
      <td>Germany</td>
      <td>1. Bundesliga</td>
      <td>male</td>
      <td>2017/2018</td>
      <td>2019-12-16T23:09:16.168756</td>
      <td>2019-12-16T23:09:16.168756</td>
    </tr>
    <tr>
      <th>3</th>
      <td>78</td>
      <td>42</td>
      <td>Croatia</td>
      <td>1. HNL</td>
      <td>male</td>
      <td>2019/2020</td>
      <td>2020-01-02T10:35:49.065</td>
      <td>2020-01-02T10:35:49.065</td>
    </tr>
    <tr>
      <th>4</th>
      <td>10</td>
      <td>42</td>
      <td>Germany</td>
      <td>2. Bundesliga</td>
      <td>male</td>
      <td>2019/2020</td>
      <td>2019-12-27T00:36:37.498</td>
      <td>2019-12-27T00:36:37.498</td>
    </tr>
  </tbody>
</table>


### Matches

```
sb.matches(competition_id=9, season_id=42)
```
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>match_id</th>
      <th>match_date</th>
      <th>kick_off</th>
      <th>competition</th>
      <th>season</th>
      <th>home_team</th>
      <th>away_team</th>
      <th>home_score</th>
      <th>away_score</th>
      <th>match_status</th>
      <th>last_updated</th>
      <th>match_week</th>
      <th>competition_stage</th>
      <th>stadium</th>
      <th>referee</th>
      <th>home_managers</th>
      <th>away_managers</th>
      <th>data_version</th>
      <th>shot_fidelity_version</th>
      <th>xy_fidelity_version</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>303299</td>
      <td>2019-12-15</td>
      <td>18:00:00.000</td>
      <td>Germany - 1. Bundesliga</td>
      <td>2019/2020</td>
      <td>Schalke 04</td>
      <td>Eintracht Frankfurt</td>
      <td>1</td>
      <td>0</td>
      <td>available</td>
      <td>2019-12-17T09:50:17.558</td>
      <td>15</td>
      <td>Regular Season</td>
      <td>VELTINS-Arena</td>
      <td>F. Zwayer</td>
      <td>David Wagner</td>
      <td>Adi Hütter</td>
      <td>1.1.0</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>303223</td>
      <td>2019-09-01</td>
      <td>18:00:00.000</td>
      <td>Germany - 1. Bundesliga</td>
      <td>2019/2020</td>
      <td>Eintracht Frankfurt</td>
      <td>Fortuna Düsseldorf</td>
      <td>2</td>
      <td>1</td>
      <td>available</td>
      <td>2019-12-16T23:09:16.168756</td>
      <td>3</td>
      <td>Regular Season</td>
      <td>Commerzbank-Arena</td>
      <td>F. Willenborg</td>
      <td>Adi Hütter</td>
      <td>Friedhelm Funkel</td>      
      <td>1.1.0</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>303083</td>
      <td>2019-12-15</td>
      <td>15:30:00.000</td>
      <td>Germany - 1. Bundesliga</td>
      <td>2019/2020</td>
      <td>Wolfsburg</td>
      <td>Borussia Mönchengladbach</td>
      <td>2</td>
      <td>1</td>
      <td>available</td>
      <td>2019-12-17T15:52:17.843</td>
      <td>15</td>
      <td>Regular Season</td>
      <td>VOLKSWAGEN ARENA</td>
      <td>F. Brych</td>
      <td>Oliver Glasner</td>
      <td>Marco Rose</td>      
      <td>1.1.0</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>303266</td>
      <td>2019-12-14</td>
      <td>15:30:00.000</td>
      <td>Germany - 1. Bundesliga</td>
      <td>2019/2020</td>
      <td>Hertha Berlin</td>
      <td>Freiburg</td>
      <td>1</td>
      <td>0</td>
      <td>available</td>
      <td>2019-12-17T17:43:18.285</td>
      <td>15</td>
      <td>Regular Season</td>
      <td>Olympiastadion Berlin</td>
      <td>F. Willenborg</td>
      <td>Jürgen Klinsmann</td>
      <td>Christian Streich</td>      
      <td>1.1.0</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>303073</td>
      <td>2019-12-21</td>
      <td>15:30:00.000</td>
      <td>Germany - 1. Bundesliga</td>
      <td>2019/2020</td>
      <td>Bayern Munich</td>
      <td>Wolfsburg</td>
      <td>2</td>
      <td>0</td>
      <td>available</td>
      <td>2019-12-23T18:02:36.454</td>
      <td>17</td>
      <td>Regular Season</td>
      <td>Allianz Arena</td>
      <td>C. Dingert</td>
      <td>Hans-Dieter Flick</td>
      <td>Oliver Glasner </td>      
      <td>1.1.0</td>
      <td>2</td>
      <td>2</td>
    </tr>
  </tbody>
</table>


### Lineups

```
sb.lineups(match_id=303299)["Eintracht Frankfurt"]
```
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>player_id</th>
      <th>player_name</th>
      <th>player_nickname</th>
      <th>birth_date</th>
      <th>player_gender</th>
      <th>player_height</th>
      <th>player_weight</th>
      <th>jersey_number</th>
      <th>country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3204</td>
      <td>Almamy Touré</td>
      <td>None</td>
      <td>1996-04-28</td>
      <td>male</td>
      <td>182.0</td>
      <td>72.0</td>
      <td>18</td>
      <td>Mali</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5591</td>
      <td>Filip Kostić</td>
      <td>None</td>
      <td>1992-11-01</td>
      <td>male</td>
      <td>184.0</td>
      <td>82.0</td>
      <td>10</td>
      <td>Serbia</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7713</td>
      <td>Obite Evan N"Dicka</td>
      <td>Evan N'Dicka</td>
      <td>1999-08-20</td>
      <td>male</td>
      <td>190.0</td>
      <td>NaN</td>
      <td>2</td>
      <td>France</td>
    </tr>
    <tr>
      <th>3</th>
      <td>8307</td>
      <td>Martin Hinteregger</td>
      <td>None</td>
      <td>1992-09-07</td>
      <td>male</td>
      <td>184.0</td>
      <td>83.0</td>
      <td>13</td>
      <td>Austria</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8669</td>
      <td>Mijat Gaćinović</td>
      <td>None</td>
      <td>1995-02-08</td>
      <td>male</td>
      <td>175.0</td>
      <td>66.0</td>
      <td>11</td>
      <td>Serbia</td>
    </tr>
  </tbody>
</table>


### Events
The default settings for querying events return a single dataframe with all event types and event attributes.

```
events = sb.events(match_id=303299)
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ball_receipt_outcome</th>
      <th>ball_recovery_offensive</th>
      <th>ball_recovery_recovery_failure</th>
      <th>block_deflection</th>
      <th>carry_end_location</th>
      <th>clearance_aerial_won</th>
      <th>clearance_body_part</th>
      <th>clearance_head</th>
      <th>clearance_left_foot</th>
      <th>clearance_right_foot</th>
      <th>counterpress</th>
      <th>dribble_no_touch</th>
      <th>dribble_outcome</th>
      <th>dribble_overrun</th>
      <th>duel_outcome</th>
      <th>duel_type</th>
      <th>duration</th>
      <th>foul_committed_advantage</th>
      <th>foul_committed_card</th>
      <th>foul_won_advantage</th>
      <th>foul_won_defensive</th>
      <th>goalkeeper_body_part</th>
      <th>goalkeeper_end_location</th>
      <th>goalkeeper_outcome</th>
      <th>goalkeeper_position</th>
      <th>goalkeeper_technique</th>
      <th>goalkeeper_type</th>
      <th>id</th>
      <th>index</th>
      <th>injury_stoppage_in_chain</th>
      <th>interception_outcome</th>
      <th>location</th>
      <th>match_id</th>
      <th>minute</th>
      <th>off_camera</th>
      <th>out</th>
      <th>pass_aerial_won</th>
      <th>pass_angle</th>
      <th>pass_assisted_shot_id</th>
      <th>pass_body_part</th>
      <th>pass_cross</th>
      <th>pass_cut_back</th>
      <th>pass_deflected</th>
      <th>pass_end_location</th>
      <th>pass_goal_assist</th>
      <th>pass_height</th>
      <th>pass_length</th>
      <th>pass_outcome</th>
      <th>pass_outswinging</th>
      <th>pass_recipient</th>
      <th>pass_shot_assist</th>
      <th>pass_straight</th>
      <th>pass_switch</th>
      <th>pass_technique</th>
      <th>pass_through_ball</th>
      <th>pass_type</th>
      <th>pass_xclaim</th>
      <th>period</th>
      <th>play_pattern</th>
      <th>player</th>
      <th>position</th>
      <th>possession</th>
      <th>possession_team</th>
      <th>related_events</th>
      <th>second</th>
      <th>shot_aerial_won</th>
      <th>shot_body_part</th>
      <th>shot_end_location</th>
      <th>shot_first_time</th>
      <th>shot_freeze_frame</th>
      <th>shot_key_pass_id</th>
      <th>shot_one_on_one</th>
      <th>shot_outcome</th>
      <th>shot_statsbomb_xg</th>
      <th>shot_statsbomb_xg2</th>
      <th>shot_technique</th>
      <th>shot_type</th>
      <th>substitution_outcome</th>
      <th>substitution_replacement</th>
      <th>team</th>
      <th>timestamp</th>
      <th>type</th>
      <th>under_pressure</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>500</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3.498736</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>84828c06-41b5-44eb-aa92-1710bdb818ac</td>
      <td>1838</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>[50.1, 16.6]</td>
      <td>303299</td>
      <td>47</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.720095</td>
      <td>NaN</td>
      <td>Left Foot</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>[13.3, 33.1]</td>
      <td>NaN</td>
      <td>Ground Pass</td>
      <td>40.329765</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Frederik Rønnow</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2</td>
      <td>Regular Play</td>
      <td>Obite Evan N"Dicka</td>
      <td>Left Center Back</td>
      <td>103</td>
      <td>Eintracht Frankfurt</td>
      <td>[ae3094e3-faa3-4608-8284-d9b8cca77711, c1202f1c-0831-4e88-83b2-597f56f0c858]</td>
      <td>52</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Eintracht Frankfurt</td>
      <td>00:02:52.438</td>
      <td>Pass</td>
      <td>True</td>
    </tr>
    <tr>
      <th>501</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3.604236</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>9061cd20-513b-499f-b925-f1de5f241281</td>
      <td>1840</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>[13.3, 33.1]</td>
      <td>303299</td>
      <td>47</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>-0.153945</td>
      <td>NaN</td>
      <td>Right Foot</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>[77.1, 23.2]</td>
      <td>NaN</td>
      <td>High Pass</td>
      <td>64.563540</td>
      <td>Incomplete</td>
      <td>NaN</td>
      <td>Mijat Gaćinović</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2</td>
      <td>Regular Play</td>
      <td>Frederik Rønnow</td>
      <td>Goalkeeper</td>
      <td>103</td>
      <td>Eintracht Frankfurt</td>
      <td>[8e6495a7-782a-4f1a-845f-3ec50d761a1e, ff758a12-1ba6-4dd4-8b2c-7d39aa7aed97]</td>
      <td>55</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Eintracht Frankfurt</td>
      <td>00:02:55.937</td>
      <td>Pass</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>502</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.101999</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>8e6495a7-782a-4f1a-845f-3ec50d761a1e</td>
      <td>1842</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>[43.0, 56.9]</td>
      <td>303299</td>
      <td>47</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>-0.703110</td>
      <td>NaN</td>
      <td>Head</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>[64.0, 39.1]</td>
      <td>NaN</td>
      <td>High Pass</td>
      <td>27.528894</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Amine Harit</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Recovery</td>
      <td>NaN</td>
      <td>2</td>
      <td>Regular Play</td>
      <td>Ozan Muhammed Kabak</td>
      <td>Right Center Back</td>
      <td>104</td>
      <td>Schalke 04</td>
      <td>[9061cd20-513b-499f-b925-f1de5f241281, be6dfe7d-7596-4cc2-8cd9-8c17d064317e]</td>
      <td>59</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Schalke 04</td>
      <td>00:02:59.541</td>
      <td>Pass</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>503</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.187459</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>86431bc7-210a-4868-8e18-26ff38becefc</td>
      <td>1854</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>[65.9, 12.6]</td>
      <td>303299</td>
      <td>48</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>-0.730239</td>
      <td>NaN</td>
      <td>Right Foot</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>[74.5, 4.9]</td>
      <td>NaN</td>
      <td>Ground Pass</td>
      <td>11.543396</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Amine Harit</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2</td>
      <td>Regular Play</td>
      <td>Suat Serdar</td>
      <td>Left Defensive Midfield</td>
      <td>104</td>
      <td>Schalke 04</td>
      <td>[761b4e65-8f64-464c-8153-6a98465208ba]</td>
      <td>7</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Schalke 04</td>
      <td>00:03:07.689</td>
      <td>Pass</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>504</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.766628</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>6e58c713-622c-4246-8243-e4162e487a1c</td>
      <td>1858</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>[79.1, 10.5]</td>
      <td>303299</td>
      <td>48</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.254940</td>
      <td>NaN</td>
      <td>Right Foot</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>[84.1, 25.8]</td>
      <td>NaN</td>
      <td>Ground Pass</td>
      <td>16.096273</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Rabbi Matondo</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2</td>
      <td>Regular Play</td>
      <td>Amine Harit</td>
      <td>Center Attacking Midfield</td>
      <td>104</td>
      <td>Schalke 04</td>
      <td>[b1960a76-d3ae-4ef3-a2cd-47eca8c25e0a, dd1575c0-a408-4177-944d-7e86d2f79181]</td>
      <td>11</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Schalke 04</td>
      <td>00:03:11.719</td>
      <td>Pass</td>
      <td>True</td>
    </tr>
  </tbody>
</table>




It's also possible to get distinct dataframes for each event type and/or to have distinct event attributes on their own columns
```
sb.events(match_id=303299, split=True, flatten_attrs=False)["dribbles"]
```
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>index</th>
      <th>period</th>
      <th>timestamp</th>
      <th>minute</th>
      <th>second</th>
      <th>type</th>
      <th>possession</th>
      <th>possession_team</th>
      <th>play_pattern</th>
      <th>team</th>
      <th>player</th>
      <th>position</th>
      <th>location</th>
      <th>duration</th>
      <th>under_pressure</th>
      <th>related_events</th>
      <th>dribble</th>
      <th>match_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>b190c01f-ad24-468c-8241-f955b91d996c</td>
      <td>131</td>
      <td>1</td>
      <td>00:02:08.032</td>
      <td>2</td>
      <td>8</td>
      <td>Dribble</td>
      <td>4</td>
      <td>Schalke 04</td>
      <td>Regular Play</td>
      <td>Schalke 04</td>
      <td>Daniel Caligiuri</td>
      <td>Right Wing</td>
      <td>[110.2, 62.9]</td>
      <td>0.000000</td>
      <td>True</td>
      <td>[60f822df-5747-4787-b0f9-45bf5217eb8a]</td>
      <td>{'outcome': {'id': 8, 'name': 'Complete'}}</td>
      <td>303299</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4d773c92-f89f-491e-b3e0-3a1d2e863148</td>
      <td>399</td>
      <td>1</td>
      <td>00:08:48.623</td>
      <td>8</td>
      <td>48</td>
      <td>Dribble</td>
      <td>18</td>
      <td>Schalke 04</td>
      <td>Regular Play</td>
      <td>Schalke 04</td>
      <td>Amine Harit</td>
      <td>Center Attacking Midfield</td>
      <td>[88.9, 22.7]</td>
      <td>0.000000</td>
      <td>True</td>
      <td>[93d829df-eea7-416b-95aa-7593828cfade]</td>
      <td>{'outcome': {'id': 8, 'name': 'Complete'}}</td>
      <td>303299</td>
    </tr>
    <tr>
      <th>2</th>
      <td>8a78dce4-998a-4e81-902c-9f3957cebc9d</td>
      <td>460</td>
      <td>1</td>
      <td>00:13:30.202</td>
      <td>13</td>
      <td>30</td>
      <td>Dribble</td>
      <td>23</td>
      <td>Schalke 04</td>
      <td>Regular Play</td>
      <td>Schalke 04</td>
      <td>Daniel Caligiuri</td>
      <td>Right Wing</td>
      <td>[99.5, 68.1]</td>
      <td>0.007309</td>
      <td>True</td>
      <td>[772c5aae-e34e-4364-8a98-7caf7636c90b]</td>
      <td>{'outcome': {'id': 9, 'name': 'Incomplete'}}</td>
      <td>303299</td>
    </tr>
    <tr>
      <th>3</th>
      <td>e44d0122-2f2e-4771-820d-cc326a8b0379</td>
      <td>496</td>
      <td>1</td>
      <td>00:14:10.135</td>
      <td>14</td>
      <td>10</td>
      <td>Dribble</td>
      <td>24</td>
      <td>Schalke 04</td>
      <td>From Throw In</td>
      <td>Schalke 04</td>
      <td>Suat Serdar</td>
      <td>Left Defensive Midfield</td>
      <td>[41.2, 31.7]</td>
      <td>0.000000</td>
      <td>True</td>
      <td>[4de4039f-7efc-461b-b7d6-27c32ec2cd2a]</td>
      <td>{'outcome': {'id': 8, 'name': 'Complete'}}</td>
      <td>303299</td>
    </tr>
    <tr>
      <th>4</th>
      <td>9555afbd-d838-42c9-8f80-be3cd09e4c4a</td>
      <td>793</td>
      <td>1</td>
      <td>00:20:18.409</td>
      <td>20</td>
      <td>18</td>
      <td>Dribble</td>
      <td>33</td>
      <td>Eintracht Frankfurt</td>
      <td>Regular Play</td>
      <td>Eintracht Frankfurt</td>
      <td>Timothy Chandler</td>
      <td>Right Wing Back</td>
      <td>[81.8, 75.7]</td>
      <td>0.000000</td>
      <td>True</td>
      <td>[a5c88cee-6319-4c25-91cd-8a028d8dbfbf]</td>
      <td>{'outcome': {'id': 9, 'name': 'Incomplete'}}</td>
      <td>303299</td>
    </tr>
  </tbody>
</table>



### Competition Events
All events from a given competition can be queried and stored on a single dataframe
```
events = sb.competition_events(
    country="Germany",
    division= "1. Bundesliga",
    season="2019/2020",
    gender="male"
)

grouped_events = sb.competition_events(
    country="Germany",
    division= "1. Bundesliga",
    season="2019/2020",
    split=True
)
grouped_events["dribbles"]
```
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>index</th>
      <th>period</th>
      <th>timestamp</th>
      <th>minute</th>
      <th>second</th>
      <th>type</th>
      <th>possession</th>
      <th>possession_team</th>
      <th>play_pattern</th>
      <th>team</th>
      <th>player</th>
      <th>position</th>
      <th>location</th>
      <th>duration</th>
      <th>under_pressure</th>
      <th>related_events</th>
      <th>dribble</th>
      <th>match_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>b190c01f-ad24-468c-8241-f955b91d996c</td>
      <td>131</td>
      <td>1</td>
      <td>00:02:08.032</td>
      <td>2</td>
      <td>8</td>
      <td>Dribble</td>
      <td>4</td>
      <td>Schalke 04</td>
      <td>Regular Play</td>
      <td>Schalke 04</td>
      <td>Daniel Caligiuri</td>
      <td>Right Wing</td>
      <td>[110.2, 62.9]</td>
      <td>0.000000</td>
      <td>True</td>
      <td>[60f822df-5747-4787-b0f9-45bf5217eb8a]</td>
      <td>{'outcome': {'id': 8, 'name': 'Complete'}}</td>
      <td>303299</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4d773c92-f89f-491e-b3e0-3a1d2e863148</td>
      <td>399</td>
      <td>1</td>
      <td>00:08:48.623</td>
      <td>8</td>
      <td>48</td>
      <td>Dribble</td>
      <td>18</td>
      <td>Schalke 04</td>
      <td>Regular Play</td>
      <td>Schalke 04</td>
      <td>Amine Harit</td>
      <td>Center Attacking Midfield</td>
      <td>[88.9, 22.7]</td>
      <td>0.000000</td>
      <td>True</td>
      <td>[93d829df-eea7-416b-95aa-7593828cfade]</td>
      <td>{'outcome': {'id': 8, 'name': 'Complete'}}</td>
      <td>303299</td>
    </tr>
    <tr>
      <th>2</th>
      <td>8a78dce4-998a-4e81-902c-9f3957cebc9d</td>
      <td>460</td>
      <td>1</td>
      <td>00:13:30.202</td>
      <td>13</td>
      <td>30</td>
      <td>Dribble</td>
      <td>23</td>
      <td>Schalke 04</td>
      <td>Regular Play</td>
      <td>Schalke 04</td>
      <td>Daniel Caligiuri</td>
      <td>Right Wing</td>
      <td>[99.5, 68.1]</td>
      <td>0.007309</td>
      <td>True</td>
      <td>[772c5aae-e34e-4364-8a98-7caf7636c90b]</td>
      <td>{'outcome': {'id': 9, 'name': 'Incomplete'}}</td>
      <td>303299</td>
    </tr>
    <tr>
      <th>3</th>
      <td>e44d0122-2f2e-4771-820d-cc326a8b0379</td>
      <td>496</td>
      <td>1</td>
      <td>00:14:10.135</td>
      <td>14</td>
      <td>10</td>
      <td>Dribble</td>
      <td>24</td>
      <td>Schalke 04</td>
      <td>From Throw In</td>
      <td>Schalke 04</td>
      <td>Suat Serdar</td>
      <td>Left Defensive Midfield</td>
      <td>[41.2, 31.7]</td>
      <td>0.000000</td>
      <td>True</td>
      <td>[4de4039f-7efc-461b-b7d6-27c32ec2cd2a]</td>
      <td>{'outcome': {'id': 8, 'name': 'Complete'}}</td>
      <td>303299</td>
    </tr>
    <tr>
      <th>4</th>
      <td>9555afbd-d838-42c9-8f80-be3cd09e4c4a</td>
      <td>793</td>
      <td>1</td>
      <td>00:20:18.409</td>
      <td>20</td>
      <td>18</td>
      <td>Dribble</td>
      <td>33</td>
      <td>Eintracht Frankfurt</td>
      <td>Regular Play</td>
      <td>Eintracht Frankfurt</td>
      <td>Timothy Chandler</td>
      <td>Right Wing Back</td>
      <td>[81.8, 75.7]</td>
      <td>0.000000</td>
      <td>True</td>
      <td>[a5c88cee-6319-4c25-91cd-8a028d8dbfbf]</td>
      <td>{'outcome': {'id': 9, 'name': 'Incomplete'}}</td>
      <td>303299</td>
    </tr>
  </tbody>
</table>

### 360 Metrics
If you have access to 360 data for a competition, you can set `include_360_metrics=True` in the `events()` and `competition_events()` functions to retrieve 360 metrics such a line breaking passess together with the event data.

The open data does not include the 360 metrics. This is currently only available to customers with a data subscription.

```
events = sb.events(match_id=3837323, include_360_metrics=True)
comp_events = sb.competition_events(
            country="Europe",
            division="Champions League",
            season="2022/2023",
            include_360_metrics=True,
)
comp_events
```
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>50_50</th>
      <th>bad_behaviour_card</th>
      <th>ball_receipt_exceeds_distance</th>
      <th>ball_receipt_in_space</th>
      <th>ball_receipt_outcome</th>
      <th>ball_recovery_offensive</th>
      <th>ball_recovery_recovery_failure</th>
      <th>block_deflection</th>
      <th>block_offensive</th>
      <th>block_save_block</th>
      <th>carry_end_location</th>
      <th>clearance_aerial_won</th>
      <th>clearance_body_part</th>
      <th>clearance_head</th>
      <th>clearance_left_foot</th>
      <th>clearance_other</th>
      <th>clearance_right_foot</th>
      <th>counterpress</th>
      <th>distance_to_nearest_defender</th>
      <th>dribble_no_touch</th>
      <th>dribble_nutmeg</th>
      <th>dribble_outcome</th>
      <th>dribble_overrun</th>
      <th>duel_outcome</th>
      <th>duel_type</th>
      <th>duration</th>
      <th>foul_committed_advantage</th>
      <th>foul_committed_card</th>
      <th>foul_committed_offensive</th>
      <th>foul_committed_penalty</th>
      <th>foul_committed_type</th>
      <th>foul_won_advantage</th>
      <th>foul_won_defensive</th>
      <th>foul_won_penalty</th>
      <th>goalkeeper_body_part</th>
      <th>goalkeeper_end_location</th>
      <th>goalkeeper_lost_in_play</th>
      <th>goalkeeper_lost_out</th>
      <th>goalkeeper_outcome</th>
      <th>goalkeeper_position</th>
      <th>goalkeeper_punched_out</th>
      <th>goalkeeper_shot_saved_off_target</th>
      <th>goalkeeper_shot_saved_to_post</th>
      <th>goalkeeper_success_in_play</th>
      <th>goalkeeper_technique</th>
      <th>goalkeeper_type</th>
      <th>half_start_late_video_start</th>
      <th>id</th>
      <th>index</th>
      <th>injury_stoppage_in_chain</th>
      <th>interception_outcome</th>
      <th>line_breaking_pass</th>
      <th>location</th>
      <th>minute</th>
      <th>miscontrol_aerial_won</th>
      <th>num_defenders_on_goal_side_of_actor</th>
      <th>obv_against_after</th>
      <th>obv_against_before</th>
      <th>obv_against_net</th>
      <th>obv_for_after</th>
      <th>obv_for_before</th>
      <th>obv_for_net</th>
      <th>obv_total_net</th>
      <th>off_camera</th>
      <th>out</th>
      <th>pass_aerial_won</th>
      <th>pass_angle</th>
      <th>pass_assisted_shot_id</th>
      <th>pass_body_part</th>
      <th>pass_cross</th>
      <th>pass_cut_back</th>
      <th>pass_deflected</th>
      <th>pass_end_location</th>
      <th>pass_goal_assist</th>
      <th>pass_height</th>
      <th>pass_inswinging</th>
      <th>pass_length</th>
      <th>pass_miscommunication</th>
      <th>pass_no_touch</th>
      <th>pass_outcome</th>
      <th>pass_outswinging</th>
      <th>pass_recipient</th>
      <th>pass_shot_assist</th>
      <th>pass_straight</th>
      <th>pass_switch</th>
      <th>pass_technique</th>
      <th>pass_through_ball</th>
      <th>pass_type</th>
      <th>pass_xclaim</th>
      <th>period</th>
      <th>play_pattern</th>
      <th>player</th>
      <th>player_id</th>
      <th>player_off_permanent</th>
      <th>position</th>
      <th>possession</th>
      <th>possession_team</th>
      <th>possession_team_id</th>
      <th>related_events</th>
      <th>second</th>
      <th>shot_aerial_won</th>
      <th>shot_body_part</th>
      <th>shot_deflected</th>
      <th>shot_end_location</th>
      <th>shot_first_time</th>
      <th>shot_freeze_frame</th>
      <th>shot_key_pass_id</th>
      <th>shot_one_on_one</th>
      <th>shot_open_goal</th>
      <th>shot_outcome</th>
      <th>shot_redirect</th>
      <th>shot_saved_off_target</th>
      <th>shot_saved_to_post</th>
      <th>shot_statsbomb_xg</th>
      <th>shot_statsbomb_xg2</th>
      <th>shot_technique</th>
      <th>shot_type</th>
      <th>substitution_outcome</th>
      <th>substitution_replacement</th>
      <th>team</th>
      <th>timestamp</th>
      <th>type</th>
      <th>under_pressure</th>
      <th>visible_opponents</th>
      <th>visible_teammates</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3479244f-8234-43c9-a389-4ce587062b48</td>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1</td>
      <td>Regular Play</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1</td>
      <td>Real Madrid</td>
      <td>220</td>
      <td>NaN</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Real Madrid</td>
      <td>00:00:00.000</td>
      <td>Starting XI</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>c4f5a51b-741e-4920-ac32-02349b1f2755</td>
      <td>2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1</td>
      <td>Regular Play</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1</td>
      <td>Real Madrid</td>
      <td>220</td>
      <td>NaN</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Celtic</td>
      <td>00:00:00.000</td>
      <td>Starting XI</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>27be67e7-fdb5-4db9-92b6-8f3214cecec4</td>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1</td>
      <td>Regular Play</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1</td>
      <td>Juventus</td>
      <td>224</td>
      <td>NaN</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Juventus</td>
      <td>00:00:00.000</td>
      <td>Starting XI</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>819c381e-29c1-4f10-a6c3-acc3181cec14</td>
      <td>2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1</td>
      <td>Regular Play</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1</td>
      <td>Juventus</td>
      <td>224</td>
      <td>NaN</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Paris Saint-Germain</td>
      <td>00:00:00.000</td>
      <td>Starting XI</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>e6d42d87-c78a-4286-94fd-4095e9f7b16f</td>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1</td>
      <td>Regular Play</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1</td>
      <td>Manchester City</td>
      <td>36</td>
      <td>NaN</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Manchester City</td>
      <td>00:00:00.000</td>
      <td>Starting XI</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>

### 360 Frames

The frame functions will return the raw 360 freeze frame data along with the visible area for each frame. This is returned at the player level so you have multiple rows per frame/event_id. 
```
match_frames = sb.frames(match_id=3772072, fmt='dataframe')
comp_frames = sb.competition_frames(
    country="Germany",
    division= "1. Bundesliga",
    season="2019/2020"
)
match_frames
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>actor</th>
      <th>distance_from_edge_of_visible_area</th>
      <th>event_uuid</th>
      <th>keeper</th>
      <th>location</th>
      <th>match_id</th>
      <th>teammate</th>
      <th>visible_area</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>False</td>
      <td>5.183739</td>
      <td>065b15cc-b550-48de-9a1e-a9608d8e6c6d</td>
      <td>False</td>
      <td>[79.14114105224532, 12.646560364129726]</td>
      <td>3855869</td>
      <td>False</td>
      <td>[50.8965834880119, 80.0, 55.8915648466696, 6.76382112514142, 80.0765213141343, 1.48859955554994, 113.056993108772, 80.0, 50.8965834880119, 80.0]</td>
    </tr>
    <tr>
      <th>1</th>
      <td>False</td>
      <td>7.784551</td>
      <td>065b15cc-b550-48de-9a1e-a9608d8e6c6d</td>
      <td>False</td>
      <td>[80.68650097437124, 23.040779651892883]</td>
      <td>3855869</td>
      <td>True</td>
      <td>[50.8965834880119, 80.0, 55.8915648466696, 6.76382112514142, 80.0765213141343, 1.48859955554994, 113.056993108772, 80.0, 50.8965834880119, 80.0]</td>
    </tr>
    <tr>
      <th>2</th>
      <td>False</td>
      <td>8.873694</td>
      <td>065b15cc-b550-48de-9a1e-a9608d8e6c6d</td>
      <td>False</td>
      <td>[80.20033992405365, 24.695673759901382]</td>
      <td>3855869</td>
      <td>False</td>
      <td>[50.8965834880119, 80.0, 55.8915648466696, 6.76382112514142, 80.0765213141343, 1.48859955554994, 113.056993108772, 80.0, 50.8965834880119, 80.0]</td>
    </tr>
    <tr>
      <th>3</th>
      <td>False</td>
      <td>9.738309</td>
      <td>065b15cc-b550-48de-9a1e-a9608d8e6c6d</td>
      <td>False</td>
      <td>[82.43349155444821, 32.24426347120625]</td>
      <td>3855869</td>
      <td>False</td>
      <td>[50.8965834880119, 80.0, 55.8915648466696, 6.76382112514142, 80.0765213141343, 1.48859955554994, 113.056993108772, 80.0, 50.8965834880119, 80.0]</td>
    </tr>
    <tr>
      <th>4</th>
      <td>False</td>
      <td>11.049633</td>
      <td>065b15cc-b550-48de-9a1e-a9608d8e6c6d</td>
      <td>False</td>
      <td>[81.320294294838, 32.98015558905158]</td>
      <td>3855869</td>
      <td>True</td>
      <td>[50.8965834880119, 80.0, 55.8915648466696, 6.76382112514142, 80.0765213141343, 1.48859955554994, 113.056993108772, 80.0, 50.8965834880119, 80.0]</td>
    </tr>
  </tbody>
</table>

### Aggregated Stats

For customers we also provide aggregated statistics at the player-match, player-season and team-season levels. 

```
player_match = sb.player_match_stats(3772072)
player_season = sb.player_season_stats(competition_id=9, season_id=42)
team_match = sb.team_match_stats(3772072)
team_season = sb.team_season_stats(competition_id=9, season_id=42)

player_match
```

<table border=\"1\" class=\"dataframe\">
  <thead>
    <tr style=\"text-align: right;\">
      <th></th>
      <th>player_match_pressures</th>
      <th>player_match_long_balls</th>
      <th>player_match_shot_touch_ratio</th>
      <th>player_match_passes_into_box</th>
      <th>player_match_pressure_duration_avg</th>
      <th>player_match_crossing_ratio</th>
      <th>player_match_op_f3_forward_passes</th>
      <th>player_match_passing_ratio</th>
      <th>team_id</th>
      <th>player_match_successful_passes</th>
      <th>player_match_op_xgbuildup_per_possession</th>
      <th>player_match_op_xgchain</th>
      <th>player_match_op_passes_into_box</th>
      <th>player_match_deep_progressions</th>
      <th>player_match_turnovers</th>
      <th>player_match_counterpressured_action_fails</th>
      <th>player_match_passes</th>
      <th>player_match_key_passes</th>
      <th>player_match_dispossessions</th>
      <th>player_match_penalties_won</th>
      <th>player_match_through_balls</th>
      <th>team_name</th>
      <th>player_match_op_passes</th>
      <th>player_match_dribbles</th>
      <th>player_match_clearances</th>
      <th>player_match_forward_passes</th>
      <th>player_match_np_xg_per_shot</th>
      <th>player_match_counterpressures</th>
      <th>player_id</th>
      <th>player_match_op_xa</th>
      <th>player_match_op_xgchain_per_possession</th>
      <th>player_match_minutes</th>
      <th>player_match_pressured_long_balls</th>
      <th>player_match_op_f3_sideways_passes</th>
      <th>player_match_dribbles_faced</th>
      <th>player_match_np_xg</th>
      <th>player_match_goals</th>
      <th>player_match_op_key_passes</th>
      <th>player_match_aerial_ratio</th>
      <th>player_match_op_shots</th>
      <th>player_match_successful_crosses</th>
      <th>player_match_shots_blocked</th>
      <th>player_match_op_f3_passes</th>
      <th>player_match_op_assists</th>
      <th>player_match_long_ball_ratio</th>
      <th>account_id</th>
      <th>player_match_np_shots</th>
      <th>player_match_challenge_ratio</th>
      <th>player_match_touches</th>
      <th>player_match_pressure_regains</th>
      <th>player_match_crosses_into_box</th>
      <th>player_match_fouls</th>
      <th>player_match_sideways_passes</th>
      <th>player_match_aerials</th>
      <th>player_match_touches_inside_box</th>
      <th>player_match_counterpressure_duration_total</th>
      <th>player_match_successful_aerials</th>
      <th>player_match_box_cross_ratio</th>
      <th>player_match_xgbuildup_per_possession</th>
      <th>player_match_dribbled_past</th>
      <th>player_match_pressure_duration_total</th>
      <th>player_match_op_xgbuildup</th>
      <th>player_match_np_shots_on_target</th>
      <th>player_match_interceptions</th>
      <th>player_match_counterpressure_duration_avg</th>
      <th>player_match_xgchain_per_possession</th>
      <th>player_match_successful_long_balls</th>
      <th>player_match_op_f3_backward_passes</th>
      <th>player_match_xgchain</th>
      <th>player_match_tackles</th>
      <th>player_match_assists</th>
      <th>player_match_sp_xa</th>
      <th>player_match_aggressive_actions</th>
      <th>player_name</th>
      <th>player_match_xa</th>
      <th>match_id</th>
      <th>player_match_passes_inside_box</th>
      <th>player_match_possession</th>
      <th>player_match_pressured_action_fails</th>
      <th>player_match_crosses</th>
      <th>player_match_fouls_won</th>
      <th>player_match_xgbuildup</th>
      <th>player_match_backward_passes</th>
      <th>player_match_unpressured_long_balls</th>
      <th>player_match_np_goals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>10</td>
      <td>0.000000</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>0.842105</td>
      <td>870</td>
      <td>32</td>
      <td>0.003191</td>
      <td>0.105292</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>38</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>Arminia Bielefeld</td>
      <td>33</td>
      <td>0</td>
      <td>0</td>
      <td>9</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>9194</td>
      <td>0.000000</td>
      <td>0.003191</td>
      <td>94.21667</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.600000</td>
      <td>48</td>
      <td>0</td>
      <td>NaN</td>
      <td>65</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>29</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>0</td>
      <td>NaN</td>
      <td>0.003191</td>
      <td>0</td>
      <td>NaN</td>
      <td>0.105292</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>0.003191</td>
      <td>6</td>
      <td>0</td>
      <td>0.105292</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>0</td>
      <td>Stefan Ortega</td>
      <td>0.000000</td>
      <td>3772072</td>
      <td>0</td>
      <td>0.491135</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0.105292</td>
      <td>0</td>
      <td>9</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>8.0</td>
      <td>0</td>
      <td>0.033333</td>
      <td>0</td>
      <td>0.570626</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.812500</td>
      <td>870</td>
      <td>13</td>
      <td>0.003726</td>
      <td>0.160582</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>0.0</td>
      <td>16</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>Arminia Bielefeld</td>
      <td>10</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0.034737</td>
      <td>1.0</td>
      <td>9210</td>
      <td>0.043881</td>
      <td>0.007299</td>
      <td>91.90000</td>
      <td>1</td>
      <td>4</td>
      <td>0</td>
      <td>0.034737</td>
      <td>0</td>
      <td>1</td>
      <td>0.285714</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>NaN</td>
      <td>48</td>
      <td>1</td>
      <td>1.0</td>
      <td>30</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>10</td>
      <td>7</td>
      <td>5</td>
      <td>0.327541</td>
      <td>2</td>
      <td>NaN</td>
      <td>0.003726</td>
      <td>0</td>
      <td>4.565010</td>
      <td>0.081964</td>
      <td>0</td>
      <td>0</td>
      <td>0.327541</td>
      <td>0.007299</td>
      <td>0</td>
      <td>2</td>
      <td>0.160582</td>
      <td>1</td>
      <td>0</td>
      <td>0.000000</td>
      <td>9</td>
      <td>Fabian Klos</td>
      <td>0.043881</td>
      <td>3772072</td>
      <td>1</td>
      <td>0.491135</td>
      <td>0.0</td>
      <td>1</td>
      <td>1</td>
      <td>0.081964</td>
      <td>6</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7.0</td>
      <td>13</td>
      <td>0.000000</td>
      <td>1</td>
      <td>1.795411</td>
      <td>0.0</td>
      <td>1</td>
      <td>0.852941</td>
      <td>190</td>
      <td>58</td>
      <td>0.017993</td>
      <td>0.773687</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0.0</td>
      <td>68</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>Union Berlin</td>
      <td>60</td>
      <td>0</td>
      <td>2</td>
      <td>4</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>9164</td>
      <td>0.000000</td>
      <td>0.017993</td>
      <td>94.21667</td>
      <td>2</td>
      <td>3</td>
      <td>0</td>
      <td>0.000000</td>
      <td>0</td>
      <td>0</td>
      <td>0.666667</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>4</td>
      <td>0</td>
      <td>0.615385</td>
      <td>48</td>
      <td>0</td>
      <td>1.0</td>
      <td>122</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>51</td>
      <td>3</td>
      <td>0</td>
      <td>NaN</td>
      <td>2</td>
      <td>0.0</td>
      <td>0.017993</td>
      <td>0</td>
      <td>12.567875</td>
      <td>0.773687</td>
      <td>0</td>
      <td>1</td>
      <td>NaN</td>
      <td>0.019504</td>
      <td>8</td>
      <td>0</td>
      <td>0.838693</td>
      <td>2</td>
      <td>0</td>
      <td>0.043227</td>
      <td>11</td>
      <td>Christopher Trimmel</td>
      <td>0.043227</td>
      <td>3772072</td>
      <td>0</td>
      <td>0.508865</td>
      <td>0.0</td>
      <td>1</td>
      <td>0</td>
      <td>0.773687</td>
      <td>13</td>
      <td>13</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3.0</td>
      <td>4</td>
      <td>0.013699</td>
      <td>1</td>
      <td>0.744943</td>
      <td>NaN</td>
      <td>1</td>
      <td>0.777778</td>
      <td>870</td>
      <td>35</td>
      <td>0.002196</td>
      <td>0.090022</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0.0</td>
      <td>45</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>Arminia Bielefeld</td>
      <td>40</td>
      <td>0</td>
      <td>1</td>
      <td>18</td>
      <td>0.019468</td>
      <td>0.0</td>
      <td>24343</td>
      <td>0.000000</td>
      <td>0.002196</td>
      <td>94.21667</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0.019468</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>0.750000</td>
      <td>48</td>
      <td>1</td>
      <td>NaN</td>
      <td>73</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>22</td>
      <td>1</td>
      <td>1</td>
      <td>NaN</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.003043</td>
      <td>0</td>
      <td>2.234830</td>
      <td>0.090022</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>0.003043</td>
      <td>3</td>
      <td>0</td>
      <td>0.124760</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>3</td>
      <td>Jacob Laursen</td>
      <td>0.000000</td>
      <td>3772072</td>
      <td>0</td>
      <td>0.491135</td>
      <td>0.0</td>
      <td>0</td>
      <td>1</td>
      <td>0.124760</td>
      <td>5</td>
      <td>4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>14.0</td>
      <td>6</td>
      <td>0.000000</td>
      <td>0</td>
      <td>0.592216</td>
      <td>NaN</td>
      <td>0</td>
      <td>0.763158</td>
      <td>870</td>
      <td>29</td>
      <td>0.006048</td>
      <td>0.211669</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0.0</td>
      <td>38</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>Arminia Bielefeld</td>
      <td>36</td>
      <td>0</td>
      <td>1</td>
      <td>7</td>
      <td>NaN</td>
      <td>2.0</td>
      <td>9204</td>
      <td>0.000000</td>
      <td>0.006048</td>
      <td>94.21667</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>0.000000</td>
      <td>0</td>
      <td>0</td>
      <td>0.500000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1.000000</td>
      <td>48</td>
      <td>0</td>
      <td>0.0</td>
      <td>64</td>
      <td>1</td>
      <td>0</td>
      <td>4</td>
      <td>29</td>
      <td>2</td>
      <td>0</td>
      <td>0.676610</td>
      <td>1</td>
      <td>NaN</td>
      <td>0.006048</td>
      <td>3</td>
      <td>8.291025</td>
      <td>0.211669</td>
      <td>0</td>
      <td>2</td>
      <td>0.338305</td>
      <td>0.006048</td>
      <td>6</td>
      <td>0</td>
      <td>0.211669</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>18</td>
      <td>Manuel Prietl</td>
      <td>0.000000</td>
      <td>3772072</td>
      <td>0</td>
      <td>0.491135</td>
      <td>0.0</td>
      <td>0</td>
      <td>1</td>
      <td>0.211669</td>
      <td>2</td>
      <td>6</td>
      <td>0</td>
    </tr>
  </tbody>
</table>

### Raw Files
Alternatively, entities can be accessed as python dictionaries serving as an interface to raw jsons and without performing any preprocessing
```

sb.competitions(fmt="dict")

sb.matches(competition_id=9, season_id=42, fmt="dict")

sb.lineups(match_id=303299, fmt="dict")

sb.events(303299, fmt="dict")

sb.competition_events(
    country="Germany",
    division= "1. Bundesliga",
    season="2019/2020",
    gender="male",
    fmt="dict"
)

sb.frames(3772072, fmt="dict")

sb.competition_frames(
    country="Germany",
    division= "1. Bundesliga",
    season="2021/2022",
    gender="male",
    fmt="dict"
)

sb.player_match_stats(3772072, fmt="dict")

sb.player_season_stats(competition_id=9, season_id=42, fmt="dict")

sb.team_match_stats(3772072, fmt="dict")

sb.team_season_stats(competition_id=9, season_id=42, fmt="dict")

```


## Common Patterns

### Filtering for goals

StatsBomb does not have a dedicated `"Goal"` event type. Goals are encoded as
`Shot` events where `shot_outcome == "Goal"`. Filtering on `type == "Goal"` will
return an empty DataFrame.

```python
events = sb.events(match_id=303299, flatten_attrs=True)

goals = events[
    (events["type"] == "Shot") &
    (events["shot_outcome"] == "Goal")
]
```

To exclude the penalty shootout (period 5), where each kick is an isolated event
rather than part of an open-play sequence:

```python
goals = events[
    (events["type"] == "Shot") &
    (events["shot_outcome"] == "Goal") &
    (events["period"] < 5)
]
```

### Reconstructing possession sequences

Every event carries a `possession` column — an integer that increments each time
possession changes. All events sharing the same `possession` value belong to the
same unbroken sequence, making it the most reliable way to reconstruct the
build-up to a goal.

```python
goal = goals.iloc[0]
buildup = events[events["possession"] == goal["possession"]]
```

For set pieces (penalties, free kicks, corners), the kick itself opens a new
possession sequence. The foul or challenge that earned it belongs to the prior
sequence (`possession - 1`).

```python
prior_possession = events[events["possession"] == goal["possession"] - 1]
```

### Ordering events across periods

The `timestamp` column resets to `00:00:00.000` at the start of each period.
Sorting on `timestamp` alone will produce incorrect ordering in matches that go
to extra time. Use `(period, timestamp)` together for reliable chronological order.

```python
events_sorted = events.sort_values(["period", "timestamp"])
```
