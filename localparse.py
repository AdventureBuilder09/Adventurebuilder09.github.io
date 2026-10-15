import json
import re
import displayCard as draw

#base = input("Please enter the input file (all.json is default)")
base = "all.json"
try:
    with open(base, 'r', encoding='utf-8') as file:
        data = json.load(file)
except json.JSONDecodeError as e:
    print(f"Parse Error: {e.msg}")
    print(f"Line: {e.lineno}, Column: {e.colno}, Position: {e.pos}")
    quit
except FileNotFoundError:
    print("Error: The specified file could not be found.")
    quit


data.sort(key=lambda card : card.get("edhrec_rank"))
head = data
print("Data successfully loaded")
starPTVal = 40
nonePTVal = -2
def cast_int_pt(val):
    if val is None:
        return nonePTVal
    elif val == "*":
        # Return a fixed value depending on where you want '*' to land
        return starPTVal
    try:
        return int(val)
    except (ValueError, TypeError):
        print("Attempt to cast unknown ",val)
        return -3

prinType = 'g'
while True:
    actions = input("""  s - search by scryfall parameters

  r - reset to full database and search

  o<e|p|t|m|n|c> - sort by Edhrec, Power, Toughness, Mana value, Name, or Color identity.
    add a '-' between the o and search type to reverse the order

  * n - set the value of '*' p/t when sorting

  _ n - set the value of undefined p/t when sorting (I.E. planeswalkers)
  
  p <n> <c> [w] [s] - print n cards with c cols, minimum width w, and starting pos s
    (for list printings, c is used as the target width to align text
  
  t <g|l=lm|lpt|lt> - choose how the list is printed, from
    ASCII grid (default),
    a list with card names and mana costs,
    names and P/T, or
    names and type lines
    
  e - exit\n\n""").split("`")
    breakout = False
    for action in actions:
        if len(action) == 0:
            continue
        elif action[0] == 'e':
            breakout = True
            break
        elif action[0] == 't':
            prinType = action[2:].strip()
        elif action[0] == 'o':
            tpos = 2 if action[1] == ' ' else 1
            rev = not action[1] == '-'
            if action[tpos] == 'e':
                data.sort(key=lambda card : card.get("edhrec_rank"), reverse = rev)
                head.sort(key=lambda card : card.get("edhrec_rank"), reverse = rev)
            elif action[tpos] == 'm':
                data.sort(key=lambda card : card.get("cmc"), reverse = rev)
                head.sort(key=lambda card : card.get("cmc"), reverse = rev)
            elif action[tpos] == 'n':
                data.sort(key=lambda card : card.get("name"), reverse = rev)
                head.sort(key=lambda card : card.get("name"), reverse = rev)
            elif action[tpos] == 'c':
                data.sort(key=lambda card : card.get("color_identity"), reverse = rev)
                head.sort(key=lambda card : card.get("color_identity"), reverse = rev)
            elif action[tpos] == 'p':
                data.sort(key=lambda card : cast_int_pt(card.get("power")), reverse = rev)
                head.sort(key=lambda card : cast_int_pt(card.get("power")), reverse = rev)
            elif action[tpos] == 't':
                data.sort(key=lambda card : cast_int_pt(card.get("toughness")), reverse = rev)
                head.sort(key=lambda card : cast_int_pt(card.get("toughness")), reverse = rev)
        elif action[0] == 'p':
            match = re.search("\d+",action)
            num = int(match.group())
            action = action[match.span()[1]:]
            
            match = re.search("\d+",action)
            if(match != None):
                cols = int(match.group())
                action = action[match.span()[1]:]
            else:
                cols = 1
            
            match = re.search("\d+",action)
            if(match != None):
                minwid = int(match.group())
                action = action[match.span()[1]:]
            else:
                minwid = 0
            
            match = re.search("\d+",action)
            if(match != None):
                startpos = int(match.group())
                action = action[match.span()[1]:]
            else:
                startpos = 0

            if (prinType == 'l' or prinType == 'list' or prinType == 'lm'):
                print(draw.listM(head[startpos:], num, cols))
            elif (prinType == 'lpt'):
                print(draw.listPT(head[startpos:], num, cols))
            elif (prinType == 'lt'):
                print(draw.listT(head[startpos:], num, cols))
            else:
                print(draw.grid(head[startpos:], num, cols, minwid))
            continue
        elif action[0] == '*':
            starPTVal = float(re.search("\d+",action).group())
            continue
        elif action[0] == '_':
            nonePTVal = float(re.search("\d+",action).group())
            continue
        elif action[0] == 'r':
            head = data

        if action[0] == 'r' or action[0] == 's':
            for group in re.findall(' (-?)([otn]|pow|tou):(\\/|")(((?<=\\/)([^\\/]|(?<=\\\\)\\/)*)|((?<=")([^"]|(?<=\\\\)")*))\\3', action):
                print(group)
                ind = 0
                while ind < (len(head)):
                    if group[1] == 't':
                        if group[2] == '"':
                            if (len(group[0])>0) == ((group[3]).casefold() in head[ind].get("type_line").casefold()):
                                head.pop(ind)
                                ind -= 1
                        elif (len(group[0])==0) == (re.search(group[3], head[ind].get("type_line"), re.IGNORECASE) == None):
                            head.pop(ind)
                            ind -= 1
                        ind += 1
                    if group[1] == 'o':
                        if group[2] == '"':
                            if (len(group[0])>0) == ((group[3]).casefold() in head[ind].get("oracle_text").casefold()):
                                head.pop(ind)
                                ind -= 1
                        elif (len(group[0])==0) == (re.search(group[3], head[ind].get("oracle_text"), re.IGNORECASE) == None):
                            head.pop(ind)
                            ind -= 1
                        ind += 1
                    if group[1] == 'n':
                        if group[2] == '"':
                            if (len(group[0])>0) == ((group[3]).casefold() in head[ind].get("name").casefold()):
                                head.pop(ind)
                                ind -= 1
                        elif (len(group[0])==0) == (re.search(group[3], head[ind].get("name"), re.IGNORECASE) == None):
                            head.pop(ind)
                            ind -= 1
                        ind += 1
                    if group[1] == 'm':
                        if group[2] == '"':
                            if (len(group[0])>0) == ((group[3]).casefold() in head[ind].get("mana_cost").casefold()):
                                head.pop(ind)
                                ind -= 1
                        elif (len(group[0])==0) == (re.search(group[3], head[ind].get("mana_cost"), re.IGNORECASE) == None):
                            head.pop(ind)
                            ind -= 1
                        ind += 1

                            
    if(breakout):
        break
