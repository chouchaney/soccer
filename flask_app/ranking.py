def goal_difference(goal_for_count, goal_against_count):
  return goal_for_count - goal_against_count


def points(won_match_count, draw_match_count):
  return 3* won_match_count + draw_match_count


def team_wins_match(team_id, match):
  return  ( match['team0']== team_id and match['score0']> match['score1'])or\
        ( match['team1']== team_id and match['score1']> match['score0'])


def team_loses_match(team_id, match):
  return  ( match['team0']== team_id and match['score0']< match['score1'])or\
        ( match['team1']== team_id and match['score1']< match['score0'])


def team_makes_a_draw(team_id, match):
  return ( ( match['team0']== team_id or  match['team1']== team_id)  and (match['score1']== match['score0']))
    


def goal_for_count_during_a_match(team_id, match):
  return match['score0'] if  match['team0'] == team_id  else  match['score1'] if  match['team1'] == team_id  else 0
    

def goal_against_count_during_a_match(team_id, match):
  return match['score1'] if  match['team0'] == team_id  else  match['score0'] if  match['team1'] == team_id  else 0


def goal_for_count(team_id, matches):
  total_goal=0
  for match in matches :
     total_goal += goal_for_count_during_a_match(team_id, match)
  return total_goal


def goal_against_count(team_id, matches):
  total_goal_against =0
  for match in matches:
     total_goal_against += goal_against_count_during_a_match(team_id, match)
  return total_goal_against


def won_match_count(team_id, matches):
  result = 0
  for match in matches :
    result += 1 if team_wins_match(team_id,match) else 0
  return result

def lost_match_count(team_id, matches):
  result = 0
  for match in matches :
    result += 1 if team_loses_match(team_id,match) else 0
  return result

def draw_match_count(team_id, matches):
  result = 0
  for match in matches :
    result += 1 if team_makes_a_draw(team_id,match) else 0
  return result

def ranking_row(team_id, matches):
  goal_for_count_ = goal_for_count(team_id, matches)
  goal_against_count_ = goal_against_count(team_id, matches)
  won_match_count_ = won_match_count(team_id, matches)
  lost_match_count_ = lost_match_count(team_id, matches)
  draw_match_count_ = draw_match_count(team_id, matches)
  return {'team_id': team_id, 
          'match_played_count': won_match_count_ + lost_match_count_ + draw_match_count_, 
          'won_match_count': won_match_count_, 
          'lost_match_count': lost_match_count_, 
          'draw_match_count': draw_match_count_, 
          'goal_for_count': goal_for_count_, 
          'goal_against_count': goal_against_count_, 
          'goal_difference': goal_difference(goal_for_count_, goal_against_count_), 
          'points': points(won_match_count_, draw_match_count_)
         }



def unsorted_ranking(teams, matches):
  result = []
  for team in teams:
    result += [ranking_row(team['id'], matches)]
  return result


def sorting_key(row):
  return (row['points'], row['goal_difference'], row['goal_for_count'])


def sorted_ranking(teams, matches):
  result = sorted(unsorted_ranking(teams, matches), key=sorting_key, reverse=True)
  for i in range(len(result)):result[i]['rank']= i+1
  return result

